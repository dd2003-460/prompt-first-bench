# N287: HDD 单盘功耗分解：典型 16TB 企业级 HDD（如 Seagate Exos 16E）平均功耗约 8-9W（读写混合负载），待机功耗约 5W；假设 24/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

HDD 单盘功耗分解：典型 16TB 企业级 HDD（如 Seagate Exos 16E）平均功耗约 8-9W（读写混合负载），待机功耗约 5W；假设 24/7 运行，平均功耗取 8.5W，则单盘年功耗 = 8.5W * 24h * 365d = 74,460 Wh = 74.46 kWh。

## Corrected Claim

HDD 单盘功耗分解：典型 16TB 企业级 HDD（如 Seagate Exos 16E）平均功耗约 8-9W（读写混合负载），待机功耗约 5W；假设 24/7 运行，平均功耗取 8.5W，则单盘年功耗 = 8.5W * 24h * 365d = 74,460 Wh = 74.46 kWh。

## Evidence

先验知识/题面给定，逻辑校验通过：Seagate Exos 16E 等 16TB 企业级硬盘平均功耗确实在 8-9W 区间，待机约 5W，计算过程 8.5 * 24 * 365 = 74460 Wh 准确无误。

## Search Query

Seagate Exos 16E power consumption watts
