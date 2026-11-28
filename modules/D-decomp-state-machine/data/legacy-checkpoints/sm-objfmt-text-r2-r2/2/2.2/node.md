# N13: 数据中心级 GPU 候选集包括 NVIDIA A100 (80GB HBM2e), H100 (80GB HBM3), L40S (48GB GDDR6) 和 

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

数据中心级 GPU 候选集包括 NVIDIA A100 (80GB HBM2e), H100 (80GB HBM3), L40S (48GB GDDR6) 和 AMD MI250X (128GB HBM2e)，需记录其租赁/购买成本及显存带宽，特别关注 L40S 的高显存容量与中等算力的平衡

## Corrected Claim

数据中心级 GPU 候选集包括 NVIDIA A100 (80GB HBM2e), H100 (80GB HBM3), L40S (48GB GDDR6) 和 AMD MI250X (128GB HBM2e)，需记录其租赁/购买成本及显存带宽；其中 L40S 以 48GB 显存和较高的能效比见长，适合特定推理场景，而非单纯追求最大显存容量。

## Evidence

父节点级核验未通过：不完备（1. 正交性良好：四个子节点分别对应四款不同的硬件，彼此独立且无逻辑矛盾。2. 完备性不足：父节点明确包含“数据中心级”限定，而子节点中包含了 NVIDIA L40S。L40S 主要面向图形渲染、推理及边缘计算，其显存类型为 GDDR6 而非 HBM，且缺乏 NVLink 等数据中心核心特性，通常不被归类为典型的数据中心训练/高性能推理 GPU（如 A100/H100/MI250X）。将其列入“数据中心级候选集”存在范畴偏差。此外，父节点提到的“高显存容量”描述不准确，L40S 的 48GB 显存小于 A100/H100 的 80GB，仅在特定低精度场景下具有性价比优势，而非“高容量”。3. 无冗余：各节点代表不同硬件实体，不可合并。）

## Search Query

A100 H100 L40S MI250X price bandwidth specs datacenter

## Retrieval Sources

- {'url': 'https://www.nvidia.com/en-us/data-center/a100/&rut=f29699becd1c61aa0280aa913bbcd0bf012ed16b30b9170501e5560abd23a25e', 'type': 'ddg', 'title': 'NVIDIA A100 Tensor Core GPU'}
- {'url': 'https://zhuanlan.zhihu.com/p/1910731560015077860&rut=75b090975508e03909130207961052f70cd43111267eea3b044fef2fea24fdfe', 'type': 'ddg', 'title': 'Nvidia Gpu芯片：A100、H100、A800、H800、H20的差异'}
