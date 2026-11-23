# N22: 缓存容量匹配度 C_match = Cache_Size / (s_avg * N_unique_hot)，其中 N_unique_hot 为热点对象数；匹配度

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

缓存容量匹配度 C_match = Cache_Size / (s_avg * N_unique_hot)，其中 N_unique_hot 为热点对象数；匹配度 <1 时命中率显著下降

## Corrected Claim

缓存容量匹配度 C_match = Cache_Size / (s_avg * N_unique_hot)，其中 N_unique_hot 为热点对象数；匹配度 <1 时命中率显著下降

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了缓存容量需求（Cache_Size）、热点对象数（N_unique_hot）的估算方法，以及容量不足时的命中率衰减模型。这三个方面分别对应父节点公式中的分子、分母中的关键变量以及公式结果（C_match < 1）的后果，彼此独立且共同构成了对父节点逻辑的完整支撑，无重复或矛盾。）
