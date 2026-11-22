# N106: RTX 5090 (Blackwell) 所需的 NVIDIA 驱动版本必须为 550+ 系列（支持 CUDA 12.8+），需确认该驱动版本是否已脱离 Bet

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25, N26, N27

## Claim

RTX 5090 (Blackwell) 所需的 NVIDIA 驱动版本必须为 550+ 系列（支持 CUDA 12.8+），需确认该驱动版本是否已脱离 Beta 阶段（通常以 'Production Branch' 标记为准），Beta 驱动的稳定性风险量化为：平均无故障时间（MTBF）比稳定版低约 20%（基于历史数据估计，需查 NVIDIA 官方文档）。

## Corrected Claim

RTX 5090 (Blackwell) 需要支持 CUDA 12.8+ 的 NVIDIA 驱动（通常为 550+ 系列），建议确认该驱动版本是否为 Production Branch 以规避 Beta 驱动的潜在稳定性风险。

## Evidence

[质询]MTBF 比稳定版低约 20% 的具体数值缺乏公开权威来源支持，属于经验估计而非官方数据；且驱动版本与 CUDA 版本的对应关系需具体查证，不能仅凭系列号断定。 | 来源 [1] 仅提及下载最新驱动，未提供具体版本号、CUDA 支持或 MTBF 数据，无法直接支持该陈述中的具体数值和版本要求。

## Search Query

NVIDIA driver 550 Blackwell RTX 5090 stable release status

## Retrieval Sources

- {'url': 'https://www.nvidia.com/en-us/geforce/drivers/&rut=67bd6c4d6d9f87f7625f8f36295cb52c7e45c17054f5230bfed5f15ede36606f', 'type': 'ddg', 'title': 'Download The Latest Official GeForce Drivers | NVIDIA'}
