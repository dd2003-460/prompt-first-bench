# N76: P_consult_after_disclosure 的波动区间量化：当 P_consult 在 [0.1, 0.3] 均匀分布时，其标准差 σ_P ≈ 0.0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N23, N24, N25

## Claim

P_consult_after_disclosure 的波动区间量化：当 P_consult 在 [0.1, 0.3] 均匀分布时，其标准差 σ_P ≈ 0.0577，均值 μ_P = 0.2，相对标准差 σ_rel ≈ 28.8%。结合 S=1.0，预测 ΔR 置信区间宽度约为 ±29%（与 N23 声称的 ±20% 存在偏差，需修正模型假设或 S 值）。

## Corrected Claim

P_consult_after_disclosure 的波动区间量化：当 P_consult 在 [0.1, 0.3] 均匀分布时，其标准差 σ_P ≈ 0.0577，均值 μ_P = 0.2，相对标准差 σ_rel ≈ 28.8%。结合 S=1.0，预测 ΔR 置信区间宽度约为 ±29%（与 N23 声称的 ±20% 存在偏差，需修正模型假设或 S 值）。

## Evidence

先验知识/题面给定，逻辑校验通过：均匀分布[0.1, 0.3]的均值0.2、标准差(0.2/√12)≈0.0577、相对标准差28.8%计算正确，且与S=1.0推导出的±29%置信区间宽度逻辑自洽。

## Search Query

uniform distribution standard deviation relative error propagation
