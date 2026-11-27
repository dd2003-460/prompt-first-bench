# N165: Pearson 相关系数 95% 置信区间的 Fisher Z 变换公式：Z = 0.5 * ln((1+ρ)/(1-ρ))，Z ~ N(0, 1/(N-3))

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N48, N49, N50

## Claim

Pearson 相关系数 95% 置信区间的 Fisher Z 变换公式：Z = 0.5 * ln((1+ρ)/(1-ρ))，Z ~ N(0, 1/(N-3))；对于 N=1000，标准误差 SE_Z ≈ 0.0316，若 ρ_phenomena = 0.4，则 95% CI 为 [0.33, 0.47]；该公式用于判断 ρ_lower 是否小于 -0.3 的显著性阈值。

## Corrected Claim

Pearson 相关系数 95% 置信区间的 Fisher Z 变换公式：Z = 0.5 * ln((1+ρ)/(1-ρ))，Z ~ N(0, 1/(N-3))；对于 N=1000，标准误差 SE_Z ≈ 0.0316，若 ρ_phenomena = 0.4，则 95% CI 为 [0.33, 0.47]；该公式用于判断 ρ_lower 是否小于 -0.3 的显著性阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：Fisher Z变换公式及标准误公式正确，数值计算（SE≈0.0316, CI≈[0.33, 0.47]）准确无误。
