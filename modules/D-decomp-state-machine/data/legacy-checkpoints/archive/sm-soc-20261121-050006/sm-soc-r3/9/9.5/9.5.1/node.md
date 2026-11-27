# N347: 买家搜索疲劳阈值 N_fatigue_threshold 的实证估计值：基于用户行为日志数据，当累计浏览商品数超过 N_fatigue_threshold（如 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N112

## Claim

买家搜索疲劳阈值 N_fatigue_threshold 的实证估计值：基于用户行为日志数据，当累计浏览商品数超过 N_fatigue_threshold（如 25 件）时，CTR 下降幅度 > 20%，该阈值需通过 A/B 测试或历史数据回归确定。

## Corrected Claim

买家搜索疲劳阈值 N_fatigue_threshold 的实证估计值：基于用户行为日志数据，当累计浏览商品数超过特定阈值时，CTR 可能出现显著下降，该阈值需通过 A/B 测试或历史数据回归确定，具体数值因业务场景而异。

## Evidence

[质询]该陈述包含具体的经验数值（25件、20%），属于特定场景下的统计规律，无法从第一性原理推导，且缺乏来源支持其普适性或具体数值准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

buyer search fatigue threshold CTR drop cumulative browsing items e-commerce
