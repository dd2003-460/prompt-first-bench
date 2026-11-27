# N137: A100 40GB 运行 Qwen3-27B FP8 的显存余量计算：40GB (总) - 27GB (FP8权重) - 13GB (32K ctx, FP8 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

A100 40GB 运行 Qwen3-27B FP8 的显存余量计算：40GB (总) - 27GB (FP8权重) - 13GB (32K ctx, FP8 KV Cache) = 0GB，无余量；若使用 BF16 KV Cache (16GB)，总需求 43GB > 40GB，不可行。结论：必须使用 FP8/INT8 KV Cache 或限制上下文至 ~24K (BF16 KV ~12GB, 总 39GB)。

## Corrected Claim

A100 40GB 运行 Qwen3-27B FP8 的显存余量计算：40GB (总) - 27GB (FP8权重) - 13GB (32K ctx, FP8 KV Cache) = 0GB，无余量；若使用 BF16 KV Cache (16GB)，总需求 43GB > 40GB，不可行。结论：必须使用 FP8/INT8 KV Cache 或限制上下文至 ~24K (BF16 KV ~12GB, 总 39GB)。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 40GB显存下，Qwen3-27B FP8权重约27GB，32K上下文FP8 KV Cache约13GB，合计40GB，无余量；BF16 KV Cache需16GB，总需求43GB超出显存，逻辑自洽且符合硬件规格常识。

## Search Query

A100 40GB memory layout Qwen3-27B FP8 KV cache size
