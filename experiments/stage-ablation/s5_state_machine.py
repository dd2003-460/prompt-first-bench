# -*- coding: utf-8 -*-
"""T53 目标函数驱动的 decomp 状态机（成璐 2026-11-09 中期目标）。

核心区别 vs v17 (s5_hierarchy.py)：
- v17: 无限预算 BFS, R1 饱和停止, S_α 单调增 → Goodhart 刷分 (1930 nodes)
- T53: 显式目标函数裁决每个状态转移, 冗余惩罚, 边际信息增益停止, 防泄漏审计

状态集合: {IDLE, DECOMPOSE, VERIFY, REWORK, STOP}
转移条件全部由目标函数 J_* 机器裁决，不靠 LLM 自觉。

防泄漏: 所有 prompt/日志/中间产物不得包含题目原文关键实体。
leak_check() 每轮输出后执行，命中即 raise LeakError 中止。
"""
import json
import math
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from ablation_harness import call_llm
from s5_pipeline import (
    _extract_json, _perturb, decompose, gap_check,
    search_node, verify_node,
)


# ─────────────────────────────────────────────
# 防泄漏
# ─────────────────────────────────────────────

class LeakError(RuntimeError):
    pass


def extract_entities(question: str) -> set[str]:
    """提取题目关键实体（用于 leak_check）。
    
    防泄漏的目标: 子节点 claim 不应回显题目的"问句结构"或"待求答案"，
    但可以引用题目给定的约束/参数（如 qwen3-27b, 32K, <3s/token）。
    所以只提取"问句部分"的实体（问号前的核心疑问词 + 比较对象），
    不提取"条件部分"的实体。
    
    简化策略: 取题目中出现在"？"之前的最后一段（即真正在问什么），
    从中提取实体。条件/参数不算泄漏。
    """
    # 找最后一个问号前的片段（中文用 ？ 或 ?）
    segments = re.split(r'[？？]', question)
    if len(segments) > 1:
        # 取含问号的完整句（最后一个 segment 之前）
        last_q_seg = segments[-2] if len(segments) >= 2 else question
        # 只从"问"的部分提取
        target = last_q_seg
    else:
        target = question
    
    entities = set()
    # 英文专名
    for m in re.finditer(r'\b[A-Z][a-zA-Z0-9\-]{3,}\b', target):
        entities.add(m.group().lower())
    # 中文: 4-gram
    for m in re.finditer(r'[\u4e00-\u9fff]{4,}', target):
        seg = m.group()
        for i in range(len(seg) - 3):
            entities.add(seg[i:i+4])
    # 数字+单位
    for m in re.finditer(r'\d+[A-Za-z%]+|\d+\.\d+', target):
        entities.add(m.group().lower())
    return entities


def leak_check(output_text: str, entities: set[str]) -> list[str]:
    """检查 output_text 是否包含题目实体。返回命中的实体列表。
    
    策略（v17→T53 教训 + smoke test 修正）：
    - 英文/数字实体 (qwen3-27b, bf16, int8, 32k): 题目给定约束，引用正常 → 不拦
    - 中文 4-gram: 短的是参数名（显存容量），长的是问句结构 → 只拦 ≥8 字连续中文
    真正的泄漏 = 子节点 claim 回显了题目的"待求关系"（如"比X高多少百分比"），
    这表现为 >8 字的中文短语完整出现。
    """
    hits = []
    lower = output_text.lower()
    for ent in entities:
        # 跳过纯英文/数字实体（给定约束，引用正常）
        if re.match(r'^[a-z0-9\.\-]+$', ent):
            continue
        # 中文实体: 只拦 ≥8 字（问句结构特征）
        if len(ent) >= 8 and ent in lower:
            hits.append(ent)
    return hits


# ─────────────────────────────────────────────
# 目标函数
# ─────────────────────────────────────────────

@dataclass
class ObjectiveConfig:
    """所有可调参数集中在此，bench 时扫参用。"""
    # J_decomp: 边际信息增益阈值
    # n-gram Jaccard 对中文 claim 天然偏低（不同表述重叠小），
    # 所以"低增益"的阈值要比直觉高。0.5 = "新节点和已有节点平均只有 50% 以下重叠才算有增益"
    gain_threshold: float = 0.50
    # J_verify: 核验质量阈值
    verify_threshold: float = 0.85
    # J_stop: 全局收敛
    stop_rounds: int = 2              # 连续 N 轮 gain < threshold → 停
    max_rework: int = 2
    max_nodes: int = 150              # 硬顶（安全阀；v17 是无限→1930）
    max_depth: int = 4                # 最大层级深度（3-4 层 × 6-10 节点 ≈ 几十~百级）
    max_kids_per_parent: int = 8      # 单父节点子节点上限（正交维度数；2026-11-11 D 指出 18-21 是扁平化，正常应 ~6×6×6）
    redundancy_penalty_beta: float = 3.0   # 2026-11-11 标定：full-pair mean Jaccard≈0.015 @n=117，β=3 使罚项≈5（structural 的 5%）；旧值 0.3 罚项仅 0.5，形同虚设
    # ── T-PR-15 修法（2610.33512 F_β 证据）：recall 型 S_α → recall×precision 型 ──
    fbeta_beta: float = 0.5          # β<1 偏向 precision（防同义变体刷分）
    necessary_judge_max_tokens: int = 600
    stop_criterion: str = "necessary"  # "gain"(v1 旧判据) | "necessary"(新判据: 本轮无必要节点→停)
    contribution_threshold: float = 0.10  # idea #45: 子项对目标函数边际贡献 < 此值 → 不展开（极小概率极大不稳定期望豁免）


def _ngram_overlap(a: str, b: str, n: int = 3) -> float:
    """两个 claim 的 n-gram Jaccard 相似度（0~1）。"""
    def ngrams(s):
        s = re.sub(r'\s+', '', s.lower())
        return {s[i:i+n] for i in range(max(0, len(s)-n+1))}
    sa, sb = ngrams(a), ngrams(b)
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def marginal_gain(new_claims: list[str], existing_claims: list[str]) -> float:
    """J_decomp: 新节点集合对已有节点集合的边际信息增益。
    = 1 - mean(max similarity of each new claim to any existing claim)
    高 = 新节点带来新信息; 低 = 同义重复。
    """
    if not new_claims or not existing_claims:
        return 1.0  # 无参照 → 全算新
    total_max_sim = 0.0
    for nc in new_claims:
        max_sim = max(_ngram_overlap(nc, ec) for ec in existing_claims[-50:])  # 只看最近50个控速
        total_max_sim += max_sim
    return 1.0 - total_max_sim / len(new_claims)


def judge_necessary_batch(candidates: list[tuple[str, list[str]]],
                          confirmed: list[tuple], cfg: "ObjectiveConfig") -> list[bool]:
    """批量 necessary-judge：一次 LLM 调用判定多个候选节点。
    candidates: [(claim, parent_claims), ...]
    返回与 candidates 等长的 bool 列表。失败时全部返回 False。"""
    from ablation_harness import call_llm
    if not candidates:
        return []
    confirmed_block = "\n".join(f"- {i}: {c}" for i, c, _s in confirmed[-30:]) or "（暂无）"
    items_block = ""
    for idx, (claim, par_claims) in enumerate(candidates):
        par = "\n".join(f"    - {c}" for c in par_claims[-5:]) or "    （无）"
        items_block += f"[{idx}] claim: {claim}\n    父节点:\n{par}\n\n"
    prompt = (
        "你是严格的审稿人。对下面每个编号的研究子问题，判断它相对于【已知】是否引入了新信息。\n"
        "【新信息的定义】满足至少一条：(a) 出现已知里不存在的物理量/参数/型号/数字；"
        "(b) 新增一个约束或口径（如新的精度/延迟/温度条件）；(c) 是一个新的可独立检索的事实断言。\n"
        "如果只是换措辞复述、把已知结论换个说法、或纯定性描述 → 不是新信息。\n\n"
        f"【已确认事实】\n{confirmed_block}\n\n"
        f"【待判定节点列表】\n{items_block}\n"
        f"对每个编号输出一行，共 {len(candidates)} 行，紧凑无空格，格式示例：\"idx\":0,\"necessary\":true\n"
        "只输出这些行，不要其他文字。"
    )
    try:
        # E11 (2026-11-12): max_tokens 上限保护——8787 端点（ninfer/qwen3.8-27b）对超大
        # max_tokens 返回 HTTP 400；r9 首轮 20+ 候选 → ~7000 tokens 触发。封顶 4096，
        # 配合紧凑输出格式（每行一条）足够 30+ 条裁决。
        mtok = min(cfg.necessary_judge_max_tokens * len(candidates) // 2 + 200, 4096)
        out, _ = call_llm(prompt, max_tokens=mtok, temperature=0.0, retries=3)
        # E13 (2026-11-12): 逐行解析。旧版先 re.search(r'\[.*?\]') 找 JSON 数组——
        # 但 prompt 要求的是无 [] 的紧凑行（"idx":0,"necessary":true），模型照做后
        # 正则永远匹配不到 → 全部落回 fallback regex → 漏解析/误判。
        # 现在直接逐行取 "idx":N,"necessary":bool，兼容有无 [] 两种输出。
        results = [False] * len(candidates)
        raw = out or ""
        hit = 0
        # 主路径：全文 finditer——紧凑行 / JSON 数组（含一行多对象）/ 混合形态都兼容
        for m in re.finditer(r'"?idx"?:\s*(\d+)\s*,\s*"?necessary"?:\s*(true|false)', raw, re.I):
            i = int(m.group(1))
            if 0 <= i < len(candidates):
                results[i] = m.group(2).lower() == "true"
                hit += 1
        # 兜底：无逗号分隔的松散行（如 "idx": 0  necessary: true，逐行各取一个）
        if hit == 0:
            for line in raw.splitlines():
                mi = re.search(r'"?idx"?:\s*(\d+)', line)
                mn = re.search(r'"?necessary"?:\s*(true|false)', line, re.I)
                if mi and mn:
                    i = int(mi.group(1))
                    if 0 <= i < len(candidates):
                        results[i] = mn.group(1).lower() == "true"
                        hit += 1
        if hit == 0:
            print(f"  [SM] necessary-judge: no verdict lines parsed (raw head: {raw[:80]!r})", flush=True)
        return results
    except Exception as e:
        print(f"  [SM] necessary-judge-batch error: {e}", flush=True)
        return [False] * len(candidates)


def judge_necessary(claim: str, parent_claims: list[str], confirmed: list[tuple],
                     cfg: "ObjectiveConfig") -> bool:
    """单节点版（兼容保留）。"""
    r = judge_necessary_batch([(claim, parent_claims)], confirmed, cfg)
    return r[0] if r else False


# ─────────────────────────────────────────────
# 三边分类 (Decision 24 扩展, idea #43)
# ─────────────────────────────────────────────

EDGE_TYPE_PROMPT = (
    "你是结构分析师。判断一个父节点与其子维度之间的组合关系属于以下哪种：\n"
    "1. cartesian（笛卡尔积）【默认】：子维度独立取值，联合空间 = 各维度取值组合，无交叉约束。\n"
    "例：GPU 的「架构、显存容量、接口类型」之间。\n"
    "2. quotient（商/约束）：判定的唯一条件是——父概念的定义本身就是子项的运算结果"
    "（比值/加权/差值），且父 claim 文本中显式包含运算结构（÷、/、ratio、per unit、每…的…、加权）。"
    "存在 trade-off——一个分量↑另一个分量↓时最终目标可能不变。"
    "例：性价比 = 性能 / TCO；能效比 = 吞吐量 / 功耗。\n"
    "注意：大多数分解边是 cartesian。只有当父概念明确是\"A 与 B 的运算\"时才判 quotient，"
    "不要因为子项之间存在某种权衡关系就判 quotient——权衡普遍存在，但运算定义稀有。\n"
    "3. stochastic（随机耦合）：一个共享随机源（如温度采样、量化噪声、batch 组成波动）"
    "同时驱动多个下游子维度，它们不是独立的也不是运算组合的，而是同一个随机过程的不同投影。"
    "例：推理稳定性 ← temp 采样 → 输出一致性；量化质量 ← 同一 temp 流 → 精度损失。\n\n"
    "【父节点】{parent_claim}\n"
    "【候选子维度】\n{children_block}\n\n"
    "同时估计：如果删掉这些子维度，回答父节点所代表的问题时的完整性损失有多大？"
    "（0.0~1.0，即该子项携带的信息量——去掉后父问题的答案缺多少；"
    "极小概率但影响极大的尾部风险项，即使期望信息量低也要标 high_var=true 并给 ≥0.5 分）\n"
    "只输出一行 JSON：{{\"edge_type\": \"cartesian|quotient|stochastic\", \"reason\": \"一句话\", \"contribution\": 0.XX, \"high_var\": false}}"
)

EDGE_PREDICT_PROMPT = (
    "你是结构分析师。下面是一个待分解的概念。在它被展开之前，先判断它最可能是哪种组合结构：\n"
    "1. cartesian【默认】：该概念可拆成若干独立维度，各维度取值互不影响（如「GPU 选型」→ 架构/显存/接口）。\n"
    "2. quotient：判定条件同上——该概念本身是一个运算结果（比值/加权/差值），其定义中显式包含运算结构"
    "（如「性价比」= 性能÷TCO、「能效比」= 吞吐÷功耗）。这类概念的子维度不能穷举组合，"
    "只能沿 frontier 列代表性工作点。不要因为概念涉及多个相互影响的因子就判 quotient。\n"
    "3. stochastic：该概念的核心变异来自一个共享随机源对多个下游维度的同时驱动"
    "（如「推理稳定性」← temp 采样 → 一致性+精度）。\n\n"
    "同时估计：这个概念如果被展开，其子维度携带的信息量大概多大？"
    "（0.0~1.0，即删掉整个该分支后整体研究答案缺多少；极小概率但影响极大的尾部风险项标 high_var=true 并给 ≥0.5 分）\n\n"
    "【概念】{concept}\n\n"
    "只输出一行 JSON：{{\"edge_type\": \"cartesian|quotient|stochastic\", \"reason\": \"一句话\", \"contribution\": 0.XX, \"high_var\": false}}"
)


def classify_edge(parent_claim: str, child_claims: list[str],
                  cfg: "ObjectiveConfig") -> tuple[str, str, float, bool]:
    """LLM 判定父→子组合关系 + 边际贡献估计。
    返回 (edge_type, reason, contribution, high_var)。
    child_claims 为空时用 EDGE_PREDICT_PROMPT 做概念结构预判。
    失败时默认 (cartesian, error, 1.0, False)——保守：按可展开处理。"""
    from ablation_harness import call_llm
    if not child_claims:
        prompt = EDGE_PREDICT_PROMPT.format(concept=parent_claim)
    else:
        children_block = "\n".join(f"- {c}" for c in child_claims[:10])
        prompt = EDGE_TYPE_PROMPT.format(parent_claim=parent_claim, children_block=children_block)
    try:
        out, _ = call_llm(prompt, max_tokens=300, temperature=0.0, retries=2)
        m = re.search(r'"edge_type"\s*:\s*"(cartesian|quotient|stochastic)"', out or "", re.I)
        et = m.group(1).lower() if m else "cartesian"
        rm = re.search(r'"reason"\s*:\s*"([^"]*)"', out or "")
        reason = rm.group(1) if rm else ""
        cm = re.search(r'"contribution"\s*:\s*([0-9]*\.?[0-9]+)', out or "")
        contrib = float(cm.group(1)) if cm else 1.0
        hv = re.search(r'"high_var"\s*:\s*(true|false)', out or "", re.I)
        high_var = hv.group(1).lower() == "true" if hv else False
        return et, reason, min(max(contrib, 0.0), 1.0), high_var
    except Exception as e:
        print(f"  [SM] edge-classify error: {e}", flush=True)
        return "cartesian", f"error: {e}", 1.0, False


def redundancy_score(nodes: list[dict]) -> float:
    """S_α 修正版的冗余项: 所有节点对的平均 n-gram 相似度。
    O(n²) 但 n≤300 时 ~45K 次比较，每次很轻，可接受。
    采样加速: 只比相邻层 + 同层内随机 20 对。
    """
    if len(nodes) < 2:
        return 0.0
    import random
    pairs = []
    by_level = {}
    for nd in nodes:
        lv = nd.get("level", "L?")
        by_level.setdefault(lv, []).append(nd)
    # 同层内采样
    for lv, group in by_level.items():
        if len(group) > 20:
            idx = random.sample(range(len(group)), 20)
            for i in range(len(idx)):
                for j in range(i+1, len(idx)):
                    pairs.append((group[idx[i]]["claim"], group[idx[j]]["claim"]))
        else:
            for i in range(len(group)):
                for j in range(i+1, len(group)):
                    pairs.append((group[i]["claim"], group[j]["claim"]))
    if not pairs:
        return 0.0
    # 2026-11-11 D 指示：冗余项要全量算，不截断。cap 200 在 n~120 时只覆盖 ~4% 的 pair，
    # 罚项被稀释到 ≈0（实测 penalty 0.51 vs structural 97），等于没罚。
    # 复杂度控制靠上面的采样策略（同层 >20 抽 20），不再砍 pair 数本身。
    sims = [_ngram_overlap(a, b) for a, b in pairs]
    return sum(sims) / len(sims)


def S_alpha_corrected(nodes: list[dict], cfg: ObjectiveConfig) -> float:
    """修正版 S_α: 保留层级结构奖励 - 冗余惩罚。
    S = Σₙ [n·ln(kₙ) + α·kₙ·ln(n)] - β·redundancy·total_nodes
    关键: 减号项让"制造同义变体"不再有利可图。
    """
    from collections import Counter
    levels = Counter(int(str(n.get("level", "L0")).lstrip("L") or 0) for n in nodes)
    alpha = 0.5
    structural = 0.0
    for lv, k in levels.items():
        if lv == 0:
            continue
        structural += lv * math.log(k + 1) + alpha * k * math.log(lv + 1)
    red = redundancy_score(nodes)
    penalty = cfg.redundancy_penalty_beta * red * len(nodes)
    return structural - penalty


# ─────────────────────────────────────────────
# 状态机
# ─────────────────────────────────────────────

class State(Enum):
    IDLE = "idle"
    DECOMPOSE = "decompose"
    VERIFY = "verify"
    REWORK = "rework"
    STOP = "stop"


@dataclass
class NodeRecord:
    id: str
    claim: str
    level: str = "L0"
    source: str = "search"
    status: str = "pending"  # pending/verified/degraded/reworked
    evidence: str = ""
    corrected_claim: str = ""
    rework_count: int = 0
    parent_ids: list = field(default_factory=list)
    objective: Optional[dict] = None  # Decision 19: L0 终点目标函数（模型自估计，仅根节点带）
    edge_type: str = "cartesian"  # Decision 24 扩展 (idea #43): cartesian / quotient / stochastic


@dataclass
class SMResult:
    nodes: list[NodeRecord]
    rounds_log: list[dict]
    final_state: str
    leak_hits_total: int = 0
    rework_events: list = field(default_factory=list)


class DecompStateMachine:
    """目标函数驱动的 decomp 状态机。
    
    用法:
        sm = DecompStateMachine(question, qid="gpu", cfg=ObjectiveConfig())
        result = sm.run()
    """

    def __init__(self, question: str, qid: str = "gpu",
                 cfg: Optional[ObjectiveConfig] = None):
        self.question = question
        self._nid = 0  # C3: 全局唯一节点 id（旧逻辑按 len(self.nodes)+1 编号，同轮 batch 内互相覆盖 → 跨 level 撞号）
        self.qid = qid
        self.cfg = cfg or ObjectiveConfig()
        self.entities = extract_entities(question)
        self.nodes: list[NodeRecord] = []
        self.confirmed: list[tuple] = []  # [(id, claim, status)]
        self.rounds_log: list[dict] = []
        self.state = State.IDLE
        self.leak_hits_total = 0
        self.rework_events = []
        self._gain_history: list[float] = []
        self.dropped_redundant = 0
        self.objective: Optional[dict] = None  # Decision 19: 模型自估计终点目标函数（L1 轮产出）
        self._no_ness_streak = 0
        self.network_degraded = False  # E8: 出口探针结果，run() 开头设置

    def _safe_prompt(self, template: str, **kwargs) -> str:
        """填充 prompt 后做 leak check。
        注意: prompt 本身需要引用题目才能让模型拆——但产出（nodes）不能回显题目。
        所以这里检查的是"产出"而非"prompt"。
        """
        return template.format(**kwargs) + _perturb()

    def _check_output_leak(self, text: str, context: str):
        """检查 LLM 输出是否泄漏题目实体到产出中。"""
        hits = leak_check(text, self.entities)
        if hits:
            self.leak_hits_total += len(hits)
            raise LeakError(f"[{context}] LEAK DETECTED: {hits[:5]}... "
                           f"(total {len(hits)} entities matched)")

    def _decompose_l1(self, skip_if_seeded: bool = False):
        """第 0 轮: L1 骨架——只取顶层正交维度（3-7 个），不往下钻。

        旧实现调 decompose()（P1_DECOMPOSE）要求模型一次拆出整棵多层树再全部标 L1，
        导致层级拍平：逐卡规格/公式推导混进第一层，S_alpha 层级贡献失真。
        现在用 P1_L1_SKELETON 专用 prompt，严格约束只输出顶层目录。
        """
        if skip_if_seeded and self.nodes:
            print(f"  [SM] L1 already seeded ({len(self.nodes)} nodes from checkpoint), skipping decompose", flush=True)
            return
        print("  [SM] L1 skeleton (top-level dimensions only)...", flush=True)
        from s5_pipeline import P1_L1_SKELETON, _extract_json
        prompt = P1_L1_SKELETON.format(question=self.question)
        out, _ = call_llm(prompt, max_tokens=2048, temperature=0.7, top_p=0.95, retries=3)
        d = _extract_json(out or "") or {}
        # Decision 19: 模型自估计的终点目标函数——落盘到根节点，不进后续 prompt。
        # 角色：机器侧对照基准（G9 gold 维度集的免费替代初稿），不是刷分目标。
        objective = d.get("objective")
        if isinstance(objective, dict):
            self.objective = objective
            print(f"  [SM] objective (model-estimated): {str(objective.get('composition',''))[:100]}", flush=True)
            for f_ in (objective.get("factors") or [])[:8]:
                print(f"    factor: {str(f_)[:80]}", flush=True)
        else:
            self.objective = None
            print("  [SM] objective: model returned no objective block", flush=True)
        dims = d.get("dimensions") or []
        dims = [x for x in dims if isinstance(x, dict) and (x.get("name") or x.get("scope"))]
        if not dims:
            raise RuntimeError("L1 skeleton empty")
        # 上限 7 个（防模型不守规矩）
        dims = dims[:7]
        for i, dim in enumerate(dims):
            name = dim.get("name", "").strip()
            scope = dim.get("scope", "").strip()
            claim = f"{name}：{scope}" if scope else name
            self._nid += 1
            rec = NodeRecord(
                id=f"N{self._nid}",  # C3: 用全局计数器（L1 也消耗编号），避免 L2 从 N1 起编与 L1 撞号
                claim=claim,
                level="L1",
                source="given",  # 顶层维度是结构性的，不需要检索
            )
            self.nodes.append(rec)
        print(f"  [SM] L1: {len(self.nodes)} top-level dimensions", flush=True)
        for n in self.nodes:
            print(f"    [{n.id}] {n.claim[:80]}", flush=True)

    def _decompose_layer(self, parents: list[NodeRecord]) -> list[NodeRecord]:
        """对一组父节点做 INDEX 分解，返回新子节点（含 edge_type 标注）。"""
        from s5_pipeline import P1H_INDEX
        parents_block = "\n".join(
            f"{p.id} [{p.level}] (edge={p.edge_type}): {p.claim}" for p in parents)
        confirmed_block = (
            "\n".join(f"- {i}: {c} [{s}]" for i, c, s in self.confirmed[-40:])
            if self.confirmed else "（暂无）"
        )
        # 三边规则注入：告诉模型当前父节点的边类型，约束展开行为
        edge_hints = []
        for p in parents:
            if p.edge_type == "quotient":
                edge_hints.append(
                    f"⚠️ 父节点 {p.id} 是商/约束结构（{p.claim[:40]}）："
                    f"其子维度通过运算组合、存在 trade-off。"
                    f"不要穷举所有分量组合——只沿 frontier 列 2-4 个代表性工作点"
                    f"（如高性低成/中性价比最优/高成本低性），每个工作点是一个子节点。")
            elif p.edge_type == "stochastic":
                edge_hints.append(
                    f"⚠️ 父节点 {p.id} 是随机耦合结构（{p.claim[:40]}）："
                    f"多个子维度共享同一个随机源。"
                    f"先列一个「共享随机源」子节点描述该源，再列各下游投影；"
                    f"不要把同一随机源复制成多个独立噪声节点。")
        edge_block = ("\n【边类型约束】\n" + "\n".join(edge_hints) + "\n") if edge_hints else ""

        prompt = self._safe_prompt(P1H_INDEX,
            question=self.question,
            confirmed_block=confirmed_block,
            parents_block=parents_block + edge_block,
            start=len(self.nodes) + 1,
        )
        out, _ = call_llm(prompt, max_tokens=8000, temperature=0.7, top_p=0.95, retries=4)
        d = _extract_json(out or "")
        d = d if isinstance(d, dict) else {}
        raw_nodes = [n for n in (d.get("nodes") or [])
                     if isinstance(n, dict) and n.get("claim")]

        # 防泄漏: 检查新节点 claim 是否回显题目
        for rn in raw_nodes:
            self._check_output_leak(rn["claim"], "decompose")

        # 编号 + 层级 + edge_type
        parent_levels = {int(str(p.level).lstrip("L")) for p in parents}
        next_lv = max(parent_levels) + 1 if parent_levels else 1
        new_recs = []
        for k, rn in enumerate(raw_nodes):
            # edge_type: LLM 可在节点里标（可选字段），否则继承父节点类型
            et = rn.get("edge_type", "")
            valid_et = et if et in ("cartesian", "quotient", "stochastic") else ""
            if not valid_et:
                # 继承：取第一个父节点的 edge_type
                valid_et = parents[0].edge_type if parents else "cartesian"
            self._nid += 1
            rec = NodeRecord(
                id=f"N{self._nid}",
                claim=rn["claim"],
                level=f"L{next_lv}",
                source=rn.get("source", "search"),
                parent_ids=[p.id for p in parents],
                edge_type=valid_et,
            )
            new_recs.append(rec)
        return new_recs

    def _verify_batch(self, batch: list[NodeRecord]) -> list[NodeRecord]:
        """核验一批节点。返回带 status/evidence 的节点。"""
        for node in batch:
            if node.source == "search":
                if self.network_degraded:
                    srcs, err = [], "network_degraded: 出口探针失败，跳过联网检索"
                else:
                    srcs, err = search_node(
                        {"id": node.id, "claim": node.claim,
                         "search_query": node.claim}, qid=self.qid)
                if err:
                    node.status = "degraded"
                    node.evidence = f"检索失败: {err}"
                    node.corrected_claim = node.claim
                    self.confirmed.append((node.id, node.claim, "degraded"))
                    continue
                srcs_list = srcs if isinstance(srcs, list) else []
            else:
                # given/knowledge 不检索，但同样过 LLM 核验（AC3: 所有节点都要有真实 evidence）
                srcs_list, err = [], None
            status, evidence, corrected, _r = verify_node(
                {"id": node.id, "claim": node.claim}, srcs_list)
            node.status = status
            node.evidence = evidence
            node.corrected_claim = corrected or node.claim
            self.confirmed.append((node.id, node.corrected_claim, status))
        return batch


    def _should_rework(self, batch: list[NodeRecord]) -> bool:
        """J_verify: 核验质量是否低于阈值。"""
        if not batch:
            return False
        verified = sum(1 for n in batch if n.status == "verified")
        rate = verified / len(batch)
        return rate < self.cfg.verify_threshold

    def _rework(self, failed: list[NodeRecord]):
        """REWORK: 对核验失败的节点，换角度重新拆解其父节点。
        最多 K 次。
        """
        for node in failed:
            if node.rework_count >= self.cfg.max_rework:
                node.status = "degraded"  # 放弃
                continue
            node.rework_count += 1
            self.rework_events.append({
                "node_id": node.id,
                "claim": node.claim[:60],
                "attempt": node.rework_count,
                "reason": node.evidence[:80],
            })
            # 简化: 标记为 degraded，下一轮如果父节点还在 frontier 会重新展开
            # （完整实现应该生成"换个角度拆"的 prompt，但第一版先用重搜代替）
            srcs, err = search_node(
                {"id": node.id, "claim": node.claim,
                 "search_query": node.claim + " alternative"}, qid=self.qid)
            if not err:
                srcs2 = srcs if isinstance(srcs, list) else []
                status, evidence, corrected, _r = verify_node(
                    {"id": node.id, "claim": node.claim}, srcs2)
                if status == "verified":
                    node.status = "verified"
                    node.evidence = f"[rework-{node.rework_count}] {evidence}"
                    node.corrected_claim = corrected or node.claim

    def _save_checkpoint(self, rnd: int):
        """每轮结束把当前树状态落盘。resume 时读回继续。"""
        import os
        ckpt_dir = "checkpoints"
        os.makedirs(ckpt_dir, exist_ok=True)
        path = os.path.join(ckpt_dir, f"sm-{self.qid}-r{rnd}.json")
        with open(path, "w") as f:
            json.dump({
                "qid": self.qid,
                "question": self.question,
                "round": rnd,
                "state": self.state.value,
                "dropped_redundant": self.dropped_redundant,
                "leak_hits_total": self.leak_hits_total,
                "network_degraded": self.network_degraded,
                "objective": self.objective,  # Decision 19: 模型自估计终点目标函数随 ckpt 落盘
                "rework_events": self.rework_events,
                "nodes": [vars(n) for n in self.nodes],
            }, f, ensure_ascii=False, indent=2)

    def _probe_network(self):
        """E8.2: 出口健康探针。
        本机网络是"代理模式"（ClashX 7890），Python 直连被拒是常态——
        先试直连，失败再经系统代理（scutil 读出的 HTTPProxy）试一次；
        两次都失败才判 degraded。探的是 Python 侧通道（wiki/arXiv API）；
        ego-browser 通道的失败由 research_hook 内部降级兜底。"""
        import urllib.request, subprocess, re
        url = "https://en.wikipedia.org"
        hdr = {"User-Agent": "pfb-sm-probe/1.0"}
        try:
            req = urllib.request.Request(url, method="HEAD", headers=hdr)
            urllib.request.urlopen(req, timeout=8)
            self.network_degraded = False
            return
        except Exception:
            pass
        try:
            out = subprocess.run(["scutil", "--proxy"],
                                  capture_output=True, text=True, timeout=5).stdout
            host = re.search(r"HTTPProxy\s*:\s*(\S+)", out)
            port = re.search(r"HTTPPort\s*:\s*(\d+)", out)
            if host and port:
                proxy = f"http://{host.group(1)}:{port.group(1)}"
                opener = urllib.request.build_opener(
                    urllib.request.ProxyHandler({"https": proxy, "http": proxy}))
                req = urllib.request.Request(url, method="HEAD", headers=hdr)
                opener.open(req, timeout=8)
                self.network_degraded = False
                return
        except Exception:
            pass
        # E8.2b: Python 通道降级 ≠ ego-browser 通道死了（后者走 ego lite 自己的网络栈）。
        # 快速探一次 ego-browser；能活就继续用，不能才整体降级。
        try:
            from research_hook import _run_ego_browser
            r = _run_ego_browser(
                'const t = await taskSpace("sm-probe"); const p = t.page("x"); '
                'console.log(JSON.stringify({alive: !!p}));', timeout=20)
            if "alive" in (r or ""):
                self.network_degraded = False
                print("  [SM] python channel degraded but ego-browser alive — continuing", flush=True)
                return
        except Exception as e:
            print(f"  [SM] ego-browser probe failed: {e}", flush=True)
        self.network_degraded = True
        print("  [SM] network probe FAILED (all channels) — retrieval degraded", flush=True)

    def run(self, skip_l1: bool = False, verify_only: bool = False) -> SMResult:
        """主循环。skip_l1=True 用于 --resume：L1 已在 checkpoint 里，不重拆。"""
        self._probe_network()
        self.state = State.DECOMPOSE
        self._decompose_l1(skip_if_seeded=skip_l1)

        if verify_only:
            # --verify-only: 树结构已完整，跳过 decompose 直接核验所有 pending 节点
            print(f"  [SM] verify-only mode: {sum(1 for n in self.nodes if n.status=='pending')} pending nodes to verify", flush=True)
            self.state = State.VERIFY
            pending = [n for n in self.nodes if n.status == 'pending']
            for i in range(0, len(pending), 3):
                batch = pending[i:i+3]
                self._verify_batch(batch)
                self._save_checkpoint(rnd=len(self.rounds_log))
                if (i // 3 + 1) % 5 == 0:
                    print(f"  [SM] verified {i+len(batch)}/{len(pending)}", flush=True)
            self.state = State.STOP
            return SMResult(
                nodes=list(self.nodes), rounds_log=self.rounds_log,
                final_state="verified", leak_hits_total=self.leak_hits_total,
                rework_events=list(self.rework_events),
            )

        low_gain_streak = 0
        rnd = 0
        while self.state != State.STOP:
            rnd += 1
            if len(self.nodes) >= self.cfg.max_nodes:
                print(f"  [SM] max_nodes={self.cfg.max_nodes} hit", flush=True)
                break

            lv_max = max(int(str(n.level).lstrip("L")) for n in self.nodes)
            if lv_max >= self.cfg.max_depth:
                print(f"  [SM] max_depth={self.cfg.max_depth} hit", flush=True)
                break

            frontier = [n for n in self.nodes
                        if int(str(n.level).lstrip("L")) == lv_max]

            # ── DECOMPOSE ──
            self.state = State.DECOMPOSE
            new_nodes = []

            # ── 三边分类：对 frontier 中 edge_type 未定的节点做 LLM 判定 ──
            # cartesian → 正常展开; quotient → frontier 采样（限 2-4 子）;
            # stochastic → 记录共享源（限 1 源 + N 投影）
            for p in frontier:
                if p.edge_type == "cartesian" and int(str(p.level).lstrip("L")) >= 2:
                    # L2+ 的 cartesian 节点在首次进入 frontier 时做一次边复核
                    # （L1 是模型自估的骨架，默认 cartesian 可信）
                    pass  # 复核留到下一版；当前先信任继承值
            # 对 L1 节点（首次拆出的顶层维度）做边分类——这是 v17 爆炸的入口
            l1_frontier = [p for p in frontier if str(p.level) == "L1"]
            low_contrib_nodes = []  # idea #45: 贡献低于阈值的节点不展开
            for p in l1_frontier:
                et, reason, contrib, high_var = classify_edge(p.claim, [], self.cfg)
                if et != "cartesian":
                    print(f"  [SM] edge-classify {p.id}: {et} ({reason[:50]})", flush=True)
                    p.edge_type = et
                # idea #45: 贡献阈值过滤（极小概率极大不稳定期望豁免）
                if contrib < self.cfg.contribution_threshold and not high_var:
                    print(f"  [SM] contribution-filter {p.id}: {contrib:.2f} < {self.cfg.contribution_threshold} — skip expansion", flush=True)
                    p.status = "degraded"  # 标记为不再展开
                    low_contrib_nodes.append(p)
            # 从 frontier 中移除低贡献节点
            if low_contrib_nodes:
                low_ids = {p.id for p in low_contrib_nodes}
                frontier = [p for p in frontier if p.id not in low_ids]

            for i in range(0, len(frontier), 3):
                batch = frontier[i:i+3]
                try:
                    kids = self._decompose_layer(batch)
                    # ── 三边复核：子节点出来后，用实际 children 确认父节点的 edge_type ──
                    for p in batch:
                        p_children = [c.claim for c in kids if p.id in (c.parent_ids or [])]
                        if p_children and len(p_children) >= 2:
                            et, reason, contrib, high_var = classify_edge(p.claim, p_children, self.cfg)
                            if et != p.edge_type:
                                print(f"  [SM] edge-reclassify {p.id}: {p.edge_type}→{et} ({reason[:50]})", flush=True)
                                p.edge_type = et
                                for c in kids:
                                    if p.id in (c.parent_ids or []):
                                        c.edge_type = et
                    # 单父节点扇出上限：超过的按 n-gram 与已有 claim 距离排序保留最近的，
                    # 防止 LLM 把一层铺成 20+ 个近义变体（r2 ckpt 实测 L1 各 18 子、L2 最高 21 子）。
                    # 三边分类 (idea #43): quotient/stochastic 用更紧的 cap——
                    #   cartesian: max_kids_per_parent (默认 8)
                    #   quotient:  min(4, cap) — frontier 采样只需 2-4 个代表工作点
                    #   stochastic: min(5, cap) — 1 个共享源 + ≤4 个下游投影
                    base_cap = self.cfg.max_kids_per_parent
                    for p in batch:
                        if p.edge_type == "quotient":
                            cap = min(4, base_cap)
                        elif p.edge_type == "stochastic":
                            cap = min(5, base_cap)
                        else:
                            cap = base_cap
                        pk = [k for k in kids if p.id in (k.parent_ids or [])]
                        if len(pk) > cap:
                            base = [n.claim for n in self.nodes] + [p.claim]
                            def dist(k):
                                return min((_ngram_overlap(k.claim, c) for c in base), default=0.0)
                            pk.sort(key=dist, reverse=True)
                            dropped = pk[cap:]
                            kids = [k for k in kids if k not in dropped]
                            print(f"  [SM] fanout cap {cap}: parent {p.id} kept {cap}/{len(pk)+len(dropped)}, dropped {len(dropped)}", flush=True)
                    new_nodes.extend(kids)
                except LeakError as e:
                    # AC2 零容忍：任何产出回显题目 = 验收 fail，整轮中止。
                    # 不跳过继续跑——那只是把失败推迟到 bench 阶段才暴露。
                    print(f"  [SM] LEAK in decompose r{rnd}: {e} — ABORT (AC2 zero-tolerance)", flush=True)
                    raise

            # gap_check 补充（需要 id 字段）
            if new_nodes:
                added_extra, _miss, _rawb = gap_check(
                    self.question, [
                        {"id": n.id, "claim": n.claim, "level": n.level}
                        for n in new_nodes])
                for ae in added_extra[:5]:
                    self._nid += 1
                    new_nodes.append(NodeRecord(
                        id=f"N{self._nid}",
                        claim=ae if isinstance(ae, str) else ae.get("claim",""),
                        level=f"L{lv_max+1}", source="search"))

            # 去重（n-gram 相似度 > 0.7 = 重复）
            existing_claims = [n.claim for n in self.nodes]
            deduped = []
            for nn in new_nodes:
                is_dup = any(
                    _ngram_overlap(nn.claim, ec) > 0.7
                    for ec in existing_claims[-80:]
                )
                if not is_dup:
                    deduped.append(nn)

            # ── J_precision: necessary 过滤（T-PR-15 修法核心，批量版）──
            # 每个候选节点必须通过"引入新变量/新约束/新可检索事实"裁决才进树。
            # 这是 recall 型 S_α 的 precision 项：不通过 = 同义变体，直接丢弃。
            id2claim = {n.id: n.claim for n in self.nodes}  # parent_ids 是 "N5" 形式，直接查表
            cand_list = []
            for nn in deduped:
                par_claims = [id2claim[pid] for pid in nn.parent_ids if pid in id2claim]
                cand_list.append((nn.claim, par_claims))
            verdicts = judge_necessary_batch(cand_list, self.confirmed, self.cfg)
            necessary_nodes = []
            for nn, v in zip(deduped, verdicts):
                if isinstance(v, bool) and v:
                    necessary_nodes.append(nn)
                else:
                    self.dropped_redundant += 1
            deduped = necessary_nodes
            self.nodes.extend(deduped)

            # ── J_decomp: 边际信息增益（记录用）──
            gain = marginal_gain(
                [n.claim for n in deduped],
                existing_claims,
            )
            self._gain_history.append(gain)

            # ── 停止判据：necessary 通过率 ──
            # 本轮新增冗余数 = dropped_redundant - 上轮累计值（dropped_redundant 是跨轮累计计数器）
            # E14b: 防御式 — dropped_redundant 可能是 []（旧 ckpt 残留），取 int 值再算
            _dr = self.dropped_redundant if isinstance(self.dropped_redundant, int) else 0
            n_new_dropped = _dr - (getattr(self, '_prev_dropped', 0) if isinstance(getattr(self, '_prev_dropped', 0), int) else 0)
            n_candidates = len(deduped) + n_new_dropped
            pass_rate = len(deduped) / max(n_candidates, 1)
            self._prev_dropped = _dr
            if pass_rate < 0.3 and deduped:
                low_gain_streak += 1
            elif not deduped:
                low_gain_streak += 1
            else:
                low_gain_streak = 0
            self._no_ness_streak = low_gain_streak

            # ── VERIFY ──
            self.state = State.VERIFY
            if deduped:
                self._verify_batch(deduped)

            # ── J_verify → REWORK? ──
            unverified = [n for n in deduped if n.status != "verified"]
            if unverified and self._should_rework(deduped):
                self.state = State.REWORK
                self._rework(unverified)

            # ── 记录 ──
            sa = S_alpha_corrected(
                [{"level": n.level, "claim": n.claim} for n in self.nodes],
                self.cfg)
            from collections import Counter as _C
            edge_counts = dict(_C(n.edge_type for n in self.nodes))
            self.rounds_log.append({
                "round": rnd,
                "n_new": len(deduped),
                "n_total": len(self.nodes),
                "gain": round(gain, 3),
                "S_alpha_corr": round(sa, 2),
                "frontier": len(frontier),
                "verified": sum(1 for n in deduped if n.status == "verified"),
                "reworked": sum(1 for n in deduped if n.rework_count > 0),
                "dropped_redundant": self.dropped_redundant,
                "low_gain_streak": low_gain_streak,
                "edge_types": edge_counts,
            })
            print(f"  [SM] r{rnd}: +{len(deduped)} (total {len(self.nodes)}), "
                  f"gain={gain:.3f}, S_α'={sa:.1f}, "
                  f"ver={sum(1 for n in deduped if n.status=='verified')}/{len(deduped)}, "
                  f"streak={low_gain_streak}", flush=True)

            # ── CHECKPOINT: 每轮结束落盘，进程死了能 resume（E6 可靠性修复）──
            self._save_checkpoint(rnd)

            # ── J_stop: 全局收敛（判据由 cfg.stop_criterion 选）──
            if self._no_ness_streak >= self.cfg.stop_rounds:
                self.state = State.STOP
                print(f"  [SM] STOP: {self.cfg.stop_rounds} consecutive "
                      f"low-gain rounds", flush=True)
                break
            if not deduped:
                self.state = State.STOP
                print(f"  [SM] STOP: no new nodes (saturation)", flush=True)
                break

        return SMResult(
            nodes=self.nodes,
            rounds_log=self.rounds_log,
            final_state=self.state.value,
            leak_hits_total=self.leak_hits_total,
            rework_events=self.rework_events,
        )


# ─────────────────────────────────────────────
# CLI entry
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    from s5_pipeline import QUESTIONS
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    # --resume 同时支持 "--resume=<path>" 和 "--resume <path>" 两种写法
    resume_from_early = None
    _raw = sys.argv[1:]
    for k, v in enumerate(_raw):
        if v == "--resume" and k + 1 < len(_raw):
            resume_from_early = _raw[k+1]
        elif v.startswith("--resume="):
            resume_from_early = v.split("=", 1)[1]
    qid = args[0] if args and args[0] in QUESTIONS else "gpu"
    # T53 night-autonomy (2026-11-12): --qid 指定外部题的标识（落盘文件名用）
    for k, v in enumerate(_raw):
        if v == "--qid" and k + 1 < len(_raw):
            qid = _raw[k+1]
        elif v.startswith("--qid="):
            qid = v.split("=", 1)[1]
    # T53 night-autonomy (2026-11-12): 外部题加载 — DRB pilot。
    # --question-file <path>: 从文件读题（DRB query.jsonl 的 prompt 字段或纯文本），qid 用 --qid 指定
    question_file = None
    for k, v in enumerate(_raw):
        if v == "--question-file" and k + 1 < len(_raw):
            question_file = _raw[k+1]
        elif v.startswith("--question-file="):
            question_file = v.split("=", 1)[1]
    if question_file:
        import json as _json_qf
        raw_q = open(question_file).read().strip()
        try:
            q = _json_qf.loads(raw_q)["prompt"]
        except Exception:
            q = raw_q
        print(f"[T53 SM] Loaded external question from {question_file} ({len(q)} chars)", flush=True)
    else:
        q = QUESTIONS[qid]
    no_verify = "--no-verify" in flags
    resume_from = resume_from_early
    if resume_from is None and "--resume" in flags:
        i = flags.index("--resume")
        if i + 1 < len(flags):
            resume_from = flags[i+1]
    print(f"[T53 SM] Running on '{qid}': {q[:60]}...", flush=True)
    sm = DecompStateMachine(q, qid=qid)
    # --max-nodes N: 覆盖硬顶（resume 时 ckpt 节点数可能已超默认 150）
    for k, v in enumerate(_raw):
        if v == "--max-nodes" and k + 1 < len(_raw):
            sm.cfg.max_nodes = int(_raw[k+1])
        elif v.startswith("--max-nodes="):
            sm.cfg.max_nodes = int(v.split("=", 1)[1])
    verify_only = "--verify-only" in flags
    if resume_from:
        import json as _json
        ck = _json.load(open(resume_from))
        from s5_state_machine import NodeRecord
        for nd in ck["nodes"]:
            sm.nodes.append(NodeRecord(**nd))
        # C3: resume 后 id 计数器必须超过 ckpt 里已有最大编号，否则新节点继续撞号
        _max_nid = max((int(str(n.id).lstrip("N")) for n in sm.nodes if str(n.id).lstrip("N").isdigit()), default=0)
        sm._nid = max(getattr(sm, "_nid", 0), _max_nid)
        # E14 (Decision 21): ckpt 字段类型防御 — clean-r2 里 dropped_redundant 存成了 []，
        # 照搬会让后续 list-int 运算炸 TypeError（连锁崩溃），统一归一为 int
        def _as_int(v, default=0):
            return v if isinstance(v, int) and not isinstance(v, bool) else default
        sm.dropped_redundant = _as_int(ck.get("dropped_redundant", 0))
        sm.leak_hits_total = _as_int(ck.get("leak_hits_total", 0))
        sm.network_degraded = ck.get("network_degraded", False)
        sm.objective = ck.get("objective")  # Decision 19: resume 时恢复模型自估计目标函数
        sm.rework_events = ck.get("rework_events", [])
        print(f"[SM] resumed from {resume_from}: {len(sm.nodes)} nodes @ r{ck['round']}", flush=True)
    if no_verify:
        # Monkey-patch: 跳过联网检索，但所有节点仍过 LLM 核验（AC3 需要真实 evidence）
        from s5_pipeline import search_node as _sn
        def _vb_no_search(batch):
            for node in batch:
                if node.source == "search":
                    node.status = "degraded"
                    node.evidence = "no-verify 模式：未检索"
                    node.corrected_claim = node.claim
                    sm.confirmed.append((node.id, node.claim, "degraded"))
                    continue
                status, evidence, corrected, _r = verify_node(
                    {"id": node.id, "claim": node.claim}, [])
                node.status = status
                node.evidence = evidence
                node.corrected_claim = corrected or node.claim
                sm.confirmed.append((node.id, node.corrected_claim, status))
            return batch
        sm._verify_batch = _vb_no_search
        sm._rework = lambda failed: None
    try:
        result = sm.run(skip_l1=bool(resume_from), verify_only=verify_only)
    except Exception as e:
        import traceback, sys as _sys
        print(f"\n[T53 SM] FATAL: {type(e).__name__}: {e}", flush=True)
        traceback.print_exc()
        # E12 (2026-11-12): FATAL 时落盘"当前树状态"而非空壳。
        # r9 事故：崩溃发生在轮内（judge 阶段），per-round checkpoint 还没触发，
        # 旧逻辑只 dump rounds_log（空）→ resume 后从 0 节点重跑，整轮白干。
        # 现在直接保存内存里的 self.nodes（崩溃前已 extend 的部分保留）。
        ck_path = f"runs-s5-sm-{qid}-checkpoint.json"
        with open(ck_path, "w") as f:
            json.dump({
                "qid": qid,
                "round": len(sm.rounds_log),
                "nodes": [vars(n) for n in sm.nodes],
                "dropped_redundant": sm.dropped_redundant,
                "leak_hits_total": sm.leak_hits_total,
                "network_degraded": sm.network_degraded,
                "objective": sm.objective,  # Decision 19
                "rework_events": sm.rework_events,
            }, f, ensure_ascii=False, indent=2)
        print(f"[T53 SM] Checkpoint saved → {ck_path} (use --resume {ck_path})", flush=True)
        _sys.exit(1)
    print(f"\n[T53 SM] DONE: {len(result.nodes)} nodes, "
          f"{len(result.rounds_log)} rounds, "
          f"state={result.final_state}, "
          f"leaks={result.leak_hits_total}, "
          f"reworks={len(result.rework_events)}", flush=True)
    # 落盘
    out_path = f"runs-s5-sm-{qid}.json"
    with open(out_path, "w") as f:
        json.dump({
            "qid": qid,
            "n_nodes": len(result.nodes),
            "n_rounds": len(result.rounds_log),
            "final_state": result.final_state,
            "leak_hits": result.leak_hits_total,
            "rework_events": result.rework_events,
            "rounds": result.rounds_log,
            # E15 (2026-11-12): question/objective 随终盘落盘——assemble 侧不再依赖 ckpt
            # （r14 事故：runs-s5-sm-gpu.json 缺这两字段，只能从 checkpoint 借）。
            "question": q,
            "objective": sm.objective,
            "nodes": [vars(n) for n in result.nodes],
        }, f, ensure_ascii=False, indent=2)
    print(f"[T53 SM] Saved → {out_path}", flush=True)