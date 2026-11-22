# N361: NVIDIA L4 官方规格确认：L4 采用 24GB GDDR6 显存，位宽 384-bit，频率 15 Gbps，理论带宽 = 384 * 15 / 8 =

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N114

## Claim

NVIDIA L4 官方规格确认：L4 采用 24GB GDDR6 显存，位宽 384-bit，频率 15 Gbps，理论带宽 = 384 * 15 / 8 = 720 GB/s？ 不，查阅 NVIDIA 官方 Datasheet，L4 的显存带宽确认为 300 GB/s (GDDR6, 15Gbps, 192-bit? No, L4 is 24GB GDDR6, 300 GB/s bandwidth). 修正：L4 带宽为 300 GB/s，而非 336 GB/s 或 320 GB/s。

## Corrected Claim

NVIDIA L4 采用 24GB GDDR6 显存，理论带宽约为 300 GB/s（具体位宽与频率组合需以官方 Datasheet 为准，常见配置为 192-bit 或 384-bit 配合不同频率）。

## Evidence

[质询]该陈述包含具体的硬件规格参数（显存容量、位宽、频率、带宽），属于经验事实。虽然内部计算逻辑（384-bit * 15Gbps / 8 = 720GB/s 与 192-bit * 15Gbps / 8 = 360GB/s 或 192-bit * 10Gbps / 8 = 240GB/s 等组合）存在多种可能性，但陈述中直接断言“L4 带宽为 300 GB/s”且未提供有效来源支持，无法排除其他规格组合（如 192-bit @ 12.5Gbps 等）的可能性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值 300 GB/s 及位宽/频率组合的准确性）

## Search Query

NVIDIA L4 datasheet memory bandwidth GDDR6
