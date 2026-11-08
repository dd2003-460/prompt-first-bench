#!/usr/bin/env python3
"""T54 S8B: 掩码条件重建 (masked-condition reconstruction) vs 角色质询 (persona interrogation).

来源: T-PR-13 判决 Q3a — persona 零效应 (2311.10054, 162 角色×4 模型族×2410 题),
唯一能把自校验符号翻正的 prompt 改动 = 把需要元认知的自评换成只需前向计算的预测
(2405.14092: "遮住一个关键条件让它重建")。本实验在本地 qwen3.8-27b 上复现这个对比。

臂设计 (单 pass, 无外部检索, 纯 prompt 杠杆):
  A0  baseline     : 直接回答 (裸基线)
  A1  persona      : 资深审计专家 persona + 要求逐条质疑自己的结论 (S8A 同款失败机制)
  A2  mask-rebuild : 生成后, 对每个关键结论遮住其依赖的一个前提/数字, 让模型从其余
                     信息重建被遮项, 重建成功→保留, 失败→降级为定性或标 [待核验]
题目:
  Q-nat  (自然域, 单节点): 物理/工程定量推理 — 缓存替换策略的命中率下界估算
  Q-soc  (社会域, 二级层): 平台经济学 — 二手平台定价行为推断 (人存原理→逐利+利益相关核验)

可证伪预测:
  P1: A2 > A0 (掩码重建净正) — 若成立, 支持"预测型自校验"杠杆
  P2: A1 ≈ A0 (persona 零效应) — 若成立, 与 2311.10054 / S8A 一致
  P3: 社会域上 A2-A0 差值 ≥ 自然域 — 二级结论层给重建提供结构化锚点, 若成立则
      "社会域必须带二级层"获得行为层证据; 若反了, 说明二级层是负担不是资产

判分: 每题人工 gold 要点清单 (见文件底部 GOLD), LLM-judge 按要点覆盖打分 0/1,
另记 [待核验] 数量作为幻觉代理指标。judge 用同族 27b (仅相对有效, 标注)。

Usage:
    python s8b_pilot.py --arms A0,A1,A2 --qs nat,soc --reps 3
    python s8b_pilot.py --dry-run --arms A0 --qs nat
"""
import argparse, json, os, re, sys, time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ablation_harness import call_llm, LLM_MODEL

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(HERE, "runs-s8b")

# ── 题目 ──────────────────────────────────────────────────────────────
QUESTIONS = {
    "nat": (
        "某边缘 CDN 节点有 128GB 内存做对象缓存，工作负载：10 万对象，大小服从 Pareto(α=1.1)，"
        "请求热度也服从 Pareto(β=0.9)，热门对象与大小负相关（ρ≈-0.3）。每天总请求 5000 万次。"
        "请估算：(a) LRU 策略下的稳态字节命中率下界；(b) LFU 相比 LRU 最多能提升多少百分点、"
        "为什么；(c) 如果对象更新率是 1%/天，LRU 的有效命中率还要再打几折？"
        "给出推导链，区分「凭记忆的」和「刚查到的」。"
    ),
    "soc": (
        "某二手交易平台观察到的现象：卖家挂价普遍比同类商品近期成交价高 15-25%，但成交周期反而变短了；"
        "同时平台数据显示，主动降价的卖家中 60% 在降价后 48 小时内没有收到新咨询。"
        "请用二级结论框架分析：(a) 这两个看似矛盾的现象能否用同一套假设解释？写出你的假设链"
        "（从生物演化的定向压力+随机偏好噪声出发，到逐利行为和利益相关方核验）；"
        "(b) 哪个利益相关方（买家/卖家/平台）最可能驱动了这个均衡，依据是什么；"
        "(c) 如果平台想打破这个均衡，最小干预是什么，会伤害谁？"
        "对每个关键断言标注置信度。"
    ),
    "gpu": (
        "你要在一台工作站上本地推理 Qwen3-27B 模型（BF16 权重约 54GB），要求单流延迟 < 3s/token、"
        "上下文窗口 ≥ 32K tokens。候选卡：RTX 5090、RTX 4090、L40S、A100-40GB。"
        "给出性价比最优的完整选卡方案。"
        "要求：思考必须最完整，确认没有遗漏任何影响决策的维度；"
        "每个关键数字标注来源（刚查到的 vs 凭记忆的），不确定的标 [待核验]；"
        "最终推荐必须是条件性的，不能给无条件排名。"
    ),
}

GOLD = {
    "nat": [
        "Pareto 热度下 LRU 命中率可用 Zipf/Pareto 累积质量估算（头部 k% 对象承载大部分请求）",
        "α=1.1 接近临界 → 缓存容量利用率对头部集中度敏感，128GB 能覆盖的头部比例决定命中率量级",
        "LFU 优势上限受对象更新/热度漂移限制（1%/天更新 → LFU 频率表老化），提升有限且需量化",
        "大小-热度负相关意味着按字节命中率 ≠ 按请求命中率，口径要分开报",
        "更新率 1%/天 → 有效驻留时间 ~100 天量级 vs 访问间隔，折扣幅度应给出推导而非拍脑袋",
        "明确标注哪些数字是估算、哪些是假设（如 miss 惩罚、对象不可分割性）",
    ],
    "soc": [
        "假设链起点：生存压力（金钱资源=定向）+ 偏好噪声（随机演化残留），不能跳级",
        "挂价高+成交快 的解释候选：信号理论（高挂价筛选诚意买家/降低还价空间感知）、锚定、或买家比价成本",
        "降价无咨询 的解释候选：降价触发负面信号（急卖=有问题?）、咨询行为滞后于价格变化、或买家等待更低锚点",
        "两个现象同一假设的解释力评估（哪条假设链能同时覆盖两者，哪条只能覆盖一个）",
        "利益相关方判定要有依据（数据里谁的行为变了、谁的收益结构变了），不能只点名",
        "最小干预方案 + 明确说清受害者（如伤害长尾卖家 or 伤害买家预期管理）",
        "每个关键断言带置信度，低置信的显式标出",
    ],
    "gpu": [
        # ── 硬件规格层（gold-tree N-5.1/N-3.2）──
        "四卡 VRAM 门槛：5090=32GB / 4090=24GB / L40S=48GB / A100-40=40GB，BF16 54GB 全部装不下",
        "Roofline decode 公式 tokens/s ≈ BW/bytes_per_token，且给出具体数值（5090≈33, A100≈29, L40S≈16 tok/s 量级）",
        "INT8 后权重 ~27GB：5090(32GB) 可装、4090(24GB) 仍紧张、L40S/A100 可装；INT8 roofline 重算（5090≈66 tok/s 上限）",
        # ── 吞吐分解层（gold-tree N-3.1/N-3.2/N-5.3）──
        "Prefill 是算力瓶颈（FLOPs/TFLOPS/MFU），decode 是带宽瓶颈——两个阶段约束不同，不能混为一谈",
        "KV cache 精确估算（~27B GQA: 32层×8 KV头×128维×2(K+V)×2字节×32K ctx ≈ 4GB）或至少指出 KV 对显存余量的影响",
        "缓存命中率/前缀复用对实际吞吐的影响（重复 prompt 场景下 decode 可跳过部分 prefill）",
        # ── 成本结构层（gold-tree N-1/N-1.1/N-1.2/N-1.3）──
        "TCO 完整公式：c_hour = (卡价 + 主机 − 残值)/H + 功耗×电价×u + 故障损耗/H，不能只报卡价",
        "电费独立计算（TDP 350W/250W × 电价 × 占空比），不是笼统'用电费'一笔带过",
        "故障损耗作为独立项（三年故障概率 × 卡价 / H），不是被 TCO 公式吞掉",
        # ── 利用率与调度层（gold-tree N-2/N-4/N-5.2）──
        "有效利用率 u = 占空比 × 调度效率的分解，而非单一数字",
        "并发流数 S 的双闸分析：速度闸 S ≤ t_max·BW/(bytes/tok) vs 显存闸 S ≤ VRAM/KV_bytes，取 min",
        # ── 经济决策层（gold-tree N-7）──
        "市场价格波动敏感性：GDDR7/HBM 供应紧张导致同型号价差 2-3x（如 RTX PRO 6000 $4,599→$16,000），选卡对采购时点敏感",
        "云租 vs 自建分水岭 = 利用率阈值（低占空比时 $0.22–0.50/h 云租低于自建 TCO），给出定量或半定量判断",
        # ── 元认知层（gold-tree SHARED 参数交互 + 来源标注）──
        "SHARED 参数交互效应：量化同时改变成本↓（权重变小→更便宜）和通过率↑（精度损失→质量下降），两个方向要分开讨论",
        "每个关键数字标注来源（刚查到的 vs 凭记忆的），不确定的标 [待核验]；最终推荐必须是条件性的（在什么利用率/电价/采购时点下哪张卡最优），不能给无条件排名",
    ],
}

# ── 臂 prompt ─────────────────────────────────────────────────────────
def build_prompt(arm: str, qid: str) -> str:
    q = QUESTIONS[qid]
    head = f"问题：{q}\n\n"
    if arm == "A0":
        return ("你是严谨的研究员。直接回答问题，给出完整推导链。\n"
                "要求：先给结论，再给因果链，不跳步；每个关键事实注明「刚查到的」（附来源）"
                "还是「凭记忆的」（标 [待核验]）；查不到就承认查不到，不要编数字。\n\n" + head)
    if arm == "A1":
        return ("你是一位以严苛著称的资深审计专家，职业习惯是对任何结论先假设它是错的。"
                "回答问题时执行以下流程：\n"
                "1. 先给出你的初步答案和推导链。\n"
                "2. 然后切换成审计专家身份，逐条质疑你自己的每个关键结论："
                "哪个前提没验证？哪个数字口径混了？哪个变量被忽略了？"
                "每个质疑给出依据，并判断是否推翻原结论。\n"
                "3. 最后修订：质疑成立的改，不成立的说明理由保留。\n"
                "输出中保留质询过程，最终答案单独一节。\n"
                "每个关键事实注明「刚查到的」（附来源）还是「凭记忆的」（标 [待核验]）。\n\n" + head)
    if arm == "A2":
        return ("你是严谨的研究员。回答问题，执行以下两阶段流程：\n"
                "【阶段一 — 生成】给出完整推导链和结论，列出你答案中所有关键前提/关键数字"
                "（编号 P1, P2, ...），每个标注它支撑哪个结论。\n"
                "【阶段二 — 掩码重建】对每个关键前提 Pi：暂时把它当作未知，"
                "只用答案中的其余信息（其他前提、观测事实、问题条件）尝试重建 Pi 的值或内容。"
                "- 重建结果与 Pi 一致或在合理误差内 → 标记 ✓，保留。\n"
                "- 重建失败或出现多个不一致候选 → 该前提降级：改为定性表述，"
                "或标注 [待核验]，并说明是哪个信息缺失导致无法重建。\n"
                "这一步不需要额外知识，只做前向推理：其余信息能不能推出被遮住的那一项。\n"
                "【输出】修订后的最终答案 + 一张重建结果表（Pi / 重建值 / 判定 ✓或[待核验] / 影响哪个结论）。\n"
                "每个关键事实注明「刚查到的」（附来源）还是「凭记忆的」（标 [待核验]）；查不到就承认，不要编。\n\n" + head)
    raise ValueError(f"unknown arm {arm}")


def judge(qid: str, answer: str) -> dict:
    """LLM-judge: 按 gold 要点逐项 0/1 + 计 [待核验] 数。同族 27b, 仅相对有效。"""
    points = "\n".join(f"{i+1}. {p}" for i, p in enumerate(GOLD[qid]))
    jp = (
        "你是评分员。下面是一道题的标准答案要点清单和一个候选回答。"
        "逐条判断候选回答是否实质覆盖了该要点（覆盖=1，未覆盖或答错=0；部分覆盖按 0 计并在 reason 说明）。\n\n"
        f"要点清单：\n{points}\n\n"
        f"候选回答：\n{answer[:12000]}\n\n"
        "输出 JSON：{\"scores\": [每要点 0/1], \"reasons\": [每条一句话], "
        "\"unverified_count\": 回答中 [待核验] 标记出现的次数, \"hallucination_flags\": [疑似编造的具体数字/事实, 没有就给空列表]}"
    )
    content, _ = call_llm(jp, max_tokens=2000, temperature=0)
    m = re.search(r"\{.*\}", content, re.S)
    try:
        d = json.loads(m.group(0)) if m else {}
    except json.JSONDecodeError:
        d = {"parse_error": content[:500]}
    scores = d.get("scores") or []
    n_pts = len(GOLD[qid])
    covered = sum(1 for s in scores[:n_pts] if s == 1)
    d["coverage"] = covered / n_pts if n_pts else None
    return d


def run_one(arm: str, qid: str, rep: int, dry_run: bool = False) -> dict:
    tag = f"{arm}-{qid}-r{rep}"
    prompt = build_prompt(arm, qid)
    rec = {
        "tag": tag, "arm": arm, "qid": qid, "rep": rep,
        "model": LLM_MODEL, "ts": datetime.now(timezone.utc).isoformat(),
    }
    if dry_run:
        rec["prompt_chars"] = len(prompt)
        print(f"[dry] {tag}: prompt {len(prompt)} chars")
        return rec
    t0 = time.time()
    try:
        answer, usage = call_llm(prompt, max_tokens=4096, temperature=0)
    except Exception as e:
        rec["error"] = str(e)
        print(f"[ERR] {tag}: {e}", file=sys.stderr)
        return rec
    rec.update(answer=answer, usage=usage, wall_s=round(time.time() - t0, 1))
    j = judge(qid, answer)
    rec["judge"] = j
    print(f"[ok] {tag}: coverage={j.get('coverage')} unverified={j.get('unverified_count')} "
          f"hallu_flags={len(j.get('hallucination_flags', []))} wall={rec['wall_s']}s")
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arms", default="A0,A1,A2")
    ap.add_argument("--qs", default="nat,soc")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    arms = args.arms.split(",")
    qs = args.qs.split(",")
    os.makedirs(RUNS_DIR, exist_ok=True)
    results = []
    for qid in qs:
        for arm in arms:
            for rep in range(1, args.reps + 1):
                r = run_one(arm, qid, rep, args.dry_run)
                results.append(r)
                with open(os.path.join(RUNS_DIR, f"{r['tag']}.json"), "w") as f:
                    json.dump(r, f, ensure_ascii=False, indent=1)
    # 汇总
    agg = {}
    for r in results:
        key = f"{r['arm']}/{r['qid']}"
        a = agg.setdefault(key, {"n": 0, "cov": [], "unv": [], "hallu": []})
        if "judge" not in r:
            continue
        a["n"] += 1
        a["cov"].append(r["judge"].get("coverage"))
        a["unv"].append(r["judge"].get("unverified_count") or 0)
        a["hallu"].append(len(r["judge"].get("hallucination_flags") or []))
    print("\n=== S8B summary ===")
    for key in sorted(agg):
        a = agg[key]
        covs = [c for c in a["cov"] if c is not None]
        mean_cov = sum(covs) / len(covs) if covs else float("nan")
        print(f"{key:10s} n={a['n']} coverage={mean_cov:.3f} "
              f"unverified_mean={sum(a['unv'])/max(len(a['unv']),1):.1f} "
              f"hallu_mean={sum(a['hallu'])/max(len(a['hallu']),1):.2f}")
    with open(os.path.join(RUNS_DIR, "summary.json"), "w") as f:
        json.dump({"ts": datetime.now(timezone.utc).isoformat(), "agg": agg}, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    import random as _rnd
    _rnd.seed()  # 确保反缓存扰动每次不同 (Python 默认已按时间播种, 此处显式化)
    main()