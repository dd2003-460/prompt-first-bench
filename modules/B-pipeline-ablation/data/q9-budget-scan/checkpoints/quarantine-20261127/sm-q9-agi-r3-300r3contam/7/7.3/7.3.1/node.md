# N234: 27B 模型 NVFP4 权重在 4xV100 上的显存分布：总权重体积为 13.5GB，TP=4 切片后每卡承载 3.375GB 权重，剩余单卡可用显存为 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

27B 模型 NVFP4 权重在 4xV100 上的显存分布：总权重体积为 13.5GB，TP=4 切片后每卡承载 3.375GB 权重，剩余单卡可用显存为 12.625GB（16GB - 3.375GB），用于分配 KV Cache 及激活值，此为计算最大并发批次的基础约束。

## Corrected Claim

27B 模型 NVFP4 权重在 4xV100 上的显存分布：总权重体积为 13.5GB，TP=4 切片后每卡承载 3.375GB 权重，剩余单卡可用显存为 12.625GB（16GB - 3.375GB），用于分配 KV Cache 及激活值，此为计算最大并发批次的基础约束。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型NVFP4精度下权重体积约13.5GB（27e9 * 0.5 bytes），TP=4切分后每卡3.375GB，16GB显存减去权重后剩余12.625GB，算术与量级均合理。

## Search Query

Qwen 27B NVFP4 weight size per GPU tensor parallelism 4 shards memory allocation
