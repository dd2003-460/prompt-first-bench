# N502: 工作点C的3年MTBF故障率模型：假设低可靠性盘MTBF=500,000小时，单盘年故障概率 P_fail_year = 1 - exp(-8760/50000

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N168

## Claim

工作点C的3年MTBF故障率模型：假设低可靠性盘MTBF=500,000小时，单盘年故障概率 P_fail_year = 1 - exp(-8760/500000) ≈ 1.7%。

## Corrected Claim

工作点C的3年MTBF故障率模型：假设低可靠性盘MTBF=500,000小时，单盘年故障概率 P_fail_year = 1 - exp(-8760/500000) ≈ 1.7%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - exp(-8760/500000) ≈ 1 - exp(-0.01752) ≈ 0.01736，即 1.7%，数值准确且符合指数分布故障率模型定义。
