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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的分子（Miss_Bytes）和分母（Total_Bytes），两者定义独立且无逻辑重叠，共同完整构成了命中率计算的输入部分，不存在冗余。）
