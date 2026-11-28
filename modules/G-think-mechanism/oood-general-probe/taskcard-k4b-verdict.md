# 任务卡 K4b — 2×2 域味判决（预注册，数据到即机械套用）

# origin: ai · 2026-11-27 22:4x 预注册 · 载体: 判断-Lead（K4a 数据到位后 Lead 直接执行，不派 sub）
# 目的: 把判决规则在数据看到之前钉死，防"看到数字再编理由"。本卡 = 判决 SOP，不是数据。

## 输入（K4a 产出，只读）
- `experiments/stage-ablation/oood-probe/metrics-2x2.json`（6 臂机械指标 + 气象 4 机制 + 硬件 37unit 批判 + gate_cov）
- 左列已有半判决: `modules/G-think-mechanism/oood-general-probe/oood-column-status.md`（S1 OOD ≥ S0 OOD，已排除"负资产"格）

## 判决矩阵（预注册，源自 kernel-config-split.md §4, b2af0909d）

主指标（硬件列）: `unit_cov`（37 gold unit 覆盖率）+ `gate_cov`（11 gate unit 覆盖率）
辅助指标（气象列）: `mech_cov`（4 机制）+ `quant_claims`（仅作记录，不作判决依据——S0 含 18 次检索调用，quant 差值有检索混淆）

等价带: Δ = S1 − S0 ∈ [−5pp, +5pp] 判"≈"；> +5pp 判 S1 胜；< −5pp 判 S0 胜。
（n=1 rep/臂，无 CI——判决措辞上限为"单域证据指向"，不写"证明"。）

| 格 | 条件（硬件列） | 判决 | 对 D 问题的答案 |
|---|---|---|---|
| 1 负资产 | S1_hw ≥ S0_hw 且 S1_ood > S0_ood | 域味纯有害，直接删 | （已被左列数据排除: S1_ood ≈ S0_ood 非 >） |
| 2 域适配配置（最理想） | S1_hw < S0_hw 且 S1_ood ≥ S0_ood | 核 general，域味=可插拔配置，三层分离架构成立 | **GPU 不 general 的回应: 核 general，域味是配置不是核** |
| 3 功能（核不 general） | S1_hw < S0_hw 且 S1_ood < S0_ood | 核离不开域味，需 domain-free 化重设计 | 当前核不 general，OOD 探针价值=定位了不 general 的位置 |
| 4 双弱 | S1_hw ≈ S0_hw 且 S1_ood ≈ S0_ood | 域味无害但也无功能，可隔离保留 | 核 general（弱证据），域味可留可删 |

## 执行节（K4a 数据到后，Lead 直接做，~10 分钟）
1. 读 metrics-2x2.json，抽 S0_hw/S1_hw 的 unit_cov + gate_cov，算 Δ
2. 对照上表定格（gate_cov 与 unit_cov 方向不一致时以 unit_cov 为准，gate_cov 记入备注）
3. 写判决节 append 进 `modules/G-think-mechanism/oood-general-probe/oood-column-status.md`（含: 定格 + 数字 + 对 D 问题的一句话答案 + 数据质量注记）
4. commit: `git add modules/G-think-mechanism/oood-general-probe/ && git commit -m "verdict: K4b 2x2 域味判决 (格N: <结论>)"`
5. 回报 D 一句话: 定格 + 对"GPU 不 general 为什么搞这些"的答案

## 边界
- 不重跑任何臂；K4a 有 parse_error 批次时，受影响 unit 从分母剔除并在判决节注明（如 37→30）
- 判决措辞上限"单域证据指向"；推广到 6 域电池（Q10-Q15）是后续工作，本判决不越界
- 若 K4a 数据异常（臂缺失/文件损坏）→ 不判决，重派 K4a 补数据
