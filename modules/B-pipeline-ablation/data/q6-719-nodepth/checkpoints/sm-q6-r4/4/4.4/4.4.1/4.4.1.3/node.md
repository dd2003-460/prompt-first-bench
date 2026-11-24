# N289: SOC_Integration_Fee = Log_Volume_GB_Month × Ingestion_Price + Alert_Volume × Ana

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

SOC_Integration_Fee = Log_Volume_GB_Month × Ingestion_Price + Alert_Volume × Analysis_Price，其中 Log_Volume_GB_Month 估算为 Daily_Traffic_2TB × 0.05 (日志占比) × 30 = 3TB/月，Ingestion_Price 典型值为 ¥0.1-0.5/GB，Alert_Volume 取决于误报率。

## Corrected Claim

SOC_Integration_Fee = Log_Volume_GB_Month × Ingestion_Price + Alert_Volume × Analysis_Price，其中 Log_Volume_GB_Month 估算为 Daily_Traffic_2TB × 0.05 (日志占比) × 30 = 3TB/月，Ingestion_Price 典型值为 ¥0.1-0.5/GB，Alert_Volume 取决于误报率。

## Evidence

先验知识/题面给定，逻辑校验通过：费用公式结构符合云监控/日志服务通用计费模型（存储/摄入+分析），数值量级（2TB流量5%日志占比约3TB/月，单价0.1-0.5元/GB）在工程实践中合理且自洽。

## Search Query

SOC SIEM log ingestion cost per GB pricing
