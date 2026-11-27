# N20: 更新率对有效命中率的折损因子：当对象更新率为 u=1%/天 时，LRU 的有效命中率 H_eff 与稳态命中率 H_steady 的关系为 H_eff = H_

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

更新率对有效命中率的折损因子：当对象更新率为 u=1%/天 时，LRU 的有效命中率 H_eff 与稳态命中率 H_steady 的关系为 H_eff = H_steady * (1 - P_invalid)，其中 P_invalid 是缓存对象在访问前被更新（失效）的概率。在指数更新模型下，P_invalid ≈ 1 - exp(-u * T_resident)，T_resident 是对象在缓存中的平均驻留时间，需通过 Little's Law 和访问间隔分布计算。

## Corrected Claim

更新率对有效命中率的折损因子：当对象更新率为 u=1%/天 时，LRU 的有效命中率 H_eff 与稳态命中率 H_steady 的关系为 H_eff = H_steady * (1 - P_invalid)，其中 P_invalid 是缓存对象在访问前被更新（失效）的概率。在指数更新模型下，P_invalid ≈ 1 - exp(-u * T_resident)，T_resident 是对象在缓存中的平均驻留时间，需通过 Little's Law 和访问间隔分布计算。

## Evidence

父节点级核验未通过：不完备（子节点1和子节点2在逻辑上是正交的，分别处理了公式中的两个核心变量（T_resident和P_invalid的计算）。然而，完备性存在缺陷：父节点明确指出P_invalid的计算依赖于T_resident，且T_resident需通过Little's Law和访问间隔分布计算，但子节点1仅给出了一个包含未定义变量（C_norm, P_eviction）的近似公式，未涵盖父节点要求的'Little's Law'和'访问间隔分布'的具体推导路径；此外，子节点2仅展示了数值示例，未提供通用的解析计算框架。）
