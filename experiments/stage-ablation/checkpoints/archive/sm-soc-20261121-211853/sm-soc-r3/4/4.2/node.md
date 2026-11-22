# N15: 信息透明化对卖家决策的边际影响系数：假设卖家对价格偏离度的敏感度为 $\beta_s$，当偏离度 > 15% 时，卖家主动降价概率 $P_{drop}$ 从基线

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

信息透明化对卖家决策的边际影响系数：假设卖家对价格偏离度的敏感度为 $\beta_s$，当偏离度 > 15% 时，卖家主动降价概率 $P_{drop}$ 从基线 $P_0$ 提升至 $P_0 + \beta_s \times (Deviation - 0.15)$。[待核验：需A/B测试数据确定 $\beta_s$ 的具体数值，通常二手市场 $\beta_s \approx 0.2-0.5$]

## Corrected Claim

信息透明化对卖家决策的边际影响系数：假设卖家对价格偏离度的敏感度为 βs，当偏离度 > 15% 时，卖家主动降价概率 Pdrop 从基线 P0 提升至 P0 + βs × (Deviation - 0.15)。具体 βs 数值需通过 A/B 测试确定，二手市场典型范围可能在 0.2-0.5 之间（待验证）。

## Evidence

[质询]该陈述包含具体的经验参数（βs ≈ 0.2-0.5）和特定的线性模型假设，属于二手市场行为经济学范畴的经验事实，无法从第一性原理或数学公理中严格推导得出，且缺乏实证数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该参数非第一性原理可推导范畴）

## Search Query

price deviation sensitivity coefficient second hand market seller price adjustment probability
