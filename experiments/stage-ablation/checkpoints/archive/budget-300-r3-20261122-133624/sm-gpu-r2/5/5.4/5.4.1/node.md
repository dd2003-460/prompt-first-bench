# N151: 硬件成本项 C_hw 的折旧模型：采用直线折旧法，残值率设为 10%（基于二手市场 3 年折价率），即 C_hw_depreciated = C_hw_purc

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

硬件成本项 C_hw 的折旧模型：采用直线折旧法，残值率设为 10%（基于二手市场 3 年折价率），即 C_hw_depreciated = C_hw_purchase * (1 - 0.10 * (t/3))，其中 t 为使用年限；对于二手卡（如 3090），需额外计入 5-10% 的溢价风险以覆盖潜在故障更换成本。

## Corrected Claim

硬件成本项 C_hw 的折旧模型：采用直线折旧法，残值率设为 10%（基于二手市场 3 年折价率），即 C_hw_depreciated = C_hw_purchase * (1 - 0.10 * (t/3))，其中 t 为使用年限；对于二手卡（如 3090），需额外计入 5-10% 的溢价风险以覆盖潜在故障更换成本。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU depreciation rate 3 year straight line residual value
