# N226: 基准曝光量 (Impressions_base) 的确定需控制季节性波动，采用同期对照组或时间序列分解（STL）提取的基线值，公式为 Base = Trend_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

基准曝光量 (Impressions_base) 的确定需控制季节性波动，采用同期对照组或时间序列分解（STL）提取的基线值，公式为 Base = Trend_t + Seasonal_t，以消除自然流量波动对 PU 计算的干扰。

## Corrected Claim

基准曝光量 (Impressions_base) 的确定需控制季节性波动，采用同期对照组或时间序列分解（STL）提取的基线值，公式为 Base = Trend_t + Seasonal_t，以消除自然流量波动对 PU 计算的干扰。

## Evidence

先验知识/题面给定，逻辑校验通过
