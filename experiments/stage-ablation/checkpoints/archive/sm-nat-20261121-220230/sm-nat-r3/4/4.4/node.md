# N20: 更新率对有效命中率的折损因子：当对象更新率为 u=1%/天 时，LRU 的有效命中率 H_eff 与稳态命中率 H_steady 的关系为 H_eff = H_

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于计算 T_resident 的近似公式（输入端），子节点2聚焦于基于 T_resident 计算 P_invalid 的具体数值范围（输出端/应用端）。两者分别对应父节点公式中的两个关键变量，逻辑上构成“先求驻留时间，再求失效概率”的串行依赖关系，无内容重叠或矛盾，且共同覆盖了父节点中关于 T_resident 计算和 P_invalid 定义的核心要素。）
