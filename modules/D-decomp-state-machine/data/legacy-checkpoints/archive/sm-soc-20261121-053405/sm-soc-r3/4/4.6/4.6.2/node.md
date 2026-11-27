# N76: P_consult_after_disclosure 的波动区间量化：当 P_consult 在 [0.1, 0.3] 均匀分布时，其标准差 σ_P ≈ 0.0

- **status**: pending
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

父节点级核验未通过：不完备（子节点在逻辑上是正交的（一个定义误差分布，一个解释偏差来源），但存在严重的完备性缺失。父节点明确指出 P_consult 服从 [0.1, 0.3] 的均匀分布，并据此计算出标准差 σ_P ≈ 0.0577。然而，子节点1却将误差定义为高斯分布，且声称 σ_ε_P 取决于样本量 n 和 R²，标记为[待核验]，完全忽略了父节点中已知的均匀分布假设及其确定的统计量（均值0.2，标准差0.0577）。这导致子节点1未能继承父节点的核心约束条件，反而引入了与父节点计算基础不一致的新假设，使得分解无法自洽地解释父节点中的数值。）

## Search Query

uniform distribution standard deviation relative error propagation
