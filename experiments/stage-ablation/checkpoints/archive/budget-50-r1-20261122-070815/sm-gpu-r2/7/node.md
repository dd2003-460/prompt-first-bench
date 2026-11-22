# N31: 消费级显卡候选集包括：RTX 4090 (24GB, 1008 GB/s, ~$1600-2000), RTX 4080 Super (16GB, 717 GB

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

消费级显卡候选集包括：RTX 4090 (24GB, 1008 GB/s, ~$1600-2000), RTX 4080 Super (16GB, 717 GB/s, ~$1000), RTX 3090 (24GB, 936 GB/s, ~$700-800 used), RTX A6000 (48GB, 768 GB/s, ~$4000-5000)；数据中心候选集包括：L40S (48GB, 864 GB/s, ~$8000), A100 80GB (80GB, 2039 GB/s, ~$10000-15000 used), H100 80GB (80GB, 3350 GB/s, ~$25000-30000)

## Corrected Claim

消费级显卡候选集包括：RTX 4090 (24GB, 1008 GB/s, ~$1600-2000)；其他显卡（RTX 4080 Super, RTX 3090, RTX A6000）及数据中心显卡（L40S, A100, H100）的规格与价格需进一步核实。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点与父节点中列出的7个具体GPU型号一一对应，覆盖了所有候选项。每个子节点独立分析了该特定硬件在目标模型（Qwen3-27B）下的显存占用、带宽瓶颈及性价比，内容互不重叠且无逻辑矛盾。虽然所有子节点都基于相同的模型参数进行计算，但这属于针对特定硬件实例化的必要分析，而非冗余的参数罗列。）

## Retrieval Sources

- {'url': 'https://detail.zol.com.cn/vga/s10074/&rut=db6edb4911e373f1bffcc789d2ee596bda7868c9fea0782a6247911248cf98c7', 'type': 'ddg', 'title': '【Rtx 4090显卡】Rtx 4090显卡报价及图片大全-zol中关村在线'}
- {'url': 'https://www.gpuxianka.com/desktop-cards/nvidia/rtx-4090-index.html&rut=589328523ca07ec6f892ca6e407ff5af4f6b558bfa50b0b75975e2a79fe67052', 'type': 'ddg', 'title': 'NVIDIA GeForce RTX 4090 24GB GDDR6X 参数评测_性能天梯排名_显卡综合概述 - GPU显卡库'}
