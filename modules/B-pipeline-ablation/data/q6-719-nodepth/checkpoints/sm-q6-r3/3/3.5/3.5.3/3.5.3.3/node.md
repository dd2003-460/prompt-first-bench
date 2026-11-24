# N266: 核心 POP 满载后的溢出流量成本 Cost_Overflow_Hybrid = Max(0, Core_Traffic - Core_Capacity) × 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N92

## Claim

核心 POP 满载后的溢出流量成本 Cost_Overflow_Hybrid = Max(0, Core_Traffic - Core_Capacity) × Unit_Price_Cloud，该成本项在混合策略中作为非线性惩罚项加入总成本函数，确保核心 POP 容量规划与公有云回源成本之间的权衡

## Corrected Claim

核心 POP 满载后的溢出流量成本 Cost_Overflow_Hybrid = Max(0, Core_Traffic - Core_Capacity) × Unit_Price_Cloud，该成本项在混合策略中作为非线性惩罚项加入总成本函数，确保核心 POP 容量规划与公有云回源成本之间的权衡

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

hybrid CDN overflow traffic cost to public cloud
