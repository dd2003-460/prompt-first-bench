# N218: 强制降价触发概率 P_force 的高压工作点：当卖家持有天数 D > 30 天且现金流紧张度 C_urgency > 0.8 时，Floor Price 分布

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

强制降价触发概率 P_force 的高压工作点：当卖家持有天数 D > 30 天且现金流紧张度 C_urgency > 0.8 时，Floor Price 分布左移，P_force ≈ 0.65，此时平台需准备 65% 的卖家接受强制降价的客服资源。

## Corrected Claim

当卖家持有天数 D > 30 天且现金流紧张度 C_urgency > 0.8 时，Floor Price 分布左移，强制降价触发概率 P_force 显著升高（具体数值需依据平台历史数据校准），平台需相应增加客服资源准备。

## Evidence

[质询]该陈述包含具体的经验性数值（P_force ≈ 0.65）和特定的业务逻辑阈值（D > 30, C_urgency > 0.8），属于平台运营策略或市场行为统计结果，无法从第一性原理或数学公理中严格推导得出，且缺乏外部数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值非第一性原理可推导范畴）

## Search Query

seller floor price distribution holding days cash flow urgency secondhand marketplace
