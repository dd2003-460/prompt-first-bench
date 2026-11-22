# N19: ‘最小干预’策略的负面外部性量化：若干预为‘强制显示近期成交均价’，对卖家伤害度 H_seller = ΔPrice * Q / Revenue，预估 H_se

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

‘最小干预’策略的负面外部性量化：若干预为‘强制显示近期成交均价’，对卖家伤害度 H_seller = ΔPrice * Q / Revenue，预估 H_seller ∈ [0.1, 0.3]；对买家伤害度 H_buyer ≈ 0（信息透明降低搜索成本）；对平台伤害度 H_platform = ΔGMV * TakeRate，预估 H_platform ∈ [-0.05, 0.05]（中性或微正）[待核验：需具体价格弹性系数 ε ≈ -1.5]

## Corrected Claim

‘最小干预’策略的负面外部性量化框架：若干预为‘强制显示近期成交均价’，对卖家伤害度 H_seller 定义为 ΔPrice * Q / Revenue，其具体数值取决于价格弹性系数 ε（通常 ε < -1）；对买家伤害度 H_buyer 趋近于 0（信息透明降低搜索成本）；对平台伤害度 H_platform 定义为 ΔGMV * TakeRate，通常表现为中性或微正。具体数值区间需基于特定市场的实证数据估算。

## Evidence

[质询]该陈述包含具体的经验性数值区间（H_seller ∈ [0.1, 0.3] 等）和假设的价格弹性系数（ε ≈ -1.5），这些属于市场经验事实而非第一性原理可推导的数学/逻辑恒等式。虽然公式结构在逻辑上自洽，但缺乏外部数据支持其具体数值量级的准确性，且不同市场环境下弹性系数差异巨大，直接断言特定区间存在过度自信的风险。 | source=knowledge，逻辑结构自洽（伤害度定义符合经济学直觉），但具体数值区间和弹性系数属于经验事实，无外部来源支持，依据经验事实排除条款降级。

## Search Query

price transparency intervention externalities seller buyer platform welfare economics
