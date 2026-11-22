# N158: 信息可信度 C_info 对 η 的乘数修正项：η_corrected = η_base * C_info。C_info 定义为买家对平台展示价格偏离度标签的信

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

信息可信度 C_info 对 η 的乘数修正项：η_corrected = η_base * C_info。C_info 定义为买家对平台展示价格偏离度标签的信任概率，受历史数据准确性影响。若平台历史数据误差率 E_err = 5%，则 C_info ≈ 1 - E_err = 0.95。需量化当 C_info < 0.8 时，η 是否低于 0.2 导致信号失效。

## Corrected Claim

信息可信度 C_info 对 η 的乘数修正项：η_corrected = η_base * C_info。C_info 定义为买家对平台展示价格偏离度标签的信任概率，受历史数据准确性影响。若平台历史数据误差率 E_err = 5%，则 C_info ≈ 1 - E_err = 0.95。需量化当 C_info < 0.8 时，η 是否低于 0.2 导致信号失效。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

information credibility coefficient trust calibration price display
