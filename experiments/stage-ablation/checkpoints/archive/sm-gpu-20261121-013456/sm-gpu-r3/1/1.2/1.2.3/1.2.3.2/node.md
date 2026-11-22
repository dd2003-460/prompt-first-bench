# N140: RTX 4090 (Ada Lovelace) 无原生 FP8 Tensor Core，其 FP8 推理需通过 CUDA 内核将 FP8 数据转换为 BF16 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

RTX 4090 (Ada Lovelace) 无原生 FP8 Tensor Core，其 FP8 推理需通过 CUDA 内核将 FP8 数据转换为 BF16 计算，实际吞吐量提升系数 ≈ 1.0x（无加速），甚至因转换开销可能低于 BF16 原生路径（来源：NVIDIA Ada Architecture Whitepaper）

## Corrected Claim

RTX 4090 (Ada Lovelace) 无原生 FP8 Tensor Core，其 FP8 推理需通过 CUDA 内核将 FP8 数据转换为 BF16 计算，实际吞吐量提升系数接近 1.0x（无明显加速），具体性能受软件优化和转换开销影响，可能略低于或接近 BF16 原生路径。

## Evidence

[质询]该陈述将‘无原生FP8 Tensor Core’与‘实际吞吐量提升系数≈1.0x（无加速）’直接等同，忽略了软件优化（如CUDA内核融合、内存带宽优化）可能带来的性能差异，且‘甚至因转换开销可能低于BF16原生路径’属于推测性结论，缺乏量化数据支持。 | 先验知识/题面给定，逻辑校验通过：RTX 4090确实无原生FP8 Tensor Core，FP8需转换为BF16计算，但吞吐量提升系数≈1.0x的表述过于绝对，未考虑软件优化可能带来的性能波动。

## Search Query

RTX 4090 Ada Lovelace FP8 support tensor core whitepaper
