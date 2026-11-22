# N9: NVIDIA H100 SXM5单卡显存为80 GB HBM3，H100 PCIe为80 GB HBM2e，A100为80 GB HBM2e，L40S为48 G

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

NVIDIA H100 SXM5单卡显存为80 GB HBM3，H100 PCIe为80 GB HBM2e，A100为80 GB HBM2e，L40S为48 GB GDDR6，RTX 4090为24 GB GDDR6X，RTX 3090为24 GB GDDR6X，这些是候选硬件的显存容量硬指标

## Corrected Claim

NVIDIA H100 SXM5单卡显存为80 GB HBM3，H100 PCIe为80 GB HBM2e，A100为80 GB HBM2e，L40S为48 GB GDDR6，RTX 4090为24 GB GDDR6X，RTX 3090为24 GB GDDR6X，这些是候选硬件的显存容量硬指标

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 完备性失败：父节点明确列出了H100、A100、L40S、RTX 4090、RTX 3090等具体硬件及其显存规格，但子节点仅包含H200和RTX 5090，完全丢失了父节点中的核心数据，未覆盖父节点的关键方面。2. 冗余性高：父节点和子节点本质上都是‘硬件型号 -> 显存容量/类型’的键值对映射，属于同一参数的不同取值，应合并为一个统一的硬件规格表或参数列表，而非拆分为互斥的子节点。）

## Search Query

NVIDIA H100 A100 L40S RTX 4090 3090 VRAM capacity
