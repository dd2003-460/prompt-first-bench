# N157: 用户体验损失系数k_penalty的量化推导：k_penalty = (ΔRevenue_per_ms / ARPU_daily)，其中ΔRevenue_per

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N49

## Claim

用户体验损失系数k_penalty的量化推导：k_penalty = (ΔRevenue_per_ms / ARPU_daily)，其中ΔRevenue_per_ms需通过A/B测试或回归分析获得，典型电商/内容平台每增加100ms延迟导致转化率下降约1-5%，ARPU_daily为每用户日均贡献收入（约¥0.5-2），从而将定性流失转化为货币化成本

## Corrected Claim

用户体验损失系数k_penalty的量化推导：k_penalty = (ΔRevenue_per_ms / ARPU_daily)，其中ΔRevenue_per_ms需通过A/B测试或回归分析获得，典型电商/内容平台每增加100ms延迟导致转化率下降约1-5%，ARPU_daily为每用户日均贡献收入（约¥0.5-2），从而将定性流失转化为货币化成本

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

latency impact conversion rate revenue per 100ms A/B test
