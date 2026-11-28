# N185: 工作点1（高KV缓存容量）：FP8量化，Block_Size=16，单卡KV Cache上限≈256K tokens，适合长文档处理，但PagedAttenti

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

工作点1（高KV缓存容量）：FP8量化，Block_Size=16，单卡KV Cache上限≈256K tokens，适合长文档处理，但PagedAttention碎片率3-7%导致实际可用容量降至238K-248K tokens

## Corrected Claim

工作点1（高KV缓存容量）：FP8量化，Block_Size=16，单卡KV Cache上限≈256K tokens，适合长文档处理，但PagedAttention碎片率3-7%导致实际可用容量降至238K-248K tokens

## Evidence

先验知识/题面给定，逻辑校验通过
