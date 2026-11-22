# N244: 字节加权平均折损系数 D_eff 的最终积分表达式为 D_eff = 1 - [∫ P(Evict|Dirty)(h) * S(h) * f_{S,H}(s,h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

字节加权平均折损系数 D_eff 的最终积分表达式为 D_eff = 1 - [∫ P(Evict|Dirty)(h) * S(h) * f_{S,H}(s,h) ds dh] / [∫ S(h) * f_{S,H}(s,h) ds dh]，其中积分域受限于缓存容量 C 能容纳的对象集合，需代入 N90 和 N91 的公式进行数值求解。

## Corrected Claim

字节加权平均折损系数 D_eff 的最终积分表达式为 D_eff = 1 - [∫ P(Evict|Dirty)(h) * S(h) * f_{S,H}(s,h) ds dh] / [∫ S(h) * f_{S,H}(s,h) ds dh]，其中积分域受限于缓存容量 C 能容纳的对象集合，需代入 N90 和 N91 的公式进行数值求解。

## Evidence

先验知识/题面给定，逻辑校验通过
