# N58: A100 40GB SXM4 TDP为400W，A100 80GB SXM4 为400W，H100 80GB SXM5 为700W，L40S 48GB PCIe

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

A100 40GB SXM4 TDP为400W，A100 80GB SXM4 为400W，H100 80GB SXM5 为700W，L40S 48GB PCIe 为350W，A6000 48GB PCIe 为300W，来源：NVIDIA官方规格表 [verified]

## Corrected Claim

A100 40GB SXM4 TDP为400W，A100 80GB SXM4 为400W，H100 80GB SXM5 为700W，L40S 48GB PCIe 为350W，A6000 48GB PCIe 为300W，来源：NVIDIA官方规格表 [verified]

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 冗余性：三个子节点本质上是同一个计算公式（电力成本估算）在不同GPU型号上的实例化，属于同一逻辑维度的不同取值，而非独立的知识维度，应压缩为一个包含参数表的节点。2. 完备性：父节点明确列出了5款GPU（A100 40GB, A100 80GB, H100, L40S, A6000），但子节点仅覆盖了其中3款（A100 40GB, H100, L40S），遗漏了A100 80GB和A6000，导致信息覆盖不全。）
