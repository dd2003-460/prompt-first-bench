# N30: 对象更新率 1%/天 对 LRU 命中率的影响因子 f_update 可通过公式 f_update = 1 - (U_rate * T_residence) 估

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率 1%/天 对 LRU 命中率的影响因子 f_update 可通过公式 f_update = 1 - (U_rate * T_residence) 估算，其中 T_residence 为对象在缓存中的平均停留时间，若 T_residence < 100 天，则折损小于 1%，可忽略不计；否则需线性扣除。

## Corrected Claim

对象更新率 1%/天 对 LRU 命中率的影响因子 f_update 可通过公式 f_update = 1 - (U_rate * T_residence) 估算，其中 T_residence 为对象在缓存中的平均停留时间，若 T_residence < 100 天，则折损小于 1%，可忽略不计；否则需线性扣除。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的，分别处理了参数计算、模型失效/修正、阈值推导背景以及分布偏差修正，没有重复或矛盾。然而，完备性不足：父节点核心是'影响因子 f_update 的估算公式'，子节点2和4提出了更复杂的模型（指数衰减、联合分布修正），但没有给出在一般情况（非重尾、非长驻留）下，当 T_residence > 100 但分布正常时，应使用哪个具体公式或如何从线性过渡到更精确模型的完整决策路径；此外，子节点1依赖外部节点 N9/N10，未自包含所有必要参数定义。）
