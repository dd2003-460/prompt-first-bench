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

父节点级核验未通过：非正交, 有冗余（子节点3和4存在逻辑冲突且内容重叠。子节点3指出重尾分布下大对象驻留时间‘显著长于’平均，导致平均T_residence低估折损；子节点4指出大对象因占用空间多被‘更快驱逐’，导致平均T_residence低估大对象惩罚。这两者对‘大对象驻留时间与平均关系’的描述矛盾（一个说长于，一个说短于/更快驱逐），且两者都在讨论分布偏差对平均T_residence的修正，属于同一维度的问题，正交性不足。）
