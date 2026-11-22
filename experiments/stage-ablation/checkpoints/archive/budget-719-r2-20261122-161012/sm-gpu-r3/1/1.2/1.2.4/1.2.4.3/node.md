# N151: 在 H100 80GB 显存下，扣除 55GB BF16 权重后剩余 25GB，可支持的最大并发 Batch Size (含 32K 上下文) 为 floor(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

在 H100 80GB 显存下，扣除 55GB BF16 权重后剩余 25GB，可支持的最大并发 Batch Size (含 32K 上下文) 为 floor(25GB / 8.59GB) = 2，即最多同时处理 2 个 32K 请求；若使用 FP8 KV Cache，Batch Size 提升至 floor(25GB / 4.29GB) = 5，吞吐量线性提升 2.5 倍 [knowledge]

## Corrected Claim

在 H100 80GB 显存下，扣除 55GB BF16 权重后剩余 25GB，可支持的最大并发 Batch Size (含 32K 上下文) 为 floor(25GB / 8.59GB) = 2，即最多同时处理 2 个 32K 请求；若使用 FP8 KV Cache，Batch Size 提升至 floor(25GB / 4.29GB) = 5，吞吐量线性提升 2.5 倍 [knowledge]

## Evidence

先验知识/题面给定，逻辑校验通过：80-55=25GB，25/8.59≈2.91取整为2，25/4.29≈5.82取整为5，5/2=2.5倍，计算与逻辑自洽。
