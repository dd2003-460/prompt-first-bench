# N48: NVIDIA A100 SXM4 的精确规格为：80GB HBM2e, 内存带宽 2.0TB/s, TDP 400W, 不支持原生 FP8 (仅 BF16/IN

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

NVIDIA A100 SXM4 的精确规格为：80GB HBM2e, 内存带宽 2.0TB/s, TDP 400W, 不支持原生 FP8 (仅 BF16/INT8), 单卡价格区间 $10,000-$15,000 (2024 Q3 市场价)

## Corrected Claim

NVIDIA A100 SXM4 的精确规格为：80GB HBM2e, 内存带宽约2.0TB/s, TDP 400W, 不支持原生 FP8 (仅 BF16/INT8), 单卡价格随市场波动（2024 Q3 具体价格需实时查询，参考区间可能不准确）

## Evidence

[质询]单卡价格区间 $10,000-$15,000 (2024 Q3 市场价) 属于经验事实，且该价格区间在2024年Q3对于A100 80GB SXM4而言可能偏低（通常二手或现货价格波动较大，且SXM4版本通常高于PCIe版本，需具体市场数据支持），参考来源未提供价格信息。 | 来源[1]直接支持80GB HBM2e规格，但内存带宽2.0TB/s需通过5120-bit * 3.2Gbps * 2 (DDR) 计算得出约2.048TB/s，逻辑自洽；TDP 400W和FP8支持情况（A100确实不支持原生FP8，仅支持BF16/INT8等）符合已知技术事实；但价格部分缺乏来源支持，且为经验事实，故降级。

## Search Query

NVIDIA A100 SXM4 specifications price 2024

## Retrieval Sources

- {'url': 'https://www.techpowerup.com/gpu-specs/a100-sxm4-80-gb.c3746&rut=41109bc35c9c31bf03bfcbbd499d7c98d4d784ae05ad4a52200d89cf287d4dca', 'type': 'ddg', 'title': 'NVIDIA A100 SXM4 80 GB Specs | TechPowerUp GPU Database'}
