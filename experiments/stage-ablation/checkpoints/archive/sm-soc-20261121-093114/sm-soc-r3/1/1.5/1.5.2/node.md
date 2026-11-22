# N41: 机会成本量化：买家在等待期间搜索其他同类商品的预期收益 E[Benefit_search] = ∫(P_market - P_alt) * f_alt(t) d

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N10

## Claim

机会成本量化：买家在等待期间搜索其他同类商品的预期收益 E[Benefit_search] = ∫(P_market - P_alt) * f_alt(t) dt，若E[Benefit_search] > 0，则买家放弃当前商品，该积分取决于替代商品分布密度f_alt(t)。

## Corrected Claim

在简化模型中，买家等待期间的机会成本可近似表示为替代商品预期收益的积分，但该收益需扣除搜索成本，且具体形式取决于效用函数和搜索策略，并非普适的固定积分公式。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑依赖而非正交（下游投影2依赖于共享随机源中的积分结果），且遗漏了父节点公式中关键变量 P_market（市场价格）的量化或定义，导致模型输入不完备。）

## Search Query

opportunity cost waiting time alternative search benefit integration consumer choice
