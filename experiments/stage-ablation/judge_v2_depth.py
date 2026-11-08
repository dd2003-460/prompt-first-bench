"""Judge v2: depth-gradient rubric scoring for nat domain.

Each gold point is decomposed into 3-4 depth levels. Judge scores each level 0/1,
weighted sum gives continuous [0,1] per point, mean across points = run score.

This replaces the binary coverage metric (denominator=6 → only 7 discrete values)
with a continuous resolution that distinguishes "mentioned the concept" from
"derived the correct quantitative relationship".

Weighting scheme — k·log(k) frequency-rarity weighting (成璐 2026-11-08):
  - Depth levels are ordered by rarity: shallow = common (high base rate), deep = rare (low base rate).
  - The value of reaching a level scales with how RARE it is (frequency × information content).
  - Pure log(k) would under-weight deep levels; multiplying by k compensates:
      w_k = k · ln(k+1) / Σ_j j·ln(j+1)   for k in {1..K}
    K=3 → weights ≈ [0.29, 0.40, 0.31]... wait no:
    k·ln(k+1): 1·ln2=0.693, 2·ln3=2.197, 3·ln4=4.159 → normalize: [0.11, 0.35, 0.54]
    K=4: 0.693, 2.197, 4.159, 6.438 → [0.08, 0.24, 0.45, 0.69]... no:
    sum=13.49 → [0.051, 0.163, 0.308, 0.477]
  - So deeper levels get disproportionately more weight. A run that reaches level 4
    but not level 1 gets 0.477 (not 0.25 as uniform would give).
  - This is the production formula from bench/self-opt-tester/bench.md O3:
      w_v = 1 + min(−log₂ p̃_v, log₂(1/ε))
    where p̃ = blind-generation base rate. For our fixed depth ladder, we use the
    deterministic k·ln(k+1) proxy instead of LLM-estimated p̃ (cheaper, no same-family
    judge bias, monotonic by construction).

Usage: python3 judge_v2_depth.py --runs runs-prod --arm S0 --q nat --reps 1-30
"""
import argparse, json, math, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ablation_harness import call_llm

# Depth-level rubric for nat (CDN cache) gold points
# Each point: list of (weight, description) — weights are k·ln(k+1) normalized (deeper = rarer = more valuable)
# K=3: [0.11, 0.35, 0.54]   K=4: [0.05, 0.16, 0.31, 0.48]

def _w3():
    raw = [k * math.log(k + 1) for k in range(1, 4)]
    s = sum(raw)
    return [r / s for r in raw]  # ≈ [0.11, 0.35, 0.54]

def _w4():
    raw = [k * math.log(k + 1) for k in range(1, 5)]
    s = sum(raw)
    return [r / s for r in raw]  # ≈ [0.05, 0.16, 0.31, 0.48]

W3 = _w3()
W4 = _w4()

NAT_RUBRIC = {
    "pt1": [
        (W3[0], "提到用 Pareto/Zipf 累积质量估算命中率（头部 k% 对象承载大部分请求）"),
        (W3[1], "给出具体公式或推导步骤（如 H(k) = 1 - (1-k)^{1-α} 或等价表述）"),
        (W3[2], "代入题面参数（α=1.1, N=10⁵, C=128GB）算出数值区间"),
    ],
    "pt2": [
        (W3[0], "指出 α=1.1 接近临界值 1，分布重尾，容量利用率对头部集中度敏感"),
        (W3[1], "说明 128GB 能覆盖的头部比例决定命中率量级（定性）"),
        (W3[2], "给出覆盖比例的估算（如 top 10-20% 对象占 >80% 字节流量）"),
    ],
    "pt3": [
        (W3[0], "提到 LFU 优势受对象更新/热度漂移限制"),
        (W3[1], "将 1%/天 更新率与 LFU 频率表老化关联（定性）"),
        (W3[2], "量化提升上限（给出百分点范围 + 推导依据，非拍脑袋）"),
    ],
    "pt4": [
        (W3[0], "区分按字节命中率 vs 按请求命中率（两个口径分开报）"),
        (W3[1], "解释为什么大小-热度负相关导致两口径不同"),
        (W3[2], "分别给出两个口径的数值或关系式"),
    ],
    "pt5": [
        (W4[0], "提到'驻留时间'/'residence time'/'停留时间'概念"),
        (W4[1], "给出 T_res 的量级估计（天/小时级，非分钟级；如 ~100 天或 ~30 天）"),
        (W4[2], "将 T_res 与访问间隔做了显式对比（T_res >> inter-visit gap）"),
        (W4[3], "推导出折扣因子并给出数值（如 p_stale = 1-exp(-u·T_res)，代入得具体折数）"),
    ],
    "pt6": [
        (W3[0], "明确标注哪些数字是估算、哪些是假设"),
        (W3[1], "列出关键假设（如 miss 惩罚、对象不可分割性、稳态假设）"),
        (W3[2], "对至少一个假设说明如果改变会怎样（敏感性）"),
    ],
}

SOC_RUBRIC = {
    "pt1": [
        (W4[0], "假设链起点包含'生存压力/金钱资源=定向压力'"),
        (W4[1], "假设链起点包含'偏好噪声/随机演化残留'"),
        (W4[2], "没有直接跳到禀赋效应/损失厌恶等现成心理学标签"),
        (W4[3], "从起点到逐利行为有中间推导步骤（非一步到位）"),
    ],
    "pt2": [
        (W4[0], "给出至少一个解释候选（信号理论/锚定/比价成本等）"),
        (W4[1], "解释候选有机制说明（为什么高挂价→快成交）"),
        (W4[2], "评估了该解释的适用边界或局限"),
        (W4[3], "考虑了多个候选之间的竞争关系"),
    ],
    "pt3": [
        (W4[0], "给出至少一个解释候选（负面信号/咨询滞后/等待更低锚点等）"),
        (W4[1], "解释候选有机制说明（为什么降价→无咨询）"),
        (W4[2], "评估了该解释的适用边界或局限"),
        (W4[3], "考虑了多个候选之间的竞争关系"),
    ],
    "pt4": [
        (W3[0], "明确指出哪条假设链能同时覆盖两个现象"),
        (W3[1], "明确指出哪条只能覆盖一个"),
        (W3[2], "对'同一假设 vs 不同假设'给出判断依据"),
    ],
    "pt5": [
        (W3[0], "判定最可能驱动均衡的利益相关方（点名）"),
        (W3[1], "给出依据（数据里谁的行为变了/谁的收益结构变了）"),
        (W3[2], "排除了其他利益相关方的理由"),
    ],
    "pt6": [
        (W3[0], "提出具体最小干预方案"),
        (W3[1], "明确说清受害者是谁"),
        (W3[2], "说明为什么是'最小'的（而非更激进的替代）"),
    ],
    "pt7": [
        (W3[0], "每个关键断言带置信度标注"),
        (W3[1], "低置信的显式标出（不是全部高置信）"),
        (W3[2], "置信度标注有依据（为什么这个给 0.6 那个给 0.9）"),
    ],
}


def _w5():
    raw = [k * math.log(k + 1) for k in range(1, 6)]
    s = sum(raw)
    return [r / s for r in raw]  # ≈ [0.04, 0.12, 0.22, 0.33, 0.49]

W5 = _w5()

GPU_RUBRIC = {
    # ═══ N-0 顶层公式 ═══
    "N-0": [  # c_pass = c_hour / (u × λ_raw × G_pass)
        (W3[0], "提到选卡的最终目标是最小化'每个通过任务的成本'（而非单纯卡价或吞吐）"),
        (W3[1], "给出 c_pass = c_hour / (u × λ_raw × G_pass) 或等价分解（成本/利用率/速率/通过率）"),
        (W3[2], "说明四个因子中哪个是决策敏感项（如 u 的 BOUND 8x 意味着占空比假设差一倍结论就翻）"),
    ],
    # ═══ N-1 每小时持有成本 ═══
    "N-1": [  # c_hour = 摊销 + 电费 + 故障
        (W3[0], "提到持有成本包含多个组成部分（不只是卡价）"),
        (W3[1], "c_hour = 购置摊销 + 电费 + 故障损耗，三项都列出"),
        (W3[2], "给出各项占比量级（如电费~50%、摊销~43%、故障~8%），说明电费通常是最大项"),
    ],
    # ═══ N-1.1 购置摊销 ═══
    "N-1.1": [  # = (卡价 + 主机价 − 卡价×残值率) / H
        (W3[0], "提到卡需要摊销到使用年限（不是一次性成本）"),
        (W3[1], "摊销公式：(卡价 + 主机价 − 残值) / H，或等价表述"),
        (W3[2], "代入具体数字算出至少一张卡的 $/h 摊销（如 5090: ($1999+$500−$600)/3y ≈ $0.57/h）"),
    ],
    # ═══ N-1.1.1 卡价 ═══
    "N-1.1.1": [  # gpu_price, B4, 2.2x, SHARED→N-1.3.2
        (W3[0], "给出至少一张候选卡的具体价格（$）"),
        (W3[1], "四张卡价格都给出，且标注来源（MSRP vs 实际市场价）"),
        (W3[2], "指出卡价是 SHARED 参数——同时影响摊销和故障损耗，真实弹性比单看摊销高 ~17%"),
    ],
    # ═══ N-1.1.2 主机价 ═══
    "N-1.1.2": [  # host_price, S-a
        (W3[0], "提到除了卡本身还有主机/配套成本（机箱/电源/CPU/内存）"),
        (W3[1], "给出主机价的量级（如 $500-$2000，取决于是否需要 ECC/多卡槽）"),
        (W3[2], "说明主机价在不同方案间的差异对 TCO 排名的影响（通常 < 卡价的 20%，不改变排名）"),
    ],
    # ═══ N-1.1.3 残值率 ═══
    "N-1.1.3": [  # resid, B8, leaf S-b
        (W3[0], "提到 GPU 有残值/贬值概念（用几年后还能卖钱）"),
        (W3[1], "给出残值率区间或假设值（如 0.15-0.45，H=3年时）"),
        (W3[2], "明确声明残值率是黑盒参数（B8），不同假设下 TCO 变化量级（如 0.15 vs 0.45 差 ~$X/h）"),
    ],
    # ═══ N-1.1.4 摊销小时数 ═══
    "N-1.1.4": [  # H, B8, 2.02x, leaf S-b
        (W3[0], "提到摊销年限 H 影响每小时成本"),
        (W3[1], "给出 H 的合理范围（如 2-5 年）并说明选择依据"),
        (W3[2], "敏感性分析：H 从 2→5 年，$/h 怎么变（线性反比），是否改变排名"),
    ],
    # ═══ N-1.2 电费 ═══
    "N-1.2": [  # = 整机功耗 × 电价
        (W3[0], "提到 GPU 运行有电费成本"),
        (W3[1], "电费 = 整机功耗(kW) × 电价($/kWh)，两项分开"),
        (W3[2], "算出每张卡的 $/h 电费（如 5090: 0.35kW×$0.15=$0.053/h；A100: 0.4kW×$0.15=$0.06/h）"),
    ],
    # ═══ N-1.2.1 整机功耗 ═══
    "N-1.2.1": [  # power_kw, S-a
        (W3[0], "提到至少一张卡的 TDP/功耗（W）"),
        (W3[1], "区分 GPU TDP 和整机功耗（含 CPU/风扇/其他，通常 GPU+100-200W）"),
        (W3[2], "四张卡功耗对比，指出功耗差异对长期电费的影响（5090 350W vs A100 400W，3年差 ~$XX）"),
    ],
    # ═══ N-1.2.2 电价 ═══
    "N-1.2.2": [  # elec, B5, 1.88x, leaf S-b
        (W3[0], "提到电价影响电费成本"),
        (W3[1], "给出电价假设（如 $0.10-0.30/kWh，因地区而异）"),
        (W3[2], "电价敏感性：$0.10 vs $0.30 下 TCO 排名是否翻转（高电价地区低 TDP 卡优势更大）"),
    ],
    # ═══ N-1.3 故障损耗 ═══
    "N-1.3": [  # = 三年故障概率 × 卡价 / H, ★F-C
        (W3[0], "提到 GPU 有故障风险（不是永久可用）"),
        (W3[1], "故障损耗 = 故障概率 × 卡价 / H，作为独立成本项（不是被摊销吞掉）"),
        (W3[2], "给出故障概率量级（如消费卡 3 年 ~5-15%，数据中心卡 ~2-5%），计算 $/h 影响"),
    ],
    # ═══ N-1.3.1 三年故障概率 ═══
    "N-1.3.1": [  # p_fail, B8, leaf S-b
        (W3[0], "提到不同类别 GPU 故障率不同（消费卡 vs 数据中心卡）"),
        (W3[1], "给出具体概率区间或来源（如 TechPowerUp/厂商 MTBF 数据）"),
        (W3[2], "指出这是黑盒参数（B8），不同假设下故障损耗项变化量级"),
    ],
    # ═══ N-2 有效利用率 ═══
    "N-2": [  # u = 占空比 × 调度效率, ★F-B
        (W3[0], "提到实际利用率低于 100%（不是 24/7 满载）"),
        (W3[1], "u = 业务需求占空比 × 调度效率，两个因子分开"),
        (W3[2], "u 的 BOUND 8x（全题瓶颈#1）：占空比假设从 0.3→0.6，TCO 排名是否翻转"),
    ],
    # ═══ N-2.1 业务需求占空比 ═══
    "N-2.1": [  # duty_demand, B6, 8.00x, ■瓶颈#1
        (W3[0], "提到'你实际用 GPU 的时间比例'（占空比）"),
        (W3[1], "给出占空比的合理范围（如 0.1-0.8，取决于使用场景）"),
        (W3[2], "识别为全题最敏感参数（BOUND 8x）：不同占空比下最优卡可能完全不同"),
    ],
    # ═══ N-2.2 调度效率 ═══
    "N-2.2": [  # sched_eff, B6, leaf S-b
        (W3[0], "提到即使 GPU 在跑，调度/排队也有损失"),
        (W3[1], "调度效率的量级（如 0.7-0.95，取决于 serving 框架）"),
        (W3[2], "调度效率与占空比的交互：高占空比时调度损失被摊薄，低占空比时更显著"),
    ],
    # ═══ N-3 原始产出速率 ═══
    "N-3": [  # λ_raw = 3600/t_task; t_task = t_prefill + t_decode/n
        (W3[0], "提到吞吐量取决于 prefill 和 decode 两个阶段"),
        (W3[1], "λ_raw = 3600 / (t_prefill + t_decode/n)，n 是并发流数"),
        (W3[2], "定量：prefill 占 ~40%、decode 占 ~60%（或类似比例），说明哪段是主要瓶颈"),
    ],
    # ═══ N-3.1 prefill 时间 ═══
    "N-3.1": [  # = FLOPs/(卡数×TFLOPS×MFU×tp_eff), ★F-A
        (W3[0], "提到 prefill 是算力受限（compute-bound），不是带宽受限"),
        (W3[1], "prefill 时间 = prefill_FLOPs / (峰值TFLOPS × MFU)，或等价表述"),
        (W3[2], "定量：27B 模型 prefill 一次 ~594 TFLOP，5090 (~210 TFLOPS BF16) 理论 ~2.8s（MFU=1）"),
    ],
    # ═══ N-3.1.1 prefill 计算量 ═══
    "N-3.1.1": [  # prefill_flops, S-a, 594 TFLOP
        (W3[0], "提到 prefill 的计算量取决于模型大小和序列长度"),
        (W3[1], "给出 27B 模型的 prefill FLOPs 量级（~600 TFLOP 级别）"),
        (W3[2], "说明 FLOPs 如何随 context 长度变化（线性），32K vs 4K 差 8x"),
    ],
    # ═══ N-3.1.2 峰值算力 ═══
    "N-3.1.2": [  # tf_peak, S-a
        (W3[0], "提到不同卡的峰值算力（TFLOPS）不同"),
        (W3[1], "给出至少两张卡的 BF16 TFLOPS（如 5090 ~210, A100 ~312）"),
        (W3[2], "算力差异对 prefill 时间的影响（A100 prefill 比 5090 快 ~1.5x）"),
    ],
    # ═══ N-3.1.3 MFU ═══
    "N-3.1.3": [  # mfu, B2, 1.20x, leaf S-b
        (W3[0], "提到实际算力达不到峰值（MFU < 1）"),
        (W3[1], "MFU 的典型范围（如 0.3-0.6，取决于 batch size 和 kernel 效率）"),
        (W3[2], "MFU 是黑盒（B2）但 BOUND 只有 1.2x——即使 MFU 假设错一倍，prefill 时间也只变 20%"),
    ],
    # ═══ N-3.2 decode 时间 ═══
    "N-3.2": [  # = tok×(W+n×KV)/(卡数×BW×η_bw×tp_eff), ★F-A
        (W3[0], "提到 decode 是带宽受限（memory-bandwidth-bound）"),
        (W3[1], "decode 时间 ∝ (权重字节 + n×KV字节) / 有效带宽"),
        (W3[2], "定量：5090 BF16 decode ~33 tok/s（1792/54），INT8 ~66 tok/s（1792/27）"),
    ],
    # ═══ N-3.2.1 权重字节 ═══
    "N-3.2.1": [  # w_bytes, S-a, 14/27/54 GB
        (W3[0], "提到模型权重大小取决于精度（W4/W8/BF16）"),
        (W3[1], "27B 模型：W4≈14GB, W8≈27GB, BF16≈54GB"),
        (W3[2], "量化选择直接决定哪些卡能装下（W4 全部可装, BF16 全部不可装）"),
    ],
    # ═══ N-3.2.2 每流 KV 字节 ═══
    "N-3.2.2": [  # kv_per_stream, B7, 2.0x, ★2倍分歧
        (W3[0], "提到 KV cache 会占用额外显存"),
        (W3[1], "KV cache 估算：27B GQA, 32层×8头×128维×2(K+V)×2字节×32K ≈ 4GB/流"),
        (W3[2], "KV 是 2 倍分歧源（B7）：不同 GQA 配置下 KV 差 2x，直接影响最大并发流数"),
    ],
    # ═══ N-3.2.3 峰值带宽 ═══
    "N-3.2.3": [  # bw_peak, S-a
        (W3[0], "提到不同卡的内存带宽（GB/s）不同"),
        (W3[1], "四张卡带宽：5090≈1792, 4090≈1008, L40S≈864, A100≈1555 GB/s"),
        (W3[2], "带宽差异直接决定 decode 速度排名（5090 > A100 > 4090 > L40S）"),
    ],
    # ═══ N-3.2.4 有效带宽系数 ═══
    "N-3.2.4": [  # eta_bw, B3, 1.43x, leaf S-b
        (W3[0], "提到实际带宽达不到峰值（η_bw < 1）"),
        (W3[1], "η_bw 典型范围（如 0.6-0.85，取决于访问模式和 kernel 优化）"),
        (W3[2], "η_bw 是黑盒（B3）但 BOUND 1.43x——假设误差对 decode 速度影响有限（< 43%）"),
    ],
    # ═══ N-4 任务通过率 ═══
    "N-4": [  # G_pass, nuisance, B1, 1.57x, ■瓶颈#2
        (W3[0], "提到不是所有输出都合格（有质量/通过率问题）"),
        (W3[1], "G_pass 受量化精度影响（W4 比 W8 通过率低），给出量级（如 ΔG ~0.05-0.10）"),
        (W3[2], "G_pass 是全题瓶颈#2（BOUND 1.57x）：量化导致的通过率下降可能抵消成本节省"),
    ],
    # ═══ N-5 可行域 ═══
    "N-5": [  # feasible_set, constraint
        (W3[0], "提到有些配置根本不可行（不是所有卡都能跑）"),
        (W3[1], "可行性由显存容量和带宽下限共同决定"),
        (W3[2], "列出哪些候选被排除及原因（如 L40S 单卡 BW 不够 W16 准入）"),
    ],
    # ═══ N-5.1 显存容量门槛 ═══
    "N-5.1": [  # n×KV + W ≤ 可用显存 → n_cap, leaf S-a
        (W3[0], "提到显存要同时装下权重和 KV cache"),
        (W3[1], "n_cap = (VRAM − W_bytes) / KV_per_stream，算出每张卡的最大并发流数"),
        (W3[2], "具体数值：5090 W8: (32−27)/4≈1流, W4: (32−14)/4≈4流, A100 W8: (40−27)/4≈3流"),
    ],
    # ═══ N-5.2 带宽准入下限 ═══
    "N-5.2": [  # W4 774 / W8 1034 / W16 1574 GB/s, leaf S-a
        (W3[0], "提到最低带宽要求（低于某值则延迟不达标）"),
        (W3[1], "给出准入下限：W4≥774, W8≥1034, W16≥1574 GB/s（对应 <3s/token 约束）"),
        (W3[2], "按此划掉不合格候选（如 L40S 864 < 1034 → W8 不可行；4090 1008 < 1034 → W8 边缘）"),
    ],
    # ═══ N-5.3 缓存命中率 ═══
    "N-5.3": [  # cache_hit_rate, nuisance, B8, 7.6x, leaf S-b
        (W3[0], "提到前缀缓存/复用可以减少重复 prefill"),
        (W3[1], "命中率 h 时有效 prefill 成本降为 (1-h)×原始值"),
        (W3[2], "命中率是黑盒（B8）且 BOUND 7.6x——高命中场景下 prefill 成本几乎消失，改变成本结构"),
    ],
    # ═══ N-6 精度选择与质量损失（新题目：精度不限，须论证）═══
    "N-6": [
        (W3[0], "提到不同精度档位（BF16/FP8/INT8/NVFP4/W4）对权重大小和推理速度的影响"),
        (W3[1], "给出至少两种精度的 27B 模型权重大小（如 BF16≈54GB, INT8≈27GB, W4≈14GB, NVFP4≈7-10GB）"),
        (W3[2], "论证所选精度的质量损失是否可接受（引用 benchmark 或给出量化指标如 perplexity 增量）"),
    ],
    # ═══ N-6.1 NVFP4 架构独占性 ═══
    "N-6.1": [
        (W3[0], "提到 NVFP4（4-bit Float）是 NVIDIA Blackwell 架构专属特性，非所有 GPU 都支持"),
        (W3[1], "指出哪些候选卡支持 FP4（仅 RTX 5090/Blackwell），哪些不支持（4090/L40S/A100/H100）"),
        (W3[2], "说明 FP4 支持带来的实际收益：权重减半 vs INT8 + 专用硬件加速，decode 速度提升量级"),
    ],
    # ═══ N-6.2 精度-质量 tradeoff 量化 ═══
    "N-6.2": [
        (W3[0], "提到低精度（W4/FP4）可能导致输出质量下降，不能只看速度"),
        (W3[1], "给出质量损失的量化依据（如 MMLU/HELMET 分数下降、perplexity 增量、或具体任务通过率变化）"),
        (W3[2], "说明在什么任务类型下低精度可接受（简单分类/摘要）vs 不可接受（复杂推理/代码生成）"),
    ],
    # ═══ N-7 候选集搜索完整性（完全开放：模型自主界定范围）═══
    "N-7": [
        (W3[0], "候选集由模型自主界定，且显式论证了纳入/排除标准（不是默默省略，而是说清'为什么考虑这个、为什么不考虑那个'）"),
        (W3[1], "每个候选给出关键规格（显存/带宽/TDP/价格/架构），且标注来源；覆盖多个不同架构/代际/容量档位"),
        (W3[2], "包含至少一个非典型或跨品类方案（如 CPU+大内存跑 W4、统一内存 Mac、或已停产但性价比突出的旧卡），而非只列当前在售 GPU"),
    ],
    # ═══ N-8 多卡方案 TCO 对比（完全开放：单卡 vs 多卡）═══
    "N-8": [
        (W3[0], "评估了至少一个多卡方案（如 2× 消费卡 vs 1× 数据卡，或 4× 旧卡 vs 1× 新卡）"),
        (W3[1], "多卡方案的 TCO 计算包含：N 倍卡价 + 更高主机成本（多卡槽/ECC/RAM/供电）+ 更高功耗"),
        (W3[2], "给出单卡 vs 多卡的 TCO 翻转点（在什么利用率/电价/使用年限下多卡更优）"),
    ],
    # ═══ N-8.1 双卡互联开销 ═══
    "N-8.1": [
        (W3[0], "提到双卡需要 NVLink/PCIe 互联，有通信开销"),
        (W3[1], "说明 tensor parallelism 的通信开销对 decode 速度的影响（通常 <10%，但 prefill 更显著）"),
        (W3[2], "指出双卡方案的额外风险：单卡故障导致整系统停机（vs 单卡可降级运行）"),
    ],
    # ═══ SHARED 参数交互 ═══
    "SHARED": [  # gpu_price / quant / n 三处交互
        (W4[0], "提到某个参数同时影响多个维度（如量化同时影响成本和通过率）"),
        (W4[1], "quant 交互：W4 降成本（权重小→显存省/更快）但升成本（通过率↓），ΔG>0.08 时 W4 输给 W8"),
        (W4[2], "gpu_price 交互：卡价同时进摊销和故障损耗，真实弹性 0.275（比单看摊销高 17%）"),
        (W4[3], "n 并发数交互：n = min(n_speed, n_cap)，不是自由量——速度闸和显存闸取 min"),
    ],
    # ═══ 元认知：来源标注 + 条件性推荐 ═══
    "META": [  # 题目硬性要求
        (W4[0], "对至少一个规格数字标注了来源（刚查到的 vs 凭记忆的）"),
        (W4[1], "不确定的数字显式标了 [待核验] 而非默默省略"),
        (W4[2], "区分了'刚查到的'和'凭记忆的'两类信息"),
        (W4[3], "最终推荐是条件性的（在什么利用率/电价/采购时点下哪张卡最优），不同条件下给出不同选择"),
    ],
}


def build_judge_prompt(qid: str, answer: str) -> str:
    if qid == "nat":
        rubric = NAT_RUBRIC
    elif qid == "soc":
        rubric = SOC_RUBRIC
    elif qid == "gpu":
        rubric = GPU_RUBRIC
    else:
        raise ValueError(f"Unknown qid: {qid}")
    points_desc = []
    for pt_name, levels in rubric.items():
        pts = []
        for i, (w, desc) in enumerate(levels, 1):
            pts.append(f"  L{i}: {desc}")
        K = len(levels)
        # show what each score means on the [0,1] scale
        anchors = f"  (0=未触及, {1/K:.2f}=仅达L1, {2/K:.2f}=达L2, ..., 1.00=全部{K}层达成)"
        points_desc.append(f"{pt_name} [{K}层]{anchors}:\n" + "\n".join(pts))
    
    rubric_text = "\n".join(points_desc)
    return (
        "你是严格评分员。下面是一道题的深度评分标准和一个候选回答。\n"
        "对每个要点，给出一个 **0.00-1.00 的连续深度分**，表示候选回答在该要点上实际达到的深度位置。\n\n"
        "**打分规则（必须严格遵守）：**\n"
        "- 分数 = 实际达成的最高层级 / 总层数，可以在层级之间插值\n"
        "- 例：4层要点，提到了概念但没给量级 → 在 L1 和 L2 之间 → 0.25-0.35\n"
        "- 例：4层要点，给了量级和对比但没推导出数值 → 在 L3 和 L4 之间 → 0.65-0.75\n"
        "- **不要只给 0、1/K、2/K...这些离散锚点**——如果回答部分达到了某层（比如给了公式但没代入参数），给该层位置的一半（如 L2 部分达成 → 0.17 而非 0.33）\n"
        "- 仅提到概念名称但无量化/推导/对比 = 不超过 0.25\n"
        "- '打0.99折'≠'基于驻留时间推导折扣因子'——前者是拍脑袋，后者需要 T_res 量级 + 与访问间隔的显式对比\n"
        "- 给出公式但未代入题面参数 = 不超过 0.75（4层时）\n"
        "- 拿不准时往低判（宁严勿松）\n"
        "- 分数必须是两位小数的数字，不要输出 0/1 列表\n\n"
        f"深度评分标准：\n{rubric_text}\n\n"
        f"候选回答：\n{answer[:12000]}\n\n"
        '输出 JSON：{"scores": {"pt1": 0.xx, "pt2": 0.xx, ...}}\n'
        "每个值是一个 0.00-1.00 的数字。只输出 JSON，不要解释。"
    )


def score_run(qid: str, answer: str) -> dict:
    """Score one answer with depth rubric. Returns per-point continuous scores."""
    prompt = build_judge_prompt(qid, answer)
    content, _ = call_llm(prompt, max_tokens=2000, temperature=0)
    m = re.search(r"\{.*\}", content, re.S)
    try:
        d = json.loads(m.group(0)) if m else {}
    except json.JSONDecodeError:
        return {"error": content[:500]}
    
    if qid == "nat":
        rubric = NAT_RUBRIC
    elif qid == "soc":
        rubric = SOC_RUBRIC
    else:
        rubric = GPU_RUBRIC
    # LLM sometimes wraps in {"scores": {...}}, sometimes returns flat {pt1: x, ...}
    if "scores" in d and isinstance(d["scores"], dict):
        scores_raw = d["scores"]
    else:
        scores_raw = d
    point_scores = {}
    total = 0
    n_points = 0
    for pt_name, levels in rubric.items():
        raw = scores_raw.get(pt_name, 0)
        # handle both old format (list) and new format (scalar)
        if isinstance(raw, list):
            # legacy: convert 0/1 list to weighted score
            fixed = list(int(x) for x in raw[:len(levels)])
            for i in range(len(fixed) - 1, 0, -1):
                if fixed[i] == 1:
                    fixed[i-1] = 1
            score = sum(w * v for (w, _), v in zip(levels, fixed))
            point_scores[pt_name] = {"score": round(score, 3), "raw_levels": fixed}
        else:
            try:
                score = max(0.0, min(1.0, float(raw)))
            except (ValueError, TypeError):
                score = 0.0
            point_scores[pt_name] = {"score": round(score, 3)}
        total += score
        n_points += 1
    
    overall = total / max(n_points, 1)
    return {"point_scores": point_scores, "overall": round(overall, 4),
            "raw": scores_raw}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default="runs-prod")
    ap.add_argument("--arm", default="S0")
    ap.add_argument("--q", default="nat")
    ap.add_argument("--reps", default="1-30")
    args = ap.parse_args()
    
    lo, hi = args.reps.split("-")
    results = []
    for rep in range(int(lo), int(hi) + 1):
        fp = f"{args.runs}/{args.arm}-{args.q}-r{rep}.json"
        if not os.path.exists(fp):
            continue
        d = json.load(open(fp))
        ans = d["answer"]
        r = score_run(args.q, ans)
        r["tag"] = f"{args.arm}-{args.q}-r{rep}"
        results.append(r)
        pts_str = " ".join(f"{k}={v['score']}" for k, v in r.get("point_scores", {}).items())
        print(f"{r['tag']}: overall={r.get('overall', 'ERR')} (pts: {pts_str})", flush=True)
    
    # summary
    if results and "overall" in results[0]:
        overalls = [r["overall"] for r in results if "overall" in r]
        mean = sum(overalls) / len(overalls)
        sd = (sum((x-mean)**2 for x in overalls)/max(len(overalls)-1,1))**0.5
        print(f"\n=== SUMMARY: {args.arm}-{args.q} n={len(overalls)} ===")
        print(f"mean={mean:.4f} ± {sd:.4f}")
        # per-point means
        for pt in (NAT_RUBRIC if args.q == "nat" else SOC_RUBRIC if args.q == "soc" else GPU_RUBRIC):
            vals = [r["point_scores"][pt]["score"] for r in results if pt in r.get("point_scores",{})]
            if vals:
                pm = sum(vals)/len(vals)
                print(f"  {pt}: {pm:.3f}")
        # distribution
        buckets = [0]*10
        for o in overalls:
            b = min(int(o*10), 9)
            buckets[b] += 1
        print(f"distribution: {' '.join(f'{b/10:.1f}-{(b+1)/10:.1f}:{c}' for b,c in enumerate(buckets) if c)}")
    
    out_fp = f"{args.runs}/judge-v2-{args.arm}-{args.q}.json"
    with open(out_fp, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved → {out_fp}")


if __name__ == "__main__":
    main()