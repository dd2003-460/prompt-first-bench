# N242: 核心 POP 缓存未命中回源优化成本 Origin_Fetch_Optimization_Cost = (Core_Monthly_Traffic_GB × (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

核心 POP 缓存未命中回源优化成本 Origin_Fetch_Optimization_Cost = (Core_Monthly_Traffic_GB × (1 - Hit_Rate_Core)) × Unit_Price_Origin_Fetch_GB × Optimization_Factor，其中 Hit_Rate_Core 为核心 POP 缓存命中率（通常 80%-95%），Optimization_Factor 为优化措施（如预热、智能路由）带来的成本降低系数（0.5-0.8），需与 N152 的公有云回源成本对比。

## Corrected Claim

核心 POP 缓存未命中回源优化成本 Origin_Fetch_Optimization_Cost = (Core_Monthly_Traffic_GB × (1 - Hit_Rate_Core)) × Unit_Price_Origin_Fetch_GB × Optimization_Factor，其中 Hit_Rate_Core 为核心 POP 缓存命中率（通常 80%-95%），Optimization_Factor 为优化措施（如预热、智能路由）带来的成本降低系数（0.5-0.8），需与 N152 的公有云回源成本对比。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（流量×单价=成本），参数范围（命中率80-95%，优化系数0.5-0.8）符合CDN行业常规经验值，逻辑自洽。

## Search Query

CDN cache miss origin fetch optimization cost reduction factor preheating smart routing
