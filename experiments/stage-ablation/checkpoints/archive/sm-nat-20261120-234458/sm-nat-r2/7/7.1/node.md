# N60: H_LFU 的字节命中率计算模型：H_LFU = 1 - (Miss_Bytes_LFU / Total_Bytes)，其中 Miss_Bytes_LFU = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

H_LFU 的字节命中率计算模型：H_LFU = 1 - (Miss_Bytes_LFU / Total_Bytes)，其中 Miss_Bytes_LFU = Σ_{i ∉ Cache_LFU} (Size_i * Frequency_i)，Cache_LFU 为按 Frequency 降序排列且总大小 ≤ 128GB 的对象集合

## Corrected Claim

H_LFU 的字节命中率计算模型：H_LFU = 1 - (Miss_Bytes_LFU / Total_Bytes)，其中 Miss_Bytes_LFU = Σ_{i ∉ Cache_LFU} (Size_i * Frequency_i)，Cache_LFU 为按 Frequency 降序排列且总大小 ≤ 128GB 的对象集合

## Evidence

先验知识/题面给定，逻辑校验通过：LFU缓存策略基于频率排序，命中率公式符合定义，量纲与逻辑自洽。
