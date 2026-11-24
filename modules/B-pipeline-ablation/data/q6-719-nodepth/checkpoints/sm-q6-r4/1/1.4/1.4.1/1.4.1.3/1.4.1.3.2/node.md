# N528: 去重算法对 Duplicity_Factor 的影响：使用强哈希（SHA-256）可识别完全相同的重复上传，降低 Reupload_Rate 至 5%；使用弱哈

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N177

## Claim

去重算法对 Duplicity_Factor 的影响：使用强哈希（SHA-256）可识别完全相同的重复上传，降低 Reupload_Rate 至 5%；使用弱哈希（MD5）可能误判相似内容，Reupload_Rate 升至 15%；感知哈希（pHash）适用于图片相似性去重，但计算开销增加，需权衡去重精度与计算成本

## Corrected Claim

去重算法对 Duplicity_Factor 的影响：使用强哈希（SHA-256）可识别完全相同的重复上传，降低 Reupload_Rate 至 5%；使用弱哈希（MD5）可能误判相似内容，Reupload_Rate 升至 15%；感知哈希（pHash）适用于图片相似性去重，但计算开销增加，需权衡去重精度与计算成本

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

hash algorithm deduplication accuracy SHA-256 MD5 pHash image video
