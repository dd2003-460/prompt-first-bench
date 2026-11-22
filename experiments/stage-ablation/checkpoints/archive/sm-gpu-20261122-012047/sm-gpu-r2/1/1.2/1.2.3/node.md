# N52: 实际 KV Cache 占用需乘以实现因子 (Implementation Factor)，包括：(1) 对齐填充 (Alignment Padding)，通常

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

实际 KV Cache 占用需乘以实现因子 (Implementation Factor)，包括：(1) 对齐填充 (Alignment Padding)，通常增加 1-5%；(2) PagedAttention 块大小 (Block Size) 带来的碎片开销，通常为 0-10%；(3) 框架特定元数据 (Metadata)，可忽略不计。综合系数约为 1.05-1.15。

## Corrected Claim

实际 KV Cache 占用需乘以实现因子 (Implementation Factor)，包括：(1) 对齐填充 (Alignment Padding)，通常增加 1-5%；(2) PagedAttention 块大小 (Block Size) 带来的碎片开销，通常为 0-10%；(3) 框架特定元数据 (Metadata)，可忽略不计。综合系数约为 1.05-1.15。

## Evidence

先验知识/题面给定，逻辑校验通过
