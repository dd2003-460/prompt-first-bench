# N200: Apple M2 Ultra (192GB Unified Memory) 在 BF16 精度下完全可行，剩余显存余量为 106.0 GB (192.0 GB 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

Apple M2 Ultra (192GB Unified Memory) 在 BF16 精度下完全可行，剩余显存余量为 106.0 GB (192.0 GB 容量 - 86.0 GB 需求)，可支持 Batch Size 扩展或更长上下文。

## Corrected Claim

Apple M2 Ultra (192GB Unified Memory) 在 BF16 精度下完全可行，剩余显存余量为 106.0 GB (192.0 GB 容量 - 86.0 GB 需求)，可支持 Batch Size 扩展或更长上下文。

## Evidence

先验知识/题面给定，逻辑校验通过：192GB - 86GB = 106GB，算术正确；M2 Ultra 支持 192GB 统一内存，BF16 下 86GB 需求在容量范围内，逻辑自洽。
