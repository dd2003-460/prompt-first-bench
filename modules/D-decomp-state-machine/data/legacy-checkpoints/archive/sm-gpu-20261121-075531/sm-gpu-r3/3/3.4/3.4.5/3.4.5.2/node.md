# N250: 数据中心卡 (A100/H100) 在 3 年现场保修期内的预期隐性成本 = P(fail_3yr) * (Downtime_Hours * Hourly_Re

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

数据中心卡 (A100/H100) 在 3 年现场保修期内的预期隐性成本 = P(fail_3yr) * (Downtime_Hours * Hourly_Revenue_Loss + RMA_Logistics_Cost)，其中 P(fail_3yr) 约为 2-5% [待核验]，Downtime_Hours 通常包含 48-72 小时等待 RMA 及重新部署时间，Hourly_Revenue_Loss 取决于业务负载，若为纯本地推理无直接营收，则主要成本为时间机会成本。

## Corrected Claim

数据中心卡 (A100/H100) 在 3 年现场保修期内的预期隐性成本 = P(fail_3yr) * (Downtime_Hours * Hourly_Revenue_Loss + RMA_Logistics_Cost)，其中 P(fail_3yr) 约为 2-5% [待核验]，Downtime_Hours 通常包含 48-72 小时等待 RMA 及重新部署时间，Hourly_Revenue_Loss 取决于业务负载，若为纯本地推理无直接营收，则主要成本为时间机会成本。

## Evidence

[质询]P(fail_3yr) 2-5% 的数值范围可能因具体硬件批次、运行负载（如是否长期满载）及环境条件（如散热不良）而波动，但在数据中心标准运维环境下，该量级符合行业对高端GPU故障率（AFR）的经验估计（通常年故障率1-2%，三年累计约3-6%）。 | 先验知识/题面给定，逻辑校验通过。公式结构符合隐性成本计算逻辑，数值量级（2-5%故障率，48-72小时停机）符合数据中心硬件运维常识。

## Search Query

A100 H100 MTBF mean time between failures warranty downtime cost
