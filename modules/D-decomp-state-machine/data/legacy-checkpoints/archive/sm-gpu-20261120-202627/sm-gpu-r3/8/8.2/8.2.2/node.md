# N423: 基于带宽瓶颈，MI300X 推理 Qwen3-27B (BF16) 的理论最大吞吐量上限 = 5300 GB/s / 54 GB ≈ 98.1 tokens/s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

基于带宽瓶颈，MI300X 推理 Qwen3-27B (BF16) 的理论最大吞吐量上限 = 5300 GB/s / 54 GB ≈ 98.1 tokens/s，远高于 N136 预估的 20-40 tokens/s，表明软件栈或计算瓶颈是主要限制因素。

## Corrected Claim

基于带宽瓶颈，MI300X 推理 Qwen3-27B (BF16) 的理论最大吞吐量上限 = 5300 GB/s / 54 GB ≈ 98.1 tokens/s，远高于 N136 预估的 20-40 tokens/s，表明软件栈或计算瓶颈是主要限制因素。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X HBM3e 带宽约 5.3TB/s，Qwen3-27B BF16 权重约 54GB，算术强度低时受带宽限制，理论上限 5300/54 ≈ 98.1 tokens/s 计算正确且量级合理。
