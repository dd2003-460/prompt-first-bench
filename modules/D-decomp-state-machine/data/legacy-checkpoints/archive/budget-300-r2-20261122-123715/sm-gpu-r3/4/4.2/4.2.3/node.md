# N89: CPU Offload 场景下，当 3GB 权重存储在 DDR4/DDR5 内存 (带宽 ~50-100 GB/s) 时，推理吞吐瓶颈由显存带宽 (1008 G

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

CPU Offload 场景下，当 3GB 权重存储在 DDR4/DDR5 内存 (带宽 ~50-100 GB/s) 时，推理吞吐瓶颈由显存带宽 (1008 GB/s) 转为内存带宽，理论最大吞吐下降系数 k_offload = MemBW_DDR / MemBW_GDDR ≈ 0.05-0.1，即速度降至原来的 5-10%，交互体验极差。

## Corrected Claim

CPU Offload 场景下，当 3GB 权重存储在 DDR4/DDR5 内存 (带宽 ~50-100 GB/s) 时，推理吞吐瓶颈由显存带宽 (1008 GB/s) 转为内存带宽，理论最大吞吐下降系数 k_offload = MemBW_DDR / MemBW_GDDR ≈ 0.05-0.1，即速度降至原来的 5-10%，交互体验极差。

## Evidence

父节点级核验未通过：不完备（子节点1侧重于基于内存带宽的纯理论延迟量化，子节点2侧重于不同Offload策略（Streaming vs Persistent）的工程权衡，两者关注点不同，具有正交性。但父节点中提到的‘显存带宽转为内存带宽’这一核心机制转变（即为什么瓶颈会转移，以及GDDR与DDR带宽对比导致的k系数推导过程）在子节点中缺乏独立或明确的解释，子节点1直接给出了DDR带宽下的延迟，未涵盖父节点中关于‘瓶颈转移机制’和‘k系数定义’的逻辑层面，导致完备性不足。）
