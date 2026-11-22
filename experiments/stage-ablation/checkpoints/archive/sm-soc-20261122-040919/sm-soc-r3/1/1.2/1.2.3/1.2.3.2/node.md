# N148: 修正后的最低挂价阈值公式：P_min = P_ref * (1 + 1/λ)，其中 λ=2.25。代入得 P_min ≈ 1.444 * P_ref。此值对应 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N37

## Claim

修正后的最低挂价阈值公式：P_min = P_ref * (1 + 1/λ)，其中 λ=2.25。代入得 P_min ≈ 1.444 * P_ref。此值对应 44.4% 的溢价，高于观测到的 15% 下限，说明 15% 下限并非由单一 λ 决定，而是 P_min 与市场竞争压力（买家搜索成本 C_search）博弈后的均衡下界，需引入竞争修正项 δ_compete 使得 P_min_effective = P_min * (1 - δ_compete)。

## Corrected Claim

修正后的最低挂价阈值公式：P_min = P_ref * (1 + 1/λ)，其中 λ=2.25。代入得 P_min ≈ 1.444 * P_ref。此值对应 44.4% 的溢价，高于观测到的 15% 下限，说明 15% 下限并非由单一 λ 决定，而是 P_min 与市场竞争压力（买家搜索成本 C_search）博弈后的均衡下界，需引入竞争修正项 δ_compete 使得 P_min_effective = P_min * (1 - δ_compete)。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 + 1/2.25 ≈ 1.444 正确，推导出的 44.4% 溢价与 15% 观测值的矛盾逻辑自洽，且引入竞争修正项 δ_compete 以解释差异符合经济学均衡逻辑。

## Search Query

prospect theory pricing threshold competition adjustment model
