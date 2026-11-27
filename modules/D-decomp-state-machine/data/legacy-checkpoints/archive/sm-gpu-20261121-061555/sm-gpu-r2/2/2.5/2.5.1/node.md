# N69: Tensor Parallelism (TP) 显存分布：在2卡TP下，权重和KV Cache均匀切分，每卡占用=Total_VRAM/2。对于FP8方案（总需

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

Tensor Parallelism (TP) 显存分布：在2卡TP下，权重和KV Cache均匀切分，每卡占用=Total_VRAM/2。对于FP8方案（总需35.6GB），每卡需17.8GB，2x RTX 4090 (24GB/卡) 可行；对于BF16方案（总需67.1GB），每卡需33.55GB，2x RTX 4090 (24GB/卡) 不可行，需2x A100 40GB或更高。

## Corrected Claim

Tensor Parallelism (TP) 显存分布：在2卡TP下，权重和KV Cache均匀切分，每卡占用=Total_VRAM/2。对于FP8方案（总需35.6GB），每卡需17.8GB，2x RTX 4090 (24GB/卡) 可行；对于BF16方案（总需67.1GB），每卡需33.55GB，2x RTX 4090 (24GB/卡) 不可行，需2x A100 40GB或更高。

## Evidence

先验知识/题面给定，逻辑校验通过：TP切分原理正确，数值计算（35.6/2=17.8, 67.1/2=33.55）准确，硬件容量对比（17.8<24, 33.55>24）符合物理直觉。

## Search Query

Tensor Parallelism memory distribution LLM
