# N312: ε_base = 0.05 的微观行为基础：对应买家每次刷新页面时随机浏览非搜索推荐商品的比例；需验证该比例在移动端 vs 桌面端、新用户 vs 老用户之间的差

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107

## Claim

ε_base = 0.05 的微观行为基础：对应买家每次刷新页面时随机浏览非搜索推荐商品的比例；需验证该比例在移动端 vs 桌面端、新用户 vs 老用户之间的差异（假设移动端高 0.02，新用户高 0.01）。

## Corrected Claim

ε_base 的微观行为基础对应买家随机浏览非搜索推荐商品的比例；需验证该比例在移动端 vs 桌面端、新用户 vs 老用户之间的差异（具体数值如 0.05, +0.02, +0.01 为假设值，需实证数据验证）。

## Evidence

[质询]该陈述包含具体的经验性参数（ε_base=0.05, 移动端差异+0.02, 新用户差异+0.01），这些数值属于特定业务场景下的统计假设或经验数据，无法从第一性原理或数学公理中严格推导得出，且缺乏外部来源支持其具体数值量级。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值非第一性原理可推导）

## Search Query

e-commerce browsing behavior random exploration rate mobile vs desktop
