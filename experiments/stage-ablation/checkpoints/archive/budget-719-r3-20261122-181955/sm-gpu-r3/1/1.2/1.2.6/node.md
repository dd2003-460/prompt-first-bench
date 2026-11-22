# N50: A100/H100 SXM 多卡互联带宽为 NVLink 600 GB/s (A100) 或 900 GB/s (H100)，PCIe 版本为 64 GB/s 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

A100/H100 SXM 多卡互联带宽为 NVLink 600 GB/s (A100) 或 900 GB/s (H100)，PCIe 版本为 64 GB/s (PCIe 4.0 x16)

## Corrected Claim

A100/H100 SXM 多卡互联带宽为 NVLink 600 GB/s (A100) 或 900 GB/s (H100)，PCIe 版本为 64 GB/s (PCIe 4.0 x16)

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 完备性缺失：父节点明确包含 A100 和 H100 两种硬件的互联带宽，但子节点仅计算了 A100 的数据量（子节点1），虽然子节点3使用了该数据量计算 H100 的时间，但缺乏对 H100 数据量是否一致或不同（若模型架构不同）的说明，且未涵盖 PCIe 在 H100 上的对比。2. 冗余性严重：子节点2和子节点3本质上是同一公式（Time = Data/Bandwidth）在不同带宽参数下的计算，属于参数化差异，而非独立的逻辑分支，应合并或抽象为通用公式。3. 正交性尚可但逻辑耦合：子节点4依赖于子节点2的计算结果，虽不矛盾，但层级上属于应用层分析，与前三个纯硬件/理论计算层略有混杂，不过主要问题在于冗余和完备性。）
