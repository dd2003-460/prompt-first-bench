# N726: FP8 E4M3 精度下 32K 上下文单请求 KV Cache 占用为 4.0 GB (256 KB/token * 32768 tokens * 0.5 压

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N257

## Claim

FP8 E4M3 精度下 32K 上下文单请求 KV Cache 占用为 4.0 GB (256 KB/token * 32768 tokens * 0.5 压缩比)，相比 BF16 (8 GB) 减少 50%，该数值为总内存需求的关键变量。

## Corrected Claim

FP8 E4M3 精度下 32K 上下文单请求 KV Cache 占用为 4.0 GB (256 KB/token * 32768 tokens * 0.5 压缩比)，相比 BF16 (8 GB) 减少 50%，该数值为总内存需求的关键变量。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 (8-bit) 相比 BF16 (16-bit) 数据量减半，50% 压缩比符合位宽差异；4.0 GB 与 8 GB 的数值关系自洽。
