# N671: Seagate Exos 16E 在 Spin-down 状态下的功耗并非恒定，而是随盘体温度（Ambient Temp）变化，在 25°C 环境下典型值为 0

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N278, N279, N280

## Claim

Seagate Exos 16E 在 Spin-down 状态下的功耗并非恒定，而是随盘体温度（Ambient Temp）变化，在 25°C 环境下典型值为 0.5W，但在 40°C 高温环境下可能升至 1.0W，需根据数据中心实际环境温度选取保守值 1.0W 进行 TCO 计算。

## Corrected Claim

Seagate Exos 16E 在 Spin-down 状态下的功耗随盘体温度变化，通常建议在高温环境下选取较高保守值进行 TCO 计算，具体数值需查阅官方最新规格书确认。

## Evidence

[质询]具体数值（25°C下0.5W，40°C下1.0W）及温度敏感性曲线属于特定硬件的经验数据，缺乏公开权威来源直接佐证，且不同批次或固件版本可能存在差异。 | 经验事实，逻辑自洽（功耗随温度升高而增加符合物理直觉，TCO计算取保守值合理）但缺来源支持。

## Search Query

Seagate Exos 16E datasheet power consumption spin down temperature dependency
