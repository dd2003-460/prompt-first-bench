# N11: 内存带宽瓶颈量化：生成速度 (tokens/s) ≈ 内存带宽 (GB/s) / (模型大小 (GB) + KV Cache 增量 (GB))，例如 24GB 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

内存带宽瓶颈量化：生成速度 (tokens/s) ≈ 内存带宽 (GB/s) / (模型大小 (GB) + KV Cache 增量 (GB))，例如 24GB 显存卡若带宽 900GB/s，理论上限约为 900/56 ≈ 16 tokens/s (BF16)。

## Corrected Claim

内存带宽瓶颈量化：生成速度 (tokens/s) ≈ 内存带宽 (GB/s) / (模型大小 (GB) + KV Cache 增量 (GB))，例如 24GB 显存卡若带宽 900GB/s，理论上限约为 900/56 ≈ 16 tokens/s (BF16)。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别量化了公式分母中的两个主要组成部分（权重加载量、KV Cache 读写量）以及公式整体的效率修正因子（η）。三者分别对应公式的不同变量或修正项，逻辑上正交且无重复。虽然KV Cache的计算细节略显复杂，但作为独立量化项是合理的。）
