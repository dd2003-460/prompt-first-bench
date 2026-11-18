# N10: 大小与热度负相关，Pearson 相关系数 ρ ≈ -0.3，需转化为联合分布或条件分布模型以计算命中概率 [待核验]

- **status**: pending
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

大小与热度负相关，Pearson 相关系数 ρ ≈ -0.3，需转化为联合分布或条件分布模型以计算命中概率 [待核验]

## Corrected Claim

大小与热度负相关，Pearson 相关系数 ρ ≈ -0.3，需转化为联合分布或条件分布模型以计算命中概率 [待核验]

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性缺陷：子节点2中的条件分布公式依赖于子节点1中定义的Copula参数和假设，两者存在强依赖关系而非正交独立，子节点2是子节点1推导出的具体应用，未形成独立的知识模块。2. 完备性缺陷：父节点要求“计算命中概率”，但子节点仅提供了联合分布构建和条件均值计算，缺失了从条件分布到具体“命中概率”（如P(S_i > threshold | r_i)）的积分或概率计算步骤，且未处理对数正态分布与原始尺度S的转换细节（如E[S]的矩生成函数处理），导致无法直接闭环解决父节点问题。）

## Search Query

Pareto correlation size popularity negative
