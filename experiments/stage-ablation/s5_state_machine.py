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
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from ablation_harness import call_llm
from s5_pipeline import (
    _extract_json, _perturb, decompose, gap_check,
    search_node, verify_node,
)

# AC7 可复现（2026-11-16）：SM_SEED 环境变量固定随机采样（默认 -1 = 不固定，向后兼容）。
# random 是单例模块，这里 seed 后 line 355 局部 `import random` 拿到的也是同一全局状态。
import os as _os
import random as _random
_SM_SEED = int(_os.environ.get("SM_SEED", "-1"))
if _SM_SEED >= 0:
    _random.seed(_SM_SEED)


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
    # ── E2 (2026-11-12): contribution 方差感知 ──
    contrib_samples: int = 1          # 每条 edge 采样次数（1 = 退化为现状单点估计）
    contrib_temperature: float = 0.0  # 采样温度（0.0 = 确定性，退化为现状）
    lambda_uncertainty: float = 1.0   # 不确定度系数：剪枝判据 = mean + λ·std < θ（λ越大越保守越难剪）
    stop_std_max: float = 0.06        # E4/P5: J_stop 方差上限（gain std > 此值 = 还在探索，不触发停止计数）。P5 CDF 回标 2026-11-12：8 样本（drb-1×3+drb-2×2+gpu×3，n_new=0 轮剔除）std_pop=0.056 → 取 1x σ；原 0.15 是拍脑袋值，比实测波动宽 2.7x，等于永不 reset


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


def classify_edge_var(parent_claim: str, child_claims: list[str],
                      cfg: "ObjectiveConfig") -> tuple[str, str, float, float, bool]:
    """E2 (2026-11-12): 方差感知版 classify_edge。
    同一 edge 采样 cfg.contrib_samples 次（temperature=cfg.contrib_temperature），
    返回 (edge_type, reason, contrib_mean, contrib_std, high_var_any)。

    - edge_type 取众数（temp>0 时可能漂移，众数最稳）
    - contribution 取 mean±std（分布信息）
    - high_var_any = 任一样本标 high_var → True（豁免剪枝）
    - cfg.contrib_samples=1 且 contrib_temperature=0.0 时退化为 classify_edge 行为（std=0）
    - 全部采样失败 → 保守默认 (cartesian, error, 1.0, 0.0, False)
    """
    from ablation_harness import call_llm
    if not child_claims:
        prompt = EDGE_PREDICT_PROMPT.format(concept=parent_claim)
    else:
        children_block = "\n".join(f"- {c}" for c in child_claims[:10])
        prompt = EDGE_TYPE_PROMPT.format(parent_claim=parent_claim, children_block=children_block)

    n = max(1, int(cfg.contrib_samples))
    temp = float(cfg.contrib_temperature)
    et_list, contribs, hvs = [], [], []
    first_reason = ""
    for i in range(n):
        try:
            out, _ = call_llm(prompt, max_tokens=300, temperature=temp, retries=2)
            m = re.search(r'"edge_type"\s*:\s*"(cartesian|quotient|stochastic)"', out or "", re.I)
            et_list.append(m.group(1).lower() if m else "cartesian")
            rm = re.search(r'"reason"\s*:\s*"([^"]*)"', out or "")
            r = rm.group(1) if rm else ""
            if i == 0 and r:
                first_reason = r
            cm = re.search(r'"contribution"\s*:\s*([0-9]*\.?[0-9]+)', out or "")
            contribs.append(min(max(float(cm.group(1)), 0.0), 1.0) if cm else 1.0)
            hv = re.search(r'"high_var"\s*:\s*(true|false)', out or "", re.I)
            hvs.append(hv.group(1).lower() == "true" if hv else False)
        except Exception as e:
            print(f"  [SM] edge-classify-var sample {i} error: {e}", flush=True)
            # 单样本失败不中断，计入保守默认
            et_list.append("cartesian")
            contribs.append(1.0)
            hvs.append(False)

    if not contribs:
        return "cartesian", "all-samples-failed", 1.0, 0.0, False
    mean_c = sum(contribs) / len(contribs)
    std_c = (sum((c - mean_c) ** 2 for c in contribs) / len(contribs)) ** 0.5
    # edge_type 众数
    from collections import Counter
    et_mode = Counter(et_list).most_common(1)[0][0]
    return et_mode, first_reason, mean_c, std_c, any(hvs)


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
    search_query: str = ""  # D32: 模型生成的英文检索词（P1H_INDEX 已要求输出；之前被丢弃，导致检索永远用中文 claim）
    retrieval_sources: list = field(default_factory=list)  # D32: 该节点实际拿到的来源 [{url,type,title}]——信息获取度量的原料


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
        self.challenge_log: list[dict] = []  # D-质询审计（2026-11-16）：各层反方质询记录
        self.rework_events = []
        self.contradiction_events: list[dict] = []  # D33: 全局矛盾扫描事件（喂回 decompose + 度量）
        self._gain_history: list[float] = []
        self.dropped_redundant = 0
        self.objective: Optional[dict] = None  # Decision 19: 模型自估计终点目标函数（L1 轮产出）
        self.objective_mode: str = "formula"  # #31 消融臂: formula=P1_L1_SKELETON(公式版) / text=P1_L1_TEXT(文字版)
        self.ckpt_round = 0  # 2026-11-16: resume 时记录 ckpt round（verify-only 批次号基准）
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
        from s5_pipeline import P1_L1_SKELETON, P1_L1_TEXT, P1_L1_MINIMAL, P1_L1_METHOD, P1_L1_METHOD_CHALLENGE, _extract_json
        if self.objective_mode == "text":
            prompt = P1_L1_TEXT.format(question=self.question)
        elif self.objective_mode == "minimal":
            prompt = P1_L1_MINIMAL.format(question=self.question)
        elif self.objective_mode == "method":
            prompt = P1_L1_METHOD.format(question=self.question)
        elif self.objective_mode == "method_challenge":
            prompt = P1_L1_METHOD_CHALLENGE.format(question=self.question)
        else:
            prompt = P1_L1_SKELETON.format(question=self.question)
        out, _ = call_llm(prompt, max_tokens=2048, temperature=0.7, top_p=0.95, retries=3)
        d = _extract_json(out or "") or {}
        # D-质询落盘（2026-11-16）：challenge 字段此前解析后直接丢弃，
        # 现在存到 self.challenge_log 并随 checkpoint 持久化——质询过程可审计。
        if isinstance(d.get("challenge"), dict):
            self.challenge_log.append({"layer": "L1", "question": self.question[:100], **d["challenge"]})
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

        # D35: 矛盾反馈注入——把上一轮检出的树内矛盾喂给 decompose 层，
        # 让模型看到"你之前拆的定义和已核验事实打架了"，定向修正而不是盲展开。
        # 这是旧流程"外部校验→内部修正"闭环的恢复：decompose 层第一次收到验证层信号。
        # （D35 修复：必须在 prompt 构造前算好；D34 崩溃根因是它被放在 call_llm 之后。）
        contradiction_block = ""
        if getattr(self, "contradiction_events", None):
            recent = self.contradiction_events[-10:]
            lines = "\n".join(
                f"- {c['a']}({c['a_claim'][:50]}) vs {c['b']}({c['b_claim'][:50]}): {c['desc'][:80]}"
                for c in recent)
            contradiction_block = (
                "\n【已检出的树内矛盾（来自上一轮全局扫描）】\n" + lines +
                "\n如果本轮要展开与上述矛盾相关的父节点，先判断哪个数值/定义更可信"
                "（看 evidence 的来源质量），在子节点 claim 里显式修正错误的一方，"
                "并在 evidence 栏注明「修正自矛盾检测」。不要回避矛盾、两边都保留。\n")


        prompt = self._safe_prompt(P1H_INDEX,
            question=self.question,
            confirmed_block=confirmed_block + (contradiction_block or ""),
            parents_block=parents_block + edge_block,
            start=len(self.nodes) + 1,
        )
        # 多父节点批次：要求模型给每个节点指定 parent 字段
        if len(parents) > 1:
            prompt += (
                f"\n\n【重要】本批次有 {len(parents)} 个父节点：{', '.join(p.id for p in parents)}。"
                f"每个子节点必须加 `parent` 字段指定它属于哪个父节点（值必须是上述 id 之一）。"
                f"不要把所有子节点都挂在同一个父节点下。"
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
        parent_id_set = {p.id for p in parents}
        new_recs = []
        for k, rn in enumerate(raw_nodes):
            # edge_type: LLM 可在节点里标（可选字段），否则继承父节点类型
            et = rn.get("edge_type", "")
            valid_et = et if et in ("cartesian", "quotient", "stochastic") else ""
            if not valid_et:
                # 继承：取第一个父节点的 edge_type
                valid_et = parents[0].edge_type if parents else "cartesian"
            # parent_ids: 优先用模型指定的 parent 字段，没指定才 fallback 到第一个父节点
            specified_parent = rn.get("parent", "")
            if specified_parent in parent_id_set:
                pids = [specified_parent]
            else:
                pids = [p.id for p in parents]  # fallback: 挂整批父节点
            self._nid += 1
            rec = NodeRecord(
                id=f"N{self._nid}",
                claim=rn["claim"],
                level=f"L{next_lv}",
                source=rn.get("source", "search"),
                parent_ids=pids,
                edge_type=valid_et,
                search_query=(rn.get("search_query") or "").strip(),  # D32: 不再丢弃模型生成的检索词
            )
            new_recs.append(rec)
        return new_recs

    def _verify_batch(self, batch: list[NodeRecord]) -> list[NodeRecord]:
        """核验一批节点。返回带 status/evidence 的节点。

        D-质询并行（2026-11-16）：verify_node 是纯 LLM 调用，短上下文批量并发
        实测提速明显（8787 qwen3.8-27b：6 并发总耗时 ≈ 最慢单个，而非累加）。
        search 节点的检索仍串行（ego-browser 有状态），LLM 核验部分并发。"""
        from concurrent.futures import ThreadPoolExecutor
        # 先串行做检索（search 节点），收集 (node, srcs_list)
        prepared = []
        for node in batch:
            if node.source == "search":
                if self.network_degraded:
                    srcs, err = [], "network_degraded: 出口探针失败，跳过联网检索"
                else:
                    srcs, err = search_node(
                        {"id": node.id, "claim": node.claim,
                         "search_query": node.search_query or node.claim}, qid=self.qid)
                if err:
                    node.status = "degraded"
                    node.evidence = f"检索失败: {err}"
                    node.corrected_claim = node.claim
                    self.confirmed.append((node.id, node.claim, "degraded"))
                    continue
                srcs_list = srcs if isinstance(srcs, list) else []
                node.retrieval_sources = [
                    {"url": s.get("url"), "type": s.get("source_type"),
                     "title": (s.get("title") or "")[:80]} for s in srcs_list]
            else:
                srcs_list, err = [], None
            prepared.append((node, srcs_list))
        # 并发 LLM 核验（含反方质询）
        def _do_verify(item):
            node, srcs_list = item
            return verify_node(
                {"id": node.id, "claim": node.claim,
                 "source": node.source}, srcs_list)
        if not prepared:
            return batch  # 整批在检索阶段已处理完（如检索失败→degraded），无 LLM 核验可做
        with ThreadPoolExecutor(max_workers=min(len(prepared), 4)) as ex:
            results = list(ex.map(_do_verify, prepared))
        for (node, _), (status, evidence, corrected, _r) in zip(prepared, results):
            node.status = status
            node.evidence = evidence
            node.corrected_claim = corrected or node.claim
            self.confirmed.append((node.id, node.corrected_claim, status))
        return batch

    def _verify_parent_nodes(self):
        """父节点级核验（2026-11-18 D提议）。

        一个父节点下所有子节点都 verify 完 + 正交/完备/冗余检查通过后，
        才标父节点 verified。

        检查项：
        1. 所有子节点 status == "verified"
        2. 正交性：子节点之间是否正交（不重复、不矛盾）
        3. 完备性：子节点是否覆盖父节点的 claim
        4. 冗余：子节点是否有可压缩成参数/变量的内容

        全部通过 → 父节点标 verified
        任一失败 → 父节点不标 verified（保持 pending），记录原因
        """
        from ablation_harness import call_llm as _cll
        import json as _json

        # 按父节点分组
        parent_children: dict[str, list[NodeRecord]] = {}
        for n in self.nodes:
            for pid in n.parent_ids:
                if pid not in parent_children:
                    parent_children[pid] = []
                parent_children[pid].append(n)

        # 对每个有子节点的父节点做核验
        for parent_id, children in parent_children.items():
            parent = next((n for n in self.nodes if n.id == parent_id), None)
            if parent is None:
                continue

            # 检查 1：所有子节点都 verified
            unverified_children = [c for c in children if c.status != "verified"]
            if unverified_children:
                # 子节点还没 verify 完，父节点保持 pending
                continue

            # 检查 2-4：正交性、完备性、冗余（LLM 判断）
            child_claims = [c.claim for c in children]
            prompt = f"""你是一个学术分解质量检查员。检查以下分解是否合格：

父节点：{parent.claim}

子节点（共 {len(children)} 个）：
""" + "\n".join(f"  - {c}" for c in child_claims) + """

请检查：
1. 正交性：子节点之间是否正交（不重复、不矛盾）？
2. 完备性：子节点是否覆盖了父节点的所有关键方面？
3. 冗余：子节点是否有可压缩成参数/变量的内容（即多个子节点其实是一个参数的不同取值）？

输出 JSON：
{{
  "orthogonal": true/false,
  "complete": true/false,
  "redundant": true/false,
  "reason": "简短说明",
  "suggestions": ["如果有问题，给出具体建议"]
}}"""
            try:
                resp, _usage = _cll(prompt, max_tokens=500, timeout=60)
                # 解析 JSON
                resp_clean = resp.strip()
                if resp_clean.startswith("```"):
                    resp_clean = resp_clean.split("```")[1]
                    if resp_clean.startswith("json"):
                        resp_clean = resp_clean[4:]
                    resp_clean = resp_clean.strip()
                check = _json.loads(resp_clean)

                if check.get("orthogonal") and check.get("complete") and not check.get("redundant"):
                    # 全部通过 → 父节点标 verified
                    parent.status = "verified"
                    parent.evidence = f"父节点级核验通过：正交+完备+无冗余（{check.get('reason', '')}）"
                    self.confirmed.append((parent.id, parent.claim, "verified"))
                    print(f"    [SM] parent {parent_id} verified: {len(children)} children, orthogonal+complete+no-redundant", flush=True)
                else:
                    # 任一失败 → 父节点保持 pending，记录原因
                    issues = []
                    if not check.get("orthogonal"):
                        issues.append("非正交")
                    if not check.get("complete"):
                        issues.append("不完备")
                    if check.get("redundant"):
                        issues.append("有冗余")
                    parent.status = "pending"
                    parent.evidence = f"父节点级核验未通过：{', '.join(issues)}（{check.get('reason', '')}）"
                    # 记录到 rework_events
                    self.rework_events.append({
                        "parent_id": parent_id,
                        "issues": issues,
                        "suggestions": check.get("suggestions", []),
                        "round": len(self.rounds_log),
                    })
                    print(f"    [SM] parent {parent_id} NOT verified: {', '.join(issues)}", flush=True)
            except Exception as e:
                # LLM 调用失败 → 父节点保持 pending
                parent.status = "pending"
                parent.evidence = f"父节点级核验失败（LLM 错误）：{e}"
                print(f"    [SM] parent {parent_id} verify failed: {e}", flush=True)

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

        D34 (2026-11-12): 旧实现是"加 alternative 后缀盲重搜一次"——没有判断失败原因、
        没有换检索词、没有利用矛盾证据，等于把同一个坏 query 再掷一次骰子。
        现在分两类处理：
          (a) 有矛盾证据的（contradiction_events 涉及该节点）→ 定向修正 rework：
              LLM 拿到双方 evidence + 来源，判哪边可信，产出 corrected claim + 新 search_query；
              用新 query 重搜 + 重验，成功则更新 claim/evidence 并标 fixed=True。
          (b) 无矛盾证据的普通 failed → 换角度重拆：LLM 给 2 个改写后的 search_query
              （不同角度/同义替换/英文化），逐个试，任一 verified 即收。
        度量：rework_fix_rate = 定向修正成功数 / 定向修正尝试数。
        """
        from ablation_harness import call_llm as _cll
        # 建矛盾索引：node_id -> [event, ...]
        contra_idx: dict[str, list[dict]] = {}
        for ev in getattr(self, "contradiction_events", []):
            if not ev.get("fixed"):
                for k in ("a", "b"):
                    contra_idx.setdefault(ev[k], []).append(ev)

        n_directed = n_directed_ok = 0
        for node in failed:
            if node.rework_count >= self.cfg.max_rework:
                node.status = "degraded"  # 放弃
                continue
            node.rework_count += 1
            events = contra_idx.get(node.id, [])
            mode = "directed" if events else "angle"
            self.rework_events.append({
                "node_id": node.id,
                "claim": node.claim[:60],
                "attempt": node.rework_count,
                "mode": mode,
                "reason": node.evidence[:80],
            })
            ok = False
            try:
                if events:
                    ok = self._rework_directed(node, events)
                    n_directed += 1
                    if ok:
                        n_directed_ok += 1
                else:
                    ok = self._rework_angle(node)
            except Exception as e:
                print(f"  [SM] rework {node.id} ({mode}) error: {e}", flush=True)
            if not ok and node.status != "verified":
                node.status = "degraded"
        if n_directed:
            rate = n_directed_ok / n_directed
            print(f"  [SM] rework directed: {n_directed_ok}/{n_directed} fixed (fix_rate={rate:.2f})", flush=True)

    def _rework_directed(self, node: "NodeRecord", events: list[dict]) -> bool:
        """D34: 定向矛盾修正——拿双方 evidence 让 LLM 裁决，产出修正 claim + 新检索词。"""
        from ablation_harness import call_llm as _cll
        by_id = {n.id: n for n in self.nodes}
        blocks = []
        for ev in events[:3]:
            other_id = ev["b"] if ev["a"] == node.id else ev["a"]
            other = by_id.get(other_id)
            if not other:
                continue
            a_node = by_id.get(ev["a"])
            blocks.append(
                f"节点A {ev['a']}: {ev['a_claim']}\n  evidence: {(a_node.evidence[:200] if a_node else '（缺失）')}\n"
                f"节点B {ev['b']}: {ev['b_claim']}\n  evidence: {other.evidence[:200]}\n"
                f"矛盾描述: {ev['desc']}"
            )
        prompt = (
            "一棵研究分解树里两个已核验节点互相矛盾。请裁决：基于双方 evidence 的来源质量"
            "（一手数据 > 转述 > 无来源），哪个节点的数值/定义更可信？\n\n"
            + "\n---\n".join(blocks) +
            f"\n\n当前需要修正的节点是 {node.id}: {node.claim}\n"
            '输出 JSON：{"keep": "A"或"B", "corrected_claim": "修正后本节点应表述的内容（带具体数值）", '
            '"search_query": "用于重新检索验证修正值的一句话检索词（英文优先，arXiv 友好）"}'
        )
        out, _ = _cll(prompt, max_tokens=1500, temperature=0.0, retries=2)
        d = _extract_json(out or "") or {}
        corrected = str(d.get("corrected_claim") or "").strip()
        new_q = str(d.get("search_query") or "").strip()
        if not corrected:
            return False
        # 用新 query 重搜 + 重验
        srcs, err = search_node({"id": node.id, "claim": corrected,
                                 "search_query": new_q or corrected}, qid=self.qid)
        if err:
            return False
        status, evidence, corr2, _r = verify_node(
            {"id": node.id, "claim": corrected}, srcs if isinstance(srcs, list) else [])
        if status == "verified":
            node.claim = corr2 or corrected
            node.search_query = new_q or node.search_query
            node.status = "verified"
            node.evidence = f"[rework-directed r{node.rework_count}] {evidence}"
            node.corrected_claim = corr2 or corrected
            for ev in events:
                ev["fixed"] = True
            print(f"  [SM] rework-directed {node.id}: FIXED → {node.claim[:60]}", flush=True)
            return True
        return False

    def _rework_angle(self, node: "NodeRecord") -> bool:
        """D34: 换角度重拆——LLM 给 2 个改写检索词（不同角度/英文化），逐个重试。"""
        from ablation_harness import call_llm as _cll
        prompt = (
            "一个事实节点核验失败（来源不支持或与来源冲突）。请给出 2 个【不同检索角度】的改写检索词，"
            "用于重新检索验证它。要求：① 至少一个用英文（arXiv 通道友好）；② 角度要不同"
            "（如：直接查数值 vs 查定义/公式 vs 查权威出处）；③ 每个 ≤15 词。\n"
            f"原节点: {node.claim}\n失败证据: {node.evidence[:150]}\n"
            '输出 JSON：{"queries": ["...", "..."]}'
        )
        out, _ = _cll(prompt, max_tokens=800, temperature=0.3, retries=2)
        d = _extract_json(out or "") or {}
        queries = [str(q).strip() for q in (d.get("queries") or []) if str(q).strip()]
        for q in queries[:2]:
            srcs, err = search_node({"id": node.id, "claim": node.claim,
                                     "search_query": q}, qid=self.qid)
            if err:
                continue
            status, evidence, corrected, _r = verify_node(
                {"id": node.id, "claim": node.claim}, srcs if isinstance(srcs, list) else [])
            if status == "verified":
                node.status = "verified"
                node.search_query = q
                node.evidence = f"[rework-angle r{node.rework_count}] {evidence}"
                node.corrected_claim = corrected or node.claim
                print(f"  [SM] rework-angle {node.id}: verified via '{q[:40]}'", flush=True)
                return True
        return False

    def _scan_contradictions(self, rnd: int):
        """D33: 全局矛盾扫描——对已 verified 节点批量问 LLM 有没有互相矛盾的数值。

        单节点 P3_VERIFY 只查"该节点 vs 自己的来源"；树内节点 A 和 B 的数值打架
        （如 H100 带宽两处差 10 倍）没有任何一步会抓。这里每轮一次、批处理，
        命中后：(a) 记入 contradiction_events 喂回下一轮 decompose（定向修正）；
        (b) 度量 contradiction_rate / fix_success_rate（信息获取提升度量的核心项）。
        只对 verified 节点扫（degraded 的 claim 本身不完整，扫了是噪声）。
        """
        from ablation_harness import call_llm as _cll
        ver = [n for n in self.nodes if n.status == "verified"]
        if len(ver) < 4:
            return
        # 控制成本：每轮最多扫最近 30 个 verified 节点
        sample = ver[-30:]
        block = "\n".join(f"{n.id}: {n.claim[:120]}" for n in sample)
        prompt = (
            "下面是一棵研究分解树里已核验的事实节点。请检查其中是否存在【互相矛盾】的数值或定义"
            "（同一物理量/参数在不同节点给出冲突的值，或两个节点的结论逻辑上不能同时成立）。\n"
            "注意：口径不同不算矛盾（如 prefill 吞吐 vs decode 吞吐）；同一量的单位换算等价也不算。\n"
            "只报真矛盾，没有就返回空列表。\n\n" + block +
            '\n输出 JSON：{"contradictions": [{"a": "Nxx", "b": "Nyy", "desc": "一句话说明哪里矛盾"}]}')
        try:
            out, _ = _cll(prompt, max_tokens=2000, temperature=0.0, retries=2)
        except Exception:
            return
        d = _extract_json(out or "") or {}
        items = d.get("contradictions") or []
        by_id = {n.id: n for n in sample}
        found = 0
        for it in items[:5]:
            a, b = it.get("a"), it.get("b")
            if a not in by_id or b not in by_id:
                continue
            found += 1
            self.contradiction_events.append({
                "round": rnd, "a": a, "b": b,
                "a_claim": by_id[a].claim[:80], "b_claim": by_id[b].claim[:80],
                "desc": str(it.get("desc", ""))[:120],
                "fixed": False,
            })
            print(f"  [SM] r{rnd} CONTRADICTION: {a} vs {b} — {str(it.get('desc',''))[:60]}", flush=True)
        if found:
            print(f"  [SM] r{rnd}: {found} contradiction(s) → fed back to next decompose round", flush=True)

    def _save_checkpoint(self, rnd: int):
        """每轮结束把当前树状态落盘。resume 时读回继续。

        树形目录结构（2026-11-18）：
        checkpoints/sm-{qid}-r{rnd}/
          meta.json              # 全局状态
          N1/                    # 根节点文件夹
            node.md              # 可读文档
            node.json            # 机器解析
            N2/                  # N1 的子节点
              node.md
              node.json
              N4/                # N2 的子节点
                node.md
                node.json
            N3/
              node.md
              node.json

        每个父节点文件夹 = 一个索引，打开就能看到所有子节点。
        原子写：meta.json 先写 tmp 再 os.replace。"""
        import os
        ckpt_dir = "checkpoints"
        base = os.path.join(ckpt_dir, f"sm-{self.qid}-r{rnd}")
        os.makedirs(base, exist_ok=True)

        # 写 meta.json（原子）
        meta = {
            "qid": self.qid,
            "question": self.question,
            "round": rnd,
            "state": self.state.value,
            "dropped_redundant": self.dropped_redundant,
            "leak_hits_total": self.leak_hits_total,
            "network_degraded": self.network_degraded,
            "objective": self.objective,
            "objective_mode": self.objective_mode,
            "challenge_log": self.challenge_log,
            "rework_events": self.rework_events,
            "contradiction_events": self.contradiction_events,
            "n_nodes": len(self.nodes),
        }
        meta_path = os.path.join(base, "meta.json")
        meta_tmp = meta_path + ".tmp"
        with open(meta_tmp, "w") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(meta_tmp, meta_path)

        # 构建树：node_id -> node, parent_id -> [child_ids]
        node_map = {n.id: n for n in self.nodes}
        children = {}  # parent_id -> [child_ids]
        roots = []
        for n in self.nodes:
            if not n.parent_ids:
                roots.append(n.id)
            for pid in n.parent_ids:
                if pid not in children:
                    children[pid] = []
                children[pid].append(n.id)

        # 层级编号：node_id -> "1", "1.1", "1.1.3"
        # 按 parent_ids 排序，保证兄弟节点顺序稳定
        def sort_key(nid):
            # N1 < N2 < ... < N10（数字排序，不是字典序）
            num = int(str(nid).lstrip("N"))
            return num

        level_ids = {}  # node_id -> "1.1.3"
        def assign_level_ids(node_id, prefix):
            level_ids[node_id] = prefix
            kids = sorted(children.get(node_id, []), key=sort_key)
            for i, kid in enumerate(kids, 1):
                assign_level_ids(kid, f"{prefix}.{i}" if prefix else str(i))

        for i, root_id in enumerate(sorted(roots, key=sort_key), 1):
            assign_level_ids(root_id, str(i))

        # 递归写树（用层级编号做目录名）
        def write_node_tree(node_id, current_dir):
            node = node_map[node_id]
            dir_name = level_ids[node_id]  # "1", "1.1", "1.1.3"
            node_dir = os.path.join(current_dir, dir_name)
            os.makedirs(node_dir, exist_ok=True)

            # 写 node.json
            node_json_path = os.path.join(node_dir, "node.json")
            node_json_tmp = node_json_path + ".tmp"
            with open(node_json_tmp, "w") as f:
                json.dump(vars(node), f, ensure_ascii=False, indent=2)
                f.flush()
                os.fsync(f.fileno())
            os.replace(node_json_tmp, node_json_path)

            # 写 node.md（可读）
            node_md_path = os.path.join(node_dir, "node.md")
            md_lines = [
                f"# {node.id}: {node.claim[:80]}",
                "",
                f"- **status**: {node.status}",
                f"- **level**: {node.level}",
                f"- **source**: {node.source}",
                f"- **edge_type**: {node.edge_type}",
                f"- **rework_count**: {node.rework_count}",
                f"- **parent_ids**: {', '.join(node.parent_ids) if node.parent_ids else '(root)'}",
                "",
                "## Claim",
                "",
                node.claim,
                "",
            ]
            if node.corrected_claim:
                md_lines += ["## Corrected Claim", "", node.corrected_claim, ""]
            if node.evidence:
                md_lines += ["## Evidence", "", node.evidence, ""]
            if node.search_query:
                md_lines += ["## Search Query", "", node.search_query, ""]
            if node.retrieval_sources:
                md_lines += ["## Retrieval Sources", ""]
                for src in node.retrieval_sources:
                    md_lines.append(f"- {src}")
                md_lines.append("")

            with open(node_md_path, "w") as f:
                f.write("\n".join(md_lines))
                f.flush()
                os.fsync(f.fileno())

            # 递归写子节点
            for child_id in children.get(node_id, []):
                write_node_tree(child_id, node_dir)

        # 从根节点开始写
        for root_id in roots:
            write_node_tree(root_id, base)

    def _load_checkpoint(self, path: str):
        """从树形目录结构加载 checkpoint。兼容旧单文件 JSON 和旧 nodes/ 格式。

        path 可以是：
        - 树形目录（新格式）：checkpoints/sm-soc-r3/（含 1/, 1.1/, 1.1.3/ 等子目录）
        - 旧 nodes/ 目录：checkpoints/sm-soc-r3/（含 nodes/ 子目录）
        - 单文件（旧格式）：checkpoints/sm-soc-r3.json
        返回 (meta_dict, nodes_list)
        """
        import os
        if os.path.isdir(path):
            meta = json.load(open(os.path.join(path, "meta.json")))

            # 检查是树形目录还是旧 nodes/ 格式
            nodes_subdir = os.path.join(path, "nodes")
            if os.path.isdir(nodes_subdir):
                # 旧 nodes/ 格式
                nodes = []
                for fn in sorted(os.listdir(nodes_subdir)):
                    if fn.endswith(".json") and not fn.endswith(".tmp"):
                        nodes.append(json.load(open(os.path.join(nodes_subdir, fn))))
                return meta, nodes
            else:
                # 新树形目录格式：递归读（目录名是 1, 1.1, 1.1.3 等）
                nodes = []
                def read_node_tree(current_dir):
                    for fn in sorted(os.listdir(current_dir)):
                        fn_path = os.path.join(current_dir, fn)
                        if os.path.isdir(fn_path) and fn[0].isdigit():
                            node_json = os.path.join(fn_path, "node.json")
                            if os.path.exists(node_json):
                                nodes.append(json.load(open(node_json)))
                            # 递归读子节点
                            read_node_tree(fn_path)
                read_node_tree(path)
                return meta, nodes
        else:
            # 旧格式：单文件
            d = json.load(open(path))
            return d, d.get("nodes", [])

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
                '(async () => { const t = await taskSpace("sm-probe"); '
                'const p = t.page("x"); '
                'console.log(JSON.stringify({alive: !!p})); })();', timeout=20)
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
            # --verify-only: 树结构已完整，跳过 decompose 直接核验所有 pending + degraded 节点
            n_pending = sum(1 for n in self.nodes if n.status == 'pending')
            n_degraded = sum(1 for n in self.nodes if n.status == 'degraded')
            print(f"  [SM] verify-only mode: {n_pending} pending + {n_degraded} degraded nodes to verify", flush=True)
            self.state = State.VERIFY
            to_verify = [n for n in self.nodes if n.status in ('pending', 'degraded')]
            # 重置 degraded 节点为 pending，让 _verify_batch 重新核验
            for n in to_verify:
                if n.status == 'degraded':
                    n.status = 'pending'
            # 2026-11-16 落盘修复：verify-only 每批落盘一次，且文件名带批次号
            # （sm-{qid}-r{base}-{k}.json）。旧逻辑用 len(self.rounds_log) 当 rnd，
            # verify-only 下 rounds_log 永远为空 → 每批都覆写同一个 sm-{qid}-r0.json，
            # 而 resume 读的是 sm-{qid}-r1.json（启动时的 ckpt）→ 进度全丢，
            # 下次 resume 又从头验一遍（1h 白跑，见 runs-s5-sm-soc-verifyonly.log）。
            # 批次号从 ckpt round 递增，resume 时取 checkpoints/ 里最大的 r{base}-{k} 续跑。
            base_rnd = self.ckpt_round  # resume 时 = ckpt 的 round；无 resume = 0
            n_batches = (len(to_verify) + 2) // 3  # 每批 3 节点
            for i in range(0, len(to_verify), 3):
                batch = to_verify[i:i+3]
                self._verify_batch(batch)
                k = i // 3 + 1
                if k % 10 == 0:
                    self._scan_contradictions(rnd=base_rnd + k)  # D33: verify-only 也扫矛盾
                self._save_checkpoint(rnd=base_rnd + k)
                print(f"  [SM] verified {i+len(batch)}/{len(to_verify)} "
                      f"(batch {k}/{n_batches}) → ckpt r{base_rnd + k}", flush=True)
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
            use_var = self.cfg.contrib_samples > 1  # E2: 多采样启用方差感知
            for p in l1_frontier:
                if use_var:
                    et, reason, contrib_mean, contrib_std, high_var = classify_edge_var(p.claim, [], self.cfg)
                    # E2 剪枝判据：mean + λ·std < θ → 即使最乐观估计也不够 → 才剪
                    # （方差大 = LLM 不确定 = 保守保留，防误剪）
                    optimistic = contrib_mean + self.cfg.lambda_uncertainty * contrib_std
                    prune_signal = optimistic
                    contrib_display = f"{contrib_mean:.2f}±{contrib_std:.2f}"
                else:
                    et, reason, contrib, high_var = classify_edge(p.claim, [], self.cfg)
                    optimistic = contrib
                    prune_signal = contrib
                    contrib_display = f"{contrib:.2f}"
                if et != "cartesian":
                    print(f"  [SM] edge-classify {p.id}: {et} ({reason[:50]})", flush=True)
                    p.edge_type = et
                # idea #45 + E2: 贡献阈值过滤（极小概率极大不稳定期望豁免；E2 用不确定度感知判据）
                if prune_signal < self.cfg.contribution_threshold and not high_var:
                    print(f"  [SM] contribution-filter {p.id}: {contrib_display} < {self.cfg.contribution_threshold} — skip expansion", flush=True)
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

            # ── Q2: 正交性判据（2026-11-18）──
            # 同一父节点下的子节点两两 n-gram 重叠 > 0.5 的对，调 LLM 判"B 能否从 A 推出"。
            # 能推出 → 丢弃 B（redundant）。防 Goodhart：拆出来的如果是同义变体，S_α 不涨。
            n_orthogonal_dropped = 0
            if new_nodes:
                # 按 parent 分组
                by_parent: dict[str, list[NodeRecord]] = {}
                for nn in new_nodes:
                    for pid in (nn.parent_ids or []):
                        by_parent.setdefault(pid, []).append(nn)
                ortho_drop_ids: set[str] = set()
                for pid, siblings in by_parent.items():
                    if len(siblings) < 2:
                        continue
                    # 找重叠对
                    pairs = []
                    for i in range(len(siblings)):
                        for j in range(i + 1, len(siblings)):
                            ov = _ngram_overlap(siblings[i].claim, siblings[j].claim)
                            if ov > 0.5:
                                pairs.append((i, j, ov))
                    if not pairs:
                        continue
                    # 批量 LLM 判推
                    pair_block = "\n".join(
                        f"[{k}] A={siblings[pi].claim[:100]} B={siblings[pj].claim[:100]}"
                        for k, (pi, pj, _ov) in enumerate(pairs))
                    ortho_prompt = (
                        "你是严格审稿人。对下面每对研究子节点，判断 B 能否从 A 推出"
                        "（即 B 的信息是否已包含在 A 中，或 B 只是 A 的换措辞/特例）。"
                        "能推出 → B 是冗余的。\n\n"
                        f"{pair_block}\n\n"
                        f"对每对输出一行，共 {len(pairs)} 行，紧凑格式：\"pair\":0,\"redundant\":true\n"
                        "只输出这些行。"
                    )
                    try:
                        mtok = min(200 * len(pairs) + 200, 4096)
                        out, _ = call_llm(ortho_prompt, max_tokens=mtok, temperature=0.0, retries=2)
                        for k, (pi, pj, _ov) in enumerate(pairs):
                            # 解析每行
                            line_pat = rf'"pair"\s*:\s*{k}\s*,\s*"redundant"\s*:\s*(true|false)'
                            m = re.search(line_pat, out or "")
                            if m and m.group(1) == "true":
                                # B 冗余 → 丢弃 B（j 侧）
                                ortho_drop_ids.add(siblings[pj].id)
                                n_orthogonal_dropped += 1
                    except Exception as e:
                        print(f"  [SM] Q2 orthogonality LLM error: {e}", flush=True)
                if ortho_drop_ids:
                    new_nodes = [nn for nn in new_nodes if nn.id not in ortho_drop_ids]
                    print(f"  [SM] Q2 orthogonality: dropped {n_orthogonal_dropped} redundant nodes", flush=True)

            # ── Q4: 可压缩复杂度判据（2026-11-18）──
            # 对每个父节点，算 marginal_gain(子节点 claims, [父节点 claim])。
            # gain < 0.3 → 子节点集合相对父节点几乎没有新信息 → 膨胀，丢弃所有子节点。
            n_compression_dropped = 0
            if new_nodes:
                by_parent2: dict[str, list[NodeRecord]] = {}
                for nn in new_nodes:
                    for pid in (nn.parent_ids or []):
                        by_parent2.setdefault(pid, []).append(nn)
                comp_drop_ids: set[str] = set()
                for pid, siblings in by_parent2.items():
                    if not siblings:
                        continue
                    parent_claim = next((n.claim for n in self.nodes if n.id == pid), "")
                    if not parent_claim:
                        continue
                    gain = marginal_gain([s.claim for s in siblings], [parent_claim])
                    if gain < 0.3:
                        for s in siblings:
                            comp_drop_ids.add(s.id)
                        n_compression_dropped += len(siblings)
                        print(f"  [SM] Q4 compression: parent {pid} gain={gain:.3f} < 0.3 — dropped {len(siblings)} kids (inflation)", flush=True)
                if comp_drop_ids:
                    new_nodes = [nn for nn in new_nodes if nn.id not in comp_drop_ids]

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
                # E4/P3: gain 方差感知 — 近窗 gain std > stop_std_max 说明还在探索期，不触发停止计数
                _win = self._gain_history[-5:]
                _gstd = (sum((g - sum(_win)/len(_win))**2 for g in _win)/len(_win)) ** 0.5 if len(_win) >= 2 else 0.0
                if _gstd <= self.cfg.stop_std_max:
                    low_gain_streak += 1
                else:
                    low_gain_streak = 0
                    print(f"    [SM] high-gain-std ({_gstd:.3f} > {self.cfg.stop_std_max}): streak reset", flush=True)
            elif not deduped:
                low_gain_streak += 1
            else:
                low_gain_streak = 0
            self._no_ness_streak = low_gain_streak

            # ── VERIFY ──
            self.state = State.VERIFY
            if deduped:
                self._verify_batch(deduped)

            # ── 父节点级核验（2026-11-18 D提议）──
            # 一个父节点下所有子节点都 verify 完 + 正交/完备/冗余检查通过后，
            # 才标父节点 verified。这样 AI 对核验进度和需要核验什么很清晰。
            self._verify_parent_nodes()

            # ── J_verify → REWORK? ──
            unverified = [n for n in deduped if n.status != "verified"]
            if unverified and self._should_rework(deduped):
                self.state = State.REWORK
                self._rework(unverified)

            # ── D33: 全局矛盾扫描（每轮一次，批处理省 LLM 调用）──
            # 旧流程"内部/外部校验有没有逻辑矛盾"的恢复：单节点 P3_VERIFY 只查自己 vs 来源，
            # 树内节点互相打架（N22 带宽 3.35TB/s vs N89 通信量差 1000 倍这类）没人抓。
            # 度量：contradiction_rate + fix_success_rate（定向修复后转 verified 比例）。
            self._scan_contradictions(rnd)

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
                "contradictions_found": sum(1 for c in self.contradiction_events if c.get("round") == rnd),
                "n_orthogonal_dropped": n_orthogonal_dropped,
                "n_compression_dropped": n_compression_dropped,
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

# ─────────────────────────────────────────────
# P4 synthesis + judge（2026-11-16，phase1-fix-pipeline "修复 P4 synthesis gap"）
# ─────────────────────────────────────────────
# 背景：SM 管线跑完只有节点树（final_state='verified'），没有 answer 综合步骤，
# 产不出 judge.coverage——gate "soc cov ≥ 0.898" 的 0.898 是 S0 的 judge.coverage
# （runs-s5-prod S5-soc 100 reps mean=0.8957），两个指标不同没法比。
# 一次性诊断（synth_diag_soc.py，soc 1.0 / nat 0.667 两 gate 均过）验证了
# 节点树信息量足够；本函数把同样的逻辑正式修进管线（复用 s5_pipeline 的
# 分段综合与 _perturb，judge 用 s8b_pilot.judge，depth 对照用 judge_v2_depth）。
# 用法：CLI 加 --synth；不加则行为与旧版完全一致（向后兼容）。

def synthesize_answer(question: str, nodes: list, qid: str) -> dict:
    """节点树 → 分段综合 → merge → judge + depth。返回 {answer, judge, coverage, depth}。"""
    from collections import defaultdict
    from s5_pipeline import _perturb
    by_lv = defaultdict(list)
    for n in nodes:
        by_lv[n.level].append(n)
    parts = []
    for lv in sorted(by_lv, key=lambda x: str(x).lstrip("L")):
        seg = "\n".join(
            f"{n.id} ({lv}): {n.corrected_claim or n.claim}  "
            f"[status={n.status}; evidence: {(n.evidence or '')[:80]}]"
            for n in by_lv[lv])
        # 2026-11-16 fix: 截断时保头不保尾——公式/数值集中在前段，
        # 尾部多为检索来源列表和重复性节点。旧逻辑 seg[:6000] 保头，
        # 但 L4 有 97 节点 24K chars，截断后丢失的恰是后半段的
        # roofline/故障损耗/利用率等关键公式节点。改为保头+保尾。
        if len(seg) > 12000:
            head = seg[:8000]
            tail = seg[-4000:]
            seg = head + "\n[...中间省略...]\n" + tail
        p = (f"你是研究员。基于下面第 {lv} 层的已核验事实，回答原问题中该层涉及的部分。"
             f"只写结论+数值/公式，每条标来源条目 id，不要重复其他层的内容。"
             f"【关键】上面列出的每一个公式（如 TCO 公式、roofline 公式、KV Cache 计算、"
             f"故障损耗项、利用率分解等），必须在你的回答中完整保留并代入具体数值，"
             f"不得省略或仅定性提及。如果某条事实给出了完整公式，你的回答必须展示该公式。"
             f"如果不同事实之间存在矛盾（如不同 head_dim 取值），取多数一致的值并注明分歧。\n\n"
             f"【问题】\n{question}\n\n【第 {lv} 层事实】\n{seg}") + _perturb()
        t0 = time.time()
        out_l, _ = call_llm(p, max_tokens=4000, temperature=0.7, top_p=0.95, retries=3)
        parts.append(f"=== 第 {lv} 层 ===\n{out_l or '(空)'}")
        print(f"  [SM] synth {lv}: {len(by_lv[lv])} 节点, out={len(out_l or '')}c, {time.time()-t0:.0f}s", flush=True)
    merge_p = (f"你是研究员。下面是同一道问题按目录树分层得到的各层结论摘要。"
               f"请把它们合并成一份完整最终答案：覆盖问题全部子问，保留所有具体数值/公式/排序，"
               f"消除层间重复，最后给一个明确的推荐结论。"
               f"规则：问题问「最多/上限/提升多少/打几折」时，必须显式列出限制因素并给出其定量影响"
               f"（如频率表老化、热度漂移、容量覆盖不足），不能只讲优势不讲上限；"
               f"比较策略时，每个策略都要给出适用限制；涉及更新/失效/折扣的，给出推导公式和代入过程。"
               f"【关键】上面各层摘要中出现的每一个公式、数值、参数（如 TCO 公式、roofline 公式、"
               f"KV Cache 计算、故障损耗项、利用率分解、临界阈值等），必须在最终答案中显式保留并代入具体数值，"
               f"不得省略或仅定性提及。如果某层给出了完整公式，最终答案必须展示该公式及其代入过程。"
               f"如果各层之间存在矛盾（如不同 head_dim 取值），取多数一致的值并注明分歧。\n\n【问题】\n{question}\n\n"
               + "\n\n".join(parts)) + _perturb()
    t0 = time.time()
    answer, _ = call_llm(merge_p, max_tokens=8000, temperature=0.7, top_p=0.95, retries=3)
    print(f"  [SM] synth merge: out={len(answer or '')}c, {time.time()-t0:.0f}s", flush=True)
    # judge（gate 指标：GOLD 要点逐条 0/1 → coverage）
    from s8b_pilot import judge
    t0 = time.time()
    j = judge(qid, answer)
    cov = round(j.get("coverage") or 0, 3)
    print(f"  [SM] judge coverage = {cov} {time.time()-t0:.0f}s", flush=True)
    # depth 对照（gpu gate 用 depth ≥ 0.50）
    depth = None
    try:
        from judge_v2_depth import score_run
        dv = score_run(qid, answer)
        depth = dv.get("overall")
        print(f"  [SM] depth_score = {depth}", flush=True)
    except Exception as e:
        print(f"  [SM] depth score failed: {e}", flush=True)
    return {"answer": answer, "judge": j, "coverage": cov, "depth": depth}


if __name__ == "__main__":
    import os
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
        # qid 可能是自定义标识（如 gpu-method），QUESTIONS 里没有——回退到 gpu 取题
        # E17 (2026-11-15): 回退时打印警告——nat-mc-v3-resume 事故：qid 不在 QUESTIONS
        # 里静默回退到 gpu 题，resume 的 81 个 nat 节点跑在 gpu 题上，整轮作废。
        if qid not in QUESTIONS:
            print(f"[SM] WARNING: qid={qid!r} not in QUESTIONS, falling back to {list(QUESTIONS.keys())} — "
                  f"check if you meant --qid=nat/soc/gpu", flush=True)
        q = QUESTIONS.get(qid, QUESTIONS["gpu"])
    no_verify = "--no-verify" in flags
    resume_from = resume_from_early
    if resume_from is None and "--resume" in flags:
        i = flags.index("--resume")
        if i + 1 < len(flags):
            resume_from = flags[i+1]
    print(f"[T53 SM] Running on '{qid}': {q[:60]}...", flush=True)
    # T53 night-autonomy (2026-11-12): cwd 感知——DRB pilot 从 repo root 启动，
    # ckpt/final json 落 stage-ablation/（与 gpu run 同目录），不再依赖进程 cwd。
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    sm = DecompStateMachine(q, qid=qid)
    # --max-nodes N: 覆盖硬顶（resume 时 ckpt 节点数可能已超默认 150）
    for k, v in enumerate(_raw):
        if v == "--max-nodes" and k + 1 < len(_raw):
            sm.cfg.max_nodes = int(_raw[k+1])
        elif v.startswith("--max-nodes="):
            sm.cfg.max_nodes = int(v.split("=", 1)[1])
    # --beta N: 覆盖冗余惩罚系数（消融臂：β=0 = 纯 S_α 无冗余惩罚，复现 v13 时代行为）
    for k, v in enumerate(_raw):
        if v == "--beta" and k + 1 < len(_raw):
            sm.cfg.redundancy_penalty_beta = float(_raw[k+1])
        elif v.startswith("--beta="):
            sm.cfg.redundancy_penalty_beta = float(v.split("=", 1)[1])
    verify_only = "--verify-only" in flags
    obj_mode_flag = next((f.split("=", 1)[1] for f in flags if f.startswith("--obj-mode=")), "formula")
    sm.objective_mode = obj_mode_flag  # #31 消融臂: formula(默认) / text
    if resume_from:
        import json as _json
        # 兼容新文件夹格式和旧单文件格式
        meta, ck_nodes = sm._load_checkpoint(resume_from)
        from s5_state_machine import NodeRecord
        for nd in ck_nodes:
            sm.nodes.append(NodeRecord(**nd))
        # C3: resume 后 id 计数器必须超过 ckpt 里已有最大编号，否则新节点继续撞号
        _max_nid = max((int(str(n.id).lstrip("N")) for n in sm.nodes if str(n.id).lstrip("N").isdigit()), default=0)
        sm._nid = max(getattr(sm, "_nid", 0), _max_nid)
        # E14 (Decision 21): ckpt 字段类型防御 — clean-r2 里 dropped_redundant 存成了 []，
        # 照搬会让后续 list-int 运算炸 TypeError（连锁崩溃），统一归一为 int
        def _as_int(v, default=0):
            return v if isinstance(v, int) and not isinstance(v, bool) else default
        sm.dropped_redundant = _as_int(meta.get("dropped_redundant", 0))
        sm.leak_hits_total = _as_int(meta.get("leak_hits_total", 0))
        sm.network_degraded = meta.get("network_degraded", False)
        sm.objective = meta.get("objective")
        sm.objective_mode = meta.get("objective_mode", "formula")
        sm.challenge_log = meta.get("challenge_log", [])
        sm.rework_events = meta.get("rework_events", [])
        sm.contradiction_events = meta.get("contradiction_events", [])
        # 2026-11-16 verify-only 落盘修复：resume 时记录 ckpt round + 探测已有 verify-only
        # 批次 ckpt（sm-{qid}-r{round+k}.json，round = base + 批号），取最大 k 作为续跑起点。
        import glob as _glob
        _base = int(meta.get("round", 0) or 0)
        # 2026-11-19 fix: resume 后无条件设 ckpt_round = _base。
        # 旧逻辑只在 _max_k > 0 分支里设，导致 resume r3 后 ckpt_round 仍为 0，
        # verify-only 批次号从 1 起算 → 落盘 sm-gpu-r1/ r2/ 覆盖旧树形目录。
        sm.ckpt_round = _base
        _max_k = 0
        # 兼容新旧格式：旧格式 glob *.json，新格式 glob 目录
        for _p in _glob.glob(f"checkpoints/sm-{qid}-r*"):
            if os.path.isdir(_p):
                _m = re.search(r"r(\d+)$", _p)
            else:
                _m = re.search(r"r(\d+)\.json$", _p)
            if _m:
                _k = int(_m.group(1)) - _base
                if _k > 0:
                    _max_k = max(_max_k, _k)
        if _max_k > 0:
            _ckpt_path = f"checkpoints/sm-{qid}-r{_base + _max_k}"
            _meta2, _resumed_nodes = sm._load_checkpoint(_ckpt_path)
            _old = {n.id: n for n in sm.nodes}
            for nd in _resumed_nodes:
                if nd["id"] in _old:
                    _old[nd["id"]].__dict__.update(nd)
            sm.ckpt_round = _base + _max_k
            print(f"[SM] verify-only resume: 续跑自批次 ckpt r{_base + _max_k} "
                  f"({_ckpt_path})", flush=True)
        # E16 (2026-11-13): FATAL 落盘的 ckpt 缺 state 字段（text arm seed 就是这种）。
        # 无需恢复 sm.state——run() 开头无条件 self.state = State.DECOMPOSE，skip_l1=True
        # 跳过 L1 后主循环从 frontier 继续核验/重拆。这里只校验 ckpt 合法性。
        if meta.get("state") not in (None, "rework", "done", "decompose", "verify"):
            print(f"[SM] WARNING: unexpected state in ckpt: {meta.get('state')!r}", flush=True)
        print(f"[SM] resumed from {resume_from}: {len(sm.nodes)} nodes @ r{meta['round']}", flush=True)
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
                "objective_mode": getattr(sm, "objective_mode", "formula"),  # #31 消融臂
                "contradiction_events": getattr(sm, "contradiction_events", []),
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
    # --synth (2026-11-16, phase1-fix-pipeline "修复 P4 synthesis gap"):
    # 节点树跑完后补 P4 综合 + judge，产出 judge.coverage（gate 指标）。
    # 不加 flag 行为不变（向后兼容）。输出 runs-s5-sm-{qid}-synth.json，
    # 与一次性诊断 synth_diag_soc.py 同格式，bench 对比不用改。
    if "--synth" in flags:
        print(f"\n[T53 SM] --synth: P4 synthesis + judge ...", flush=True)
        try:
            s = synthesize_answer(q, result.nodes, qid)
            synth_path = f"runs-s5-sm-{qid}-synth.json"
            with open(synth_path, "w") as f:
                json.dump({
                    "qid": qid,
                    "n_nodes": len(result.nodes),
                    "final_state": result.final_state,
                    "answer": s["answer"],
                    "judge": s["judge"],
                    "coverage": s["coverage"],
                    "depth_score": s["depth"],
                    "source_run": out_path,
                }, f, ensure_ascii=False, indent=2)
            print(f"[T53 SM] Synth saved → {synth_path} | coverage={s['coverage']} depth={s['depth']}", flush=True)
        except Exception as e:
            import traceback
            print(f"[T53 SM] SYNTH FAILED: {type(e).__name__}: {e}", flush=True)
            traceback.print_exc()