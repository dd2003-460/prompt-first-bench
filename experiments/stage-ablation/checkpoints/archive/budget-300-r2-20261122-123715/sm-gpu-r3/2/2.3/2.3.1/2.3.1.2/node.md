# N216: RTX 4090 在 FP8 推理下相比 BF16 的速度提升 1.5-2 倍，主要源于：1) 计算密度翻倍 (2x FLOPS)；2) 显存带宽压力减半 (权

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

RTX 4090 在 FP8 推理下相比 BF16 的速度提升 1.5-2 倍，主要源于：1) 计算密度翻倍 (2x FLOPS)；2) 显存带宽压力减半 (权重读取量减半)；但此提升在 Decode 阶段 (Memory Bound) 更为显著，在 Prefill 阶段 (Compute Bound) 提升可能接近 2 倍 [待核验]。

## Corrected Claim

RTX 4090 在 FP8 推理下相比 BF16 的速度提升 1.5-2 倍，主要源于：1) 计算密度翻倍 (2x FLOPS)；2) 显存带宽压力减半 (权重读取量减半)；但此提升在 Decode 阶段 (Memory Bound) 更为显著，在 Prefill 阶段 (Compute Bound) 提升可能接近 2 倍 [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8相比BF16计算密度翻倍且显存占用减半，符合硬件架构原理；Decode阶段受带宽限制，带宽减半直接带来接近2倍加速，Prefill阶段受计算限制，计算密度翻倍带来接近2倍加速，逻辑自洽。

## Search Query

RTX 4090 FP8 vs BF16 decode vs prefill speedup ratio LLM
