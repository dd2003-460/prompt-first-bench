# N69: Tensor Parallelism (TP) 显存分布：在2卡TP下，权重和KV Cache均匀切分，每卡占用=Total_VRAM/2。对于FP8方案（总需

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

Tensor Parallelism (TP) 显存分布：在2卡TP下，权重和KV Cache均匀切分，每卡占用=Total_VRAM/2。对于FP8方案（总需35.6GB），每卡需17.8GB，2x RTX 4090 (24GB/卡) 可行；对于BF16方案（总需67.1GB），每卡需33.55GB，2x RTX 4090 (24GB/卡) 不可行，需2x A100 40GB或更高。

## Corrected Claim

Tensor Parallelism (TP) 显存分布：在2卡TP下，权重和KV Cache均匀切分，每卡占用=Total_VRAM/2。对于FP8方案（总需35.6GB），每卡需17.8GB，2x RTX 4090 (24GB/卡) 可行；对于BF16方案（总需67.1GB），每卡需33.55GB，2x RTX 4090 (24GB/卡) 不可行，需2x A100 40GB或更高。

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 冗余性高：两个子节点结构完全相同，仅精度和数值不同，本质上是同一计算逻辑（TP=2均分）在不同参数下的实例，应合并为一个通用公式或表格。2. 完备性不足：父节点明确包含“可行性判断”（RTX 4090 vs A100），但子节点仅陈述了显存占用数值，完全丢失了硬件适配性分析这一关键结论。）

## Search Query

Tensor Parallelism memory distribution LLM
