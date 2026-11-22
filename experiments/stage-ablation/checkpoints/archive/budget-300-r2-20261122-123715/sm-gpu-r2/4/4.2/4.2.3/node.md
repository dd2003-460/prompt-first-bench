# N89: CPU Offload 场景下，当 3GB 权重存储在 DDR4/DDR5 内存 (带宽 ~50-100 GB/s) 时，推理吞吐瓶颈由显存带宽 (1008 G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

CPU Offload 场景下，当 3GB 权重存储在 DDR4/DDR5 内存 (带宽 ~50-100 GB/s) 时，推理吞吐瓶颈由显存带宽 (1008 GB/s) 转为内存带宽，理论最大吞吐下降系数 k_offload = MemBW_DDR / MemBW_GDDR ≈ 0.05-0.1，即速度降至原来的 5-10%，交互体验极差。

## Corrected Claim

CPU Offload 场景下，当 3GB 权重存储在 DDR4/DDR5 内存 (带宽 ~50-100 GB/s) 时，推理吞吐瓶颈由显存带宽 (1008 GB/s) 转为内存带宽，理论最大吞吐下降系数 k_offload = MemBW_DDR / MemBW_GDDR ≈ 0.05-0.1，即速度降至原来的 5-10%，交互体验极差。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽比 50-100/1008 ≈ 0.05-0.1，符合内存带宽瓶颈下的吞吐下降理论推导。
