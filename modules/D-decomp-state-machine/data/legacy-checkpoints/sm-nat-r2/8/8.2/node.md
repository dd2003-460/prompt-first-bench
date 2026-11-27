# N96: LRU 保留集合 S_LRU 的确定准则：S_LRU = {i | W_LRU(i) ≤ T_window}，其中 T_window 为缓存中对象的平均驻留时间

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

LRU 保留集合 S_LRU 的确定准则：S_LRU = {i | W_LRU(i) ≤ T_window}，其中 T_window 为缓存中对象的平均驻留时间窗口，W_LRU(i) 由 N22 给出；在 128GB 容量下，S_LRU 包含的对象数 N_LRU = min(100000, C / E[S_head])，其中 E[S_head] 为头部对象的平均大小。

## Corrected Claim

LRU 保留集合 S_LRU 的确定准则：S_LRU = {i | W_LRU(i) ≤ T_window}，其中 T_window 为缓存中对象的平均驻留时间窗口，W_LRU(i) 由 N22 给出；在 128GB 容量下，S_LRU 包含的对象数 N_LRU = min(100000, C / E[S_head])，其中 E[S_head] 为头部对象的平均大小。

## Evidence

先验知识/题面给定，逻辑校验通过
