# N8: 对象更新率 1%/天 导致 LRU 有效命中率折损系数 D = 1 - (1 - 0.01)^(T_resident)，其中 T_resident 是对象的平均

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

对象更新率 1%/天 导致 LRU 有效命中率折损系数 D = 1 - (1 - 0.01)^(T_resident)，其中 T_resident 是对象的平均驻留时间（由 LRU 替换策略和请求频率决定）

## Corrected Claim

对象更新率 1%/天 导致 LRU 有效命中率折损系数 D = 1 - (1 - 0.01)^(T_resident)，其中 T_resident 是对象的平均驻留时间（由 LRU 替换策略和请求频率决定）

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1和子节点4在定义 T_resident 时存在逻辑冲突和冗余。子节点1给出的是基于流速率的宏观近似（C/R_evict），而子节点4给出的是基于具体对象排名和Pareto分布的微观近似。这两者并非正交的独立维度，而是对同一变量（T_resident）的不同估算方法，且子节点4中关于“第N_cap+1个对象”的描述在LRU语境下通常用于确定驱逐边界，直接作为单个对象的平均驻留时间近似在逻辑上不够严谨，容易与子节点1的稳态平均概念混淆。此外，子节点3中的公式 H_eff = H_original * (1 - P_stale * H_original) 在数学上存在问题：如果 H_original 接近 1，P_stale 较小时，该公式可能产生非物理结果或逻辑偏差（通常有效命中率应为 H_original * (1 - P_stale) 或类似线性衰减，取决于失效定义），且它引入了父节点未明确定义的 H_original 依赖关系，使得分解边界不清。）
