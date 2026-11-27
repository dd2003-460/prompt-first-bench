# N211: 在ρ=-0.3（热小冷大）且β=0.9条件下，LFU因更倾向于保留高频小对象，其字节命中率提升量δ_ρ的蒙特卡洛模拟估计值约为0.5-1.0个百分点，该值显著低

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

在ρ=-0.3（热小冷大）且β=0.9条件下，LFU因更倾向于保留高频小对象，其字节命中率提升量δ_ρ的蒙特卡洛模拟估计值约为0.5-1.0个百分点，该值显著低于独立假设(ρ=0)下的提升量，表明负相关削弱了LFU的频率-大小协同优势。

## Corrected Claim

在ρ=-0.3（热小冷大）且β=0.9条件下，LFU因更倾向于保留高频小对象，其字节命中率提升量δ_ρ预计低于独立假设(ρ=0)下的提升量，表明负相关削弱了LFU的频率-大小协同优势。

## Evidence

[质询]该陈述包含具体的蒙特卡洛模拟数值范围（0.5-1.0个百分点），属于经验事实/模拟结果，无法从第一性原理直接推导，且缺乏来源支持以确认该特定参数组合下的具体数值量级。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LFU vs LRU byte hit rate improvement Pareto distribution negative correlation size frequency simulation
