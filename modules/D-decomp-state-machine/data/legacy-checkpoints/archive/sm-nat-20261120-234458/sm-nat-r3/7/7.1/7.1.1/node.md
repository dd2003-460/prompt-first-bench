# N182: Miss_Bytes_LFU (LFU 未命中字节数) 的计算：Miss_Bytes_LFU = Σ_{i ∉ Cache_LFU} (Size_i * Fre

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

Miss_Bytes_LFU (LFU 未命中字节数) 的计算：Miss_Bytes_LFU = Σ_{i ∉ Cache_LFU} (Size_i * Frequency_i)，其中 Cache_LFU 为按 Frequency 降序排列且总大小 ≤ 128GB 的对象集合；由于 K>N (容量充足)，Cache_LFU = 全部对象，故 Miss_Bytes_LFU = 0

## Corrected Claim

Miss_Bytes_LFU (LFU 未命中字节数) 的计算：Miss_Bytes_LFU = Σ_{i ∉ Cache_LFU} (Size_i * Frequency_i)，其中 Cache_LFU 为按 Frequency 降序排列且总大小 ≤ 128GB 的对象集合；由于 K>N (容量充足)，Cache_LFU = 全部对象，故 Miss_Bytes_LFU = 0

## Evidence

先验知识/题面给定，逻辑校验通过：LFU缓存策略在容量充足（K>N）时缓存所有对象，未命中集合为空，故未命中字节数为0，推导自洽。
