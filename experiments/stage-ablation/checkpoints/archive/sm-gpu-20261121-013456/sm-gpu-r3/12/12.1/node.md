# N294: RTX 5090 官方 MSRP 为 $1999，显存规格为 32GB GDDR7，显存带宽 1792 GB/s，支持原生 FP4 和 INT4 加速（Blac

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N123

## Claim

RTX 5090 官方 MSRP 为 $1999，显存规格为 32GB GDDR7，显存带宽 1792 GB/s，支持原生 FP4 和 INT4 加速（Blackwell 架构特性）。

## Corrected Claim

RTX 5090 显存规格为 32GB GDDR7，显存带宽约 1792 GB/s，基于 Blackwell 架构，支持 FP4/INT4 加速；官方 MSRP 通常为 $1999（需进一步来源确认）。

## Evidence

[质询]显存带宽数值存在细微偏差：根据来源[1]提供的 28 Gbps 有效速率和 512-bit 接口计算，理论带宽应为 1792 GB/s，但部分官方或媒体资料常标注为 1792 GB/s 或近似值，此处主要风险在于 FP4/INT4 支持虽为 Blackwell 特性，但具体‘原生加速’的表述在不同语境下（如是否指硬件单元直接支持 vs 软件优化）可能存在解读差异，且 MSRP 未在提供的摘要中直接列出，需依赖外部常识或更详细来源确认。 | 来源[1]和[2]直接支持 32GB GDDR7 显存和 Blackwell 架构；带宽 1792 GB/s 可由 28 Gbps * 512 / 8 推导得出，逻辑自洽；但 MSRP $1999 未在提供的摘要文本中明确出现，属于经验事实且缺乏直接来源支持，故降级。

## Search Query

NVIDIA RTX 5090 official specifications 32GB GDDR7 1792 GB/s FP4 support

## Retrieval Sources

- {'url': 'https://www.techpowerup.com/gpu-specs/geforce-rtx-5090.c4216&rut=0805989be3efe396818ff83fb297b42459bc0d1abfd8d295ec5ade8d8b6191fb', 'type': 'ddg', 'title': 'NVIDIA GeForce RTX 5090 Specs | TechPowerUp GPU Database'}
- {'url': 'https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/&rut=a11ece31eb6c4de74732c323577b537d8cfb33cfb24e0f367ee8c99420a152bf', 'type': 'ddg', 'title': 'GeForce RTX 5090 Graphics Cards | NVIDIA'}
