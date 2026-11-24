# N177: 唯一对象数 U 的低估风险修正：若存在重复上传或转码生成多版本（如 720p/1080p），实际 Unique Objects 可能为原始上传数的 2-3 倍，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

唯一对象数 U 的低估风险修正：若存在重复上传或转码生成多版本（如 720p/1080p），实际 Unique Objects 可能为原始上传数的 2-3 倍，即 U_corrected = U_base × Duplicity_Factor (1.5-3.0)，需通过去重算法或哈希表验证

## Corrected Claim

唯一对象数 U 的低估风险修正：若存在重复上传或转码生成多版本（如 720p/1080p），实际 Unique Objects 可能为原始上传数的 2-3 倍，即 U_corrected = U_base × Duplicity_Factor (1.5-3.0)，需通过去重算法或哈希表验证

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN unique object count deduplication factor video transcoding
