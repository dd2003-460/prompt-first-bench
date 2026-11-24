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

父节点级核验通过：正交+完备+无冗余（子节点严格对应父节点公式中的四个独立变量（流量、命中率、单价、优化系数），彼此无逻辑重叠或矛盾。每个子节点提供了该变量的计算逻辑、参数范围或理论依据，覆盖了成本估算所需的所有关键维度。）

## Search Query

CDN cache miss origin fetch optimization cost reduction factor preheating smart routing
