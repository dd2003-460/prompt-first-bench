# N79: 若容量不足 (C < Total_Bytes)，LRU 的空间缺失字节数 Miss_Bytes_LRU 的解析近似：Miss_Bytes_LRU ≈ ∫_{S_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

若容量不足 (C < Total_Bytes)，LRU 的空间缺失字节数 Miss_Bytes_LRU 的解析近似：Miss_Bytes_LRU ≈ ∫_{S_threshold}^{S_max} s * f(s) ds，其中 S_threshold 是 LRU 缓存中保留对象的大小阈值，由缓存容量 C 和访问频率分布共同决定；高频小对象被保留，低频大对象被驱逐。

## Corrected Claim

若容量不足 (C < Total_Bytes)，LRU 的空间缺失字节数 Miss_Bytes_LRU 的解析近似：Miss_Bytes_LRU ≈ ∫_{S_threshold}^{S_max} s * f(s) ds，其中 S_threshold 是 LRU 缓存中保留对象的大小阈值，由缓存容量 C 和访问频率分布共同决定；高频小对象被保留，低频大对象被驱逐。

## Evidence

先验知识/题面给定，逻辑校验通过
