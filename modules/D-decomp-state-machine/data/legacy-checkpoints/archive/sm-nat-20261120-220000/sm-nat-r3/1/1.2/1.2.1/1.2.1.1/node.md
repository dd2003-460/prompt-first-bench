# N75: LRU字节命中率下界公式 H_LRU(C) = H_bytes_topK，其中 K 为缓存容量 C 能容纳的对象数量（按大小从小到大排序取前 K 个，假设热度与

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

LRU字节命中率下界公式 H_LRU(C) = H_bytes_topK，其中 K 为缓存容量 C 能容纳的对象数量（按大小从小到大排序取前 K 个，假设热度与大小负相关则小对象热度高，故前 K 个即最热对象）；需计算 K = max{n | Σ_{i=1}^n S_(i) ≤ C}，其中 S_(i) 为第 i 小对象的大小。

## Corrected Claim

LRU字节命中率下界公式 H_LRU(C) = H_bytes_topK，其中 K 为缓存容量 C 能容纳的对象数量（按大小从小到大排序取前 K 个，假设热度与大小负相关则小对象热度高，故前 K 个即最热对象）；需计算 K = max{n | Σ_{i=1}^n S_(i) ≤ C}，其中 S_(i) 为第 i 小对象的大小。

## Evidence

先验知识/题面给定，逻辑校验通过
