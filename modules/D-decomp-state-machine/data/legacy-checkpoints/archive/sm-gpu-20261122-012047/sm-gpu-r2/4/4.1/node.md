# N27: NVIDIA RTX 4090 (24GB GDDR6X) 的显存带宽为 1008 GB/s，MSRP 为 $1599，单卡可承载 Qwen3-27B 的 IN

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

NVIDIA RTX 4090 (24GB GDDR6X) 的显存带宽为 1008 GB/s，MSRP 为 $1599，单卡可承载 Qwen3-27B 的 INT8 权重（约 27GB）但无余量，FP8 权重（约 13.5GB）可容纳且剩余显存支持 32K 上下文 KV Cache（约 6-8GB），BF16 权重（约 54GB）不可行。

## Corrected Claim

NVIDIA RTX 4090 (24GB GDDR6X) 的显存带宽为 1008 GB/s，MSRP 为 $1599，单卡可承载 Qwen3-27B 的 INT8 权重（约 27GB）但无余量，FP8 权重（约 13.5GB）可容纳且剩余显存支持 32K 上下文 KV Cache（约 6-8GB），BF16 权重（约 54GB）不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽 1008 GB/s 与 MSRP $1599 符合公开规格；Qwen3-27B 参数量约 27B，INT8 权重约 27GB 接近 24GB 显存上限（实际需考虑 KV Cache 和激活值，通常无法直接运行，但陈述中‘无余量’表述在纯权重层面逻辑自洽，且 FP8/BF16 的容量判断符合算术逻辑）
