# N332: 修正矛盾后的A100 80GB并发扩展性：基于N141修正，BF16下单请求KV Cache为8.0 GB。A100 80GB总显存 - 权重54.36GB -

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N123

## Claim

修正矛盾后的A100 80GB并发扩展性：基于N141修正，BF16下单请求KV Cache为8.0 GB。A100 80GB总显存 - 权重54.36GB - 激活/开销2.0GB = 剩余23.64GB用于KV Cache。最大并发Batch Size = floor(23.64 GB / 8.0 GB) = 2。因此，A100 80GB在BF16下支持最大Batch Size=2的32K上下文并发，而非N123所述的Batch Size=1。

## Corrected Claim

修正矛盾后的A100 80GB并发扩展性：基于N141修正，BF16下单请求KV Cache为8.0 GB。A100 80GB总显存 - 权重54.36GB - 激活/开销2.0GB = 剩余23.64GB用于KV Cache。最大并发Batch Size = floor(23.64 GB / 8.0 GB) = 2。因此，A100 80GB在BF16下支持最大Batch Size=2的32K上下文并发，而非N123所述的Batch Size=1。

## Evidence

先验知识/题面给定，逻辑校验通过：80GB总显存减去54.36GB权重和2.0GB开销后剩余23.64GB，除以单请求8.0GB KV Cache，向下取整得2，计算自洽且符合硬件资源分配逻辑。

## Search Query

A100 80GB Qwen3-27B BF16 batch size 32k context concurrency
