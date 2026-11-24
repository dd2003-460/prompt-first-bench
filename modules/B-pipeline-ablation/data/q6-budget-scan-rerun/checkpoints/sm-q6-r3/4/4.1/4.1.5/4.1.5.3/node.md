# N288: 核心城市聚集策略的缓存命中率影响：核心城市用户请求集中于Top-K热门内容，缓存命中率可达85%-95%；非核心城市用户请求分散，命中率降至60%-75%，整体

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

核心城市聚集策略的缓存命中率影响：核心城市用户请求集中于Top-K热门内容，缓存命中率可达85%-95%；非核心城市用户请求分散，命中率降至60%-75%，整体命中率 = (Core_Traffic * Core_Hit_Rate + Non_Core_Traffic * Non_Core_Hit_Rate) / Total_Traffic，需基于流量分布加权计算

## Corrected Claim

核心城市聚集策略的缓存命中率影响：核心城市用户请求集中于Top-K热门内容，缓存命中率可达85%-95%；非核心城市用户请求分散，命中率降至60%-75%，整体命中率 = (Core_Traffic * Core_Hit_Rate + Non_Core_Traffic * Non_Core_Hit_Rate) / Total_Traffic，需基于流量分布加权计算

## Evidence

先验知识/题面给定，逻辑校验通过
