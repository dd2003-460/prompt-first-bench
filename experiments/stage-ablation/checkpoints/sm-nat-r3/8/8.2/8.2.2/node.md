# N275: LRU 保留对象数 N_LRU 的计算：N_LRU = min(100000, 128GB / E[S_head])，其中 E[S_head] 为头部对象平均大

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

LRU 保留对象数 N_LRU 的计算：N_LRU = min(100000, 128GB / E[S_head])，其中 E[S_head] 为头部对象平均大小，若 E[S_head] = 1.1KB，则 N_LRU = 100000，表明 LRU 可缓存全部对象。

## Corrected Claim

LRU 保留对象数 N_LRU 的计算：N_LRU = min(100000, 128GB / E[S_head])，其中 E[S_head] 为头部对象平均大小，若 E[S_head] = 1.1KB，则 N_LRU = 100000，表明 LRU 可缓存全部对象。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB / 1.1KB ≈ 119,409,523，远大于 100,000，故 min(100,000, 119,409,523) = 100,000，计算与结论自洽。
