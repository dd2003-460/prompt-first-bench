# N522: Batch_Size=4 时，每序列分配 64K tokens KV Cache，总 KV 占用 = 4 × 64K × 8KB = 2GB，而非 N186 中

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N186

## Claim

Batch_Size=4 时，每序列分配 64K tokens KV Cache，总 KV 占用 = 4 × 64K × 8KB = 2GB，而非 N186 中声称的 8GB（可能混淆了总容量与单 batch 占用）

## Corrected Claim

Batch_Size=4 时，每序列分配 64K tokens KV Cache，总 KV 占用 = 4 × 64K × 8KB = 2GB，而非 N186 中声称的 8GB（可能混淆了总容量与单 batch 占用）

## Evidence

先验知识/题面给定，逻辑校验通过：4 * 64K * 8KB = 2GB，计算无误且量级合理
