# N99: FP8 推理的硬件支持范围：H100/H200 原生支持 E4M3/E5M2 FP8 计算，而消费级 GPU (如 RTX 4090/5090) 仅支持 FP8

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

FP8 推理的硬件支持范围：H100/H200 原生支持 E4M3/E5M2 FP8 计算，而消费级 GPU (如 RTX 4090/5090) 仅支持 FP8 存储和反量化，计算仍为 BF16/FP16，因此 FP8 在消费级硬件上仅节省显存 (27GB vs 54GB) 而不提供计算加速，吞吐量提升有限 (约 10-15%)。

## Corrected Claim

FP8 推理的硬件支持范围：H100/H200 原生支持 E4M3/E5M2 FP8 计算，而消费级 GPU (如 RTX 4090/5090) 仅支持 FP8 存储和反量化，计算仍为 BF16/FP16，因此 FP8 在消费级硬件上仅节省显存 (27GB vs 54GB) 而不提供计算加速，吞吐量提升有限 (约 10-15%)。

## Evidence

先验知识/题面给定，逻辑校验通过：H100/H200 (Hopper架构) 原生支持FP8 Tensor Core计算，而RTX 4090/5090 (Ada/Blackwell架构) 虽支持FP8存储/反量化但缺乏原生FP8计算单元（或主要依赖BF16/FP16计算路径），导致消费级硬件上FP8主要节省显存而非提供显著计算加速，符合硬件架构事实。

## Search Query

FP8 inference support RTX 4090 vs H100 hardware acceleration compute
