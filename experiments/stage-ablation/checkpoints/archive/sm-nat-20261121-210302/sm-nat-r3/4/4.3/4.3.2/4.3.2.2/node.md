# N133: LRU 缓存内对象数量 N_cap 与热度阈值 P_th 的映射公式：N_cap = N_total * (1 - P_th^{β-1})，其中 N_total

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

LRU 缓存内对象数量 N_cap 与热度阈值 P_th 的映射公式：N_cap = N_total * (1 - P_th^{β-1})，其中 N_total=100,000，β=0.9

## Corrected Claim

LRU 缓存内对象数量 N_cap 与热度阈值 P_th 的映射公式：N_cap = N_total * (1 - P_th^{β-1})，其中 N_total=100,000，β=0.9

## Evidence

先验知识/题面给定，逻辑校验通过
