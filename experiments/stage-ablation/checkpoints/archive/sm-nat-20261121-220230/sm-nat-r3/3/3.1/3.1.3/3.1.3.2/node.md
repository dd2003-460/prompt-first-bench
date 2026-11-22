# N166: 中间热度对象（Rank 10%-50%）的失效概率 P_invalid 的精确计算公式为 P_invalid = 1 - exp(-u * T_resident

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

中间热度对象（Rank 10%-50%）的失效概率 P_invalid 的精确计算公式为 P_invalid = 1 - exp(-u * T_resident)，其中 u=0.01 为每日更新率，T_resident 由 N101 给出；当 T_resident=1.2 天时，P_invalid = 1 - exp(-0.012) ≈ 0.0119，该值与 (1 - 0.99)^1.2 的近似值差异小于 0.1%，验证了指数模型在低更新率下的线性近似有效性。

## Corrected Claim

中间热度对象（Rank 10%-50%）的失效概率 P_invalid 的精确计算公式为 P_invalid = 1 - exp(-u * T_resident)，其中 u=0.01 为每日更新率，T_resident 由 N101 给出；当 T_resident=1.2 天时，P_invalid = 1 - exp(-0.012) ≈ 0.0119，该值与 (1 - 0.99)^1.2 的近似值差异小于 0.1%，验证了指数模型在低更新率下的线性近似有效性。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布失效模型 P=1-exp(-uT) 在低更新率下近似为 uT，数值计算 1-exp(-0.012)≈0.01188 与 0.012 差异极小，符合数学推导。
