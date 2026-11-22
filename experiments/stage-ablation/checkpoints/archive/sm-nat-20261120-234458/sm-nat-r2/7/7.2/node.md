# N61: H_LRU 的字节命中率计算模型：H_LRU = 1 - (Miss_Bytes_LRU / Total_Bytes)，其中 Miss_Bytes_LRU 需通

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

H_LRU 的字节命中率计算模型：H_LRU = 1 - (Miss_Bytes_LRU / Total_Bytes)，其中 Miss_Bytes_LRU 需通过 LRU 驱逐仿真或基于访问间隔的解析近似计算，不能简单用频率排序代替

## Corrected Claim

H_LRU 的字节命中率计算模型：H_LRU = 1 - (Miss_Bytes_LRU / Total_Bytes)，其中 Miss_Bytes_LRU 需通过 LRU 驱逐仿真或基于访问间隔的解析近似计算，不能简单用频率排序代替

## Evidence

先验知识/题面给定，逻辑校验通过：LRU命中率定义符合标准缓存指标公式，且LRU算法依赖最近访问顺序而非频率，故不能简单用频率排序代替，逻辑自洽。
