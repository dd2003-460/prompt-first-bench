# N109: NVIDIA A100 80GB SXM4 的 2024-05 至 2024-11 期间云租赁折算月成本约为 $2,500-$3,500/卡，或一次性采购价 $

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

NVIDIA A100 80GB SXM4 的 2024-05 至 2024-11 期间云租赁折算月成本约为 $2,500-$3,500/卡，或一次性采购价 $14,000-$18,000，受供应链影响波动 ±20%。

## Corrected Claim

NVIDIA A100 80GB 在 2024 年期间的云租赁月成本量级约为 $2,000-$4,000/卡（取决于具体云厂商和实例类型），具体 SXM4 版本及采购价需参考特定供应链数据。

## Evidence

[质询]来源主要覆盖 PCIe 版本或通用 A100 租赁价格，未明确区分 SXM4 与 PCIe 版本的价差，且未提供 2024 年 5-11 月特定时间段的采购价数据，存在口径混淆风险。 | 来源 [1][2][3] 提供了 A100 80GB 的每小时租赁价格（如 $0.27-$1.5/hr 不等），经计算月成本量级与陈述相符，但缺乏针对 SXM4 特定型号及 2024 下半年采购价的直接证据，属于间接支持。

## Search Query

NVIDIA A100 80GB price 2024 cloud cost per hour

## Retrieval Sources

- {'url': 'https://rentgpu.org/gpus/nvidia-a100-80gb-pcie/cloud-instances&rut=8f3bac95958dd1b4610f59ef25c5e260211e42c37760d4270d1483a6a4b5a102', 'type': 'ddg', 'title': 'Nvidia A100 80GB PCIe cloud instances — hyperscaler pricing comparison ...'}
- {'url': 'https://fastgpu.co/gpus/a100-80gb&rut=cc97e8c51e29719c14085b202843d8e1bb88b724949e4b6818c416a22eb63788', 'type': 'ddg', 'title': 'A100 80GB cloud pricing and rental cost per hour | FastGPU'}
- {'url': 'https://gpucompare.cloud/gpu/nvidia-a100/&rut=a9a8bd2fc26588b7dbcb4fb750120787395334e3a5eba3fc40290039d1c43494', 'type': 'ddg', 'title': 'Rent NVIDIA A100 Cloud GPU - Compare Prices from $0.27/hr | GPUCompare ...'}
