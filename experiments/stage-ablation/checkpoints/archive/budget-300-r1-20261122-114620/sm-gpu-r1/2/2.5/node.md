# N16: 数据中心级 GPU 价格基准：A100 40GB ≈ $10000, A100 80GB ≈ $15000, H100 80GB ≈ $25000-30000,

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

数据中心级 GPU 价格基准：A100 40GB ≈ $10000, A100 80GB ≈ $15000, H100 80GB ≈ $25000-30000, L40S 48GB ≈ $8000, AMD MI250X ≈ $15000

## Corrected Claim

数据中心级 GPU 硬件采购价格基准（估算）：A100 40GB 约 $10000, A100 80GB 约 $15000, H100 80GB 约 $25000-30000, L40S 48GB 约 $8000, AMD MI250X 约 $15000（注：具体价格随市场波动，此处为典型量级参考）

## Evidence

[质询]参考来源仅提供了GPU的租赁价格（每小时/每月），而非硬件采购价格（Capex）。虽然租赁价格与硬件成本存在相关性，但直接断言具体的硬件采购价格（如A100 40GB ≈ $10000）缺乏来源直接支持，且不同时期、不同渠道的硬件价格波动较大，存在口径混淆（租赁vs采购）的风险。 | 来源[1][2][3]仅涉及A100的租赁价格（$0.45/hr - $2.52/hr），未提供硬件采购价格数据，无法直接支持claim中的具体美元数值；但根据行业常识，A100/H100等高端GPU的硬件价格量级（$10k-$30k）符合逻辑直觉，属于经验事实，逻辑自洽但缺来源直接支持。

## Search Query

NVIDIA A100 H100 L40S AMD MI250X price 2024

## Retrieval Sources

- {'url': 'https://computeprices.com/gpus/a100pcie&rut=7d90cd2d7905f50267db069925e237fe5844b92df79c6b453e7609c76a9b6e68', 'type': 'ddg', 'title': 'A100 PCIe 40GB GPU Price: $0.45/hr | Compare 14+ Providers'}
- {'url': 'https://www.thundercompute.com/blog/nvidia-a100-pricing&rut=897fe2427e444230446cef505b7337e19b8c1752142669518fd797b8b5834e6a', 'type': 'ddg', 'title': 'NVIDIA A100 Pricing (November 2026): Cheapest On-demand GPU Instances'}
- {'url': 'https://computeindex.net/gpu/a100-40g&rut=8f71c3b31818b6a4e4a669fcf5c5597722ffca7a1d81ce6e1d520767f27dcef8', 'type': 'ddg', 'title': 'Nvidia A100 40gb租赁价格 2026 | 时租$2.52/月租$1,179'}
