# N159: SEM 路径系数标准误的 Bootstrap 计算具体化：σ²_SEM = Var_{b=1}^{1000}(β_b)，其中 β_b 为第 b 次重抽样的 ML

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N51

## Claim

SEM 路径系数标准误的 Bootstrap 计算具体化：σ²_SEM = Var_{b=1}^{1000}(β_b)，其中 β_b 为第 b 次重抽样的 MLE 估计值；95% 置信区间定义为 [β_{2.5%}, β_{97.5%}]，若区间不包含 0 且宽度 < 2 * SE(β)，则判定估计稳定。

## Corrected Claim

SEM 路径系数标准误的 Bootstrap 计算具体化：σ²_SEM = Var_{b=1}^{1000}(β_b)，其中 β_b 为第 b 次重抽样的 MLE 估计值；95% 置信区间定义为 [β_{2.5%}, β_{97.5%}]，若区间不包含 0 且宽度 < 2 * SE(β)，则判定估计稳定。

## Evidence

先验知识/题面给定，逻辑校验通过
