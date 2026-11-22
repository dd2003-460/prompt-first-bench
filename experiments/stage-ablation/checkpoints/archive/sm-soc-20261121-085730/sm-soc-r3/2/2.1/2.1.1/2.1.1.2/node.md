# N182: k 的 95% 置信区间 [0.25, 0.45] 的计算依赖于样本标准误 SE_k，SE_k = sqrt(Var(ε) / Σ(Premium_i^2))，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

k 的 95% 置信区间 [0.25, 0.45] 的计算依赖于样本标准误 SE_k，SE_k = sqrt(Var(ε) / Σ(Premium_i^2))，其中 Var(ε) 为残差方差，Σ(Premium_i^2) 为溢价率平方和，需明确样本量 N 对区间宽度的影响。

## Corrected Claim

k 的 95% 置信区间 [0.25, 0.45] 的计算依赖于样本标准误 SE_k，SE_k = sqrt(Var(ε) / Σ(Premium_i^2))，其中 Var(ε) 为残差方差，Σ(Premium_i^2) 为溢价率平方和，需明确样本量 N 对区间宽度的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合线性回归中斜率系数标准误的标准定义（SE = σ/√Σx²），置信区间构造逻辑自洽。
