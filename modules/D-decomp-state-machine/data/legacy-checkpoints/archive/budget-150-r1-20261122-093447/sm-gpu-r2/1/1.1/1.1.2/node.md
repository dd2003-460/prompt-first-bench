# N47: KV_Cache_MB 的计算中 bytes_per_elem 取决于 KV Cache 的存储精度：通常与模型权重精度一致或独立设置。若模型为 BF16，KV

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

KV_Cache_MB 的计算中 bytes_per_elem 取决于 KV Cache 的存储精度：通常与模型权重精度一致或独立设置。若模型为 BF16，KV Cache 通常也为 BF16 (2 bytes)；若使用 FP8 量化推理，KV Cache 可设为 FP8 (1 byte) 或 INT8 (1 byte)。

## Corrected Claim

KV_Cache_MB 的计算中 bytes_per_elem 取决于 KV Cache 的存储精度：通常与模型权重精度一致或独立设置。若模型为 BF16，KV Cache 通常也为 BF16 (2 bytes)；若使用 FP8 量化推理，KV Cache 可设为 FP8 (1 byte) 或 INT8 (1 byte)。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16精度对应2字节，FP8/INT8对应1字节，符合计算机体系结构与深度学习推理的基本事实。

## Search Query

KV cache precision FP8 INT8 inference memory
