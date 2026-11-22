# N57: A100 40GB SXM4 显存带宽为 1555 GB/s，A100 80GB SXM4 为 2039 GB/s，H100 80GB SXM5 为 3350 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

A100 40GB SXM4 显存带宽为 1555 GB/s，A100 80GB SXM4 为 2039 GB/s，H100 80GB SXM5 为 3350 GB/s，L40S 48GB PCIe 为 864 GB/s，A6000 48GB PCIe 为 768 GB/s，来源：NVIDIA官方规格表 [verified]

## Corrected Claim

A100 40GB SXM4 显存带宽为 1555 GB/s，A100 80GB SXM4 为 2039 GB/s，H100 80GB SXM5 为 3350 GB/s，L40S 48GB PCIe 为 864 GB/s，A6000 48GB PCIe 为 768 GB/s，来源：NVIDIA官方规格表 [verified]

## Evidence

父节点级核验未通过：有冗余（子节点虽然针对不同的硬件型号，但其核心逻辑完全相同（均为：带宽 / 固定模型大小 = 吞吐量），且所有子节点都重复了相同的计算前提（Qwen3-27B, BF16, 54.6GB）。这构成了典型的“同构重复”，即多个子节点本质上是同一公式在不同参数下的实例化，而非独立的知识维度。）
