# N160: 高溢价商品触发筛选行为的阈值 D_trigger：当 D = (P_ask - P_mkt)/P_mkt > 10% 时，买家使用价格筛选功能的概率 P_use

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

高溢价商品触发筛选行为的阈值 D_trigger：当 D = (P_ask - P_mkt)/P_mkt > 10% 时，买家使用价格筛选功能的概率 P_use_filter 显著上升，P_use_filter = P_base + θ * D，其中 θ ≈ 0.5-0.8，意味着每增加 1% 溢价，筛选使用率增加 0.5%-0.8%。

## Corrected Claim

高溢价商品可能触发买家的筛选行为，具体阈值D_trigger及筛选使用率增加系数θ需依据特定平台或市场的实证数据确定，通常认为溢价超过一定比例（如10%）会显著影响用户行为。

## Evidence

[质询]该陈述包含具体的经验参数（阈值10%、系数θ≈0.5-0.8），属于行为经济学/平台经济学的实证结论，无法从第一性原理或数学公理严格推导得出，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

consumer filter usage probability high price deviation threshold e-commerce behavior
