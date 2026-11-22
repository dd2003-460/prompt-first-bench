# N90: 选择效应量化：假设平台对降价卖家给予流量权重加成 w_boost，低质商品（定义：退货率>10%或描述不符投诉率>5%）在推荐池中的占比变化 ΔShare_lo

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N24

## Claim

选择效应量化：假设平台对降价卖家给予流量权重加成 w_boost，低质商品（定义：退货率>10%或描述不符投诉率>5%）在推荐池中的占比变化 ΔShare_low = (Share_low_post - Share_low_pre)，其中 Share_low_pre 需基于历史数据估算（[待核验]，预估基线 5-15%）。

## Corrected Claim

选择效应量化：假设平台对降价卖家给予流量权重加成 w_boost，低质商品（定义：退货率>10%或描述不符投诉率>5%）在推荐池中的占比变化 ΔShare_low = (Share_low_post - Share_low_pre)，其中 Share_low_pre 需基于历史数据估算（具体基线值需根据实际平台数据确定，此处暂缺可靠参考）。

## Evidence

[质询]该陈述包含具体的经验性数值基线（5-15%），属于经验事实，无法从第一性原理推导，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

marketplace platform recommendation bias low quality sellers traffic boost adverse selection rate
