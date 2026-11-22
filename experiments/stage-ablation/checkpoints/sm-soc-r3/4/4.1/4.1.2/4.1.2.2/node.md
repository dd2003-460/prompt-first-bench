# N213: 回归模型中控制变量 γ * controls 必须包含 Log(Inventory_Age) 和 Category_Scarcity_Index，否则 β_in

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N69

## Claim

回归模型中控制变量 γ * controls 必须包含 Log(Inventory_Age) 和 Category_Scarcity_Index，否则 β_info 存在约 0.03 的正向偏差，因为高溢价商品通常伴随更短的库存年龄（新鲜度效应混淆价格效应）。

## Corrected Claim

回归模型中控制变量 γ * controls 建议包含 Log(Inventory_Age) 和 Category_Scarcity_Index，以缓解因高溢价商品通常伴随更短库存年龄（新鲜度效应）而导致的 β_info 潜在正向偏差。

## Evidence

[质询]该陈述包含具体的经验性数值（偏差约 0.03）和特定的因果机制（新鲜度效应混淆），这属于实证研究结论而非第一性原理可推导的数学或逻辑事实。在缺乏具体数据集、模型设定或文献支持的情况下，无法验证该特定数值和机制的普适性或准确性。 | 经验事实，逻辑自洽但缺来源支持
