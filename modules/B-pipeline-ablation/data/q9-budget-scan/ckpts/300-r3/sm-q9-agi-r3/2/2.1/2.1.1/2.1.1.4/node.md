# N175: 重试机制的成本模型：每次重试需重新生成Query并重新计算熵，假设首次生成失败率p_fail=20%，则平均生成次数E[N]=1/(1-p_fail)=1.25

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

重试机制的成本模型：每次重试需重新生成Query并重新计算熵，假设首次生成失败率p_fail=20%，则平均生成次数E[N]=1/(1-p_fail)=1.25次，额外Token开销约为1.25 * Query_Len - Query_Len ≈ 0.25 * Query_Len tokens

## Corrected Claim

重试机制的成本模型：每次重试需重新生成Query并重新计算熵，假设首次生成失败率p_fail=20%，则平均生成次数E[N]=1/(1-p_fail)=1.25次，额外Token开销约为1.25 * Query_Len - Query_Len ≈ 0.25 * Query_Len tokens

## Evidence

先验知识/题面给定，逻辑校验通过：几何分布期望公式 E[N]=1/p_success 及线性成本叠加逻辑自洽，数值计算正确。
