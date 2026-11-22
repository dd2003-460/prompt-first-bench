# N78: 在‘低阈值/高溢价’工作点（实测 $\theta_{sc} = 3\%$，商品单价 $P_{item} = 200$ 元），搜索成本占比临界值为 $C_{tot

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N28

## Claim

在‘低阈值/高溢价’工作点（实测 $\theta_{sc} = 3\%$，商品单价 $P_{item} = 200$ 元），搜索成本占比临界值为 $C_{total} < 6$ 元；若单次搜索成本为 0.5 元，买家最多执行 12 次搜索；当 15-25% 溢价导致需增加 5 次以上验证搜索时，总成本占比超过 3%，买家立即转向依赖‘销量’或‘信用’等信号筛选，不再比价。

## Corrected Claim

在‘低阈值/高溢价’工作点（实测 θ_sc = 3%，商品单价 P_item = 200 元），搜索成本占比临界值为 C_total < 6 元；若单次搜索成本为 0.5 元，买家最多执行 12 次搜索；当溢价导致验证搜索次数增加使总成本占比超过 3% 时，买家倾向于转向依赖‘销量’或‘信用’等信号筛选，而非继续比价。

## Evidence

[质询]该陈述包含具体的经验性参数（如‘15-25%溢价导致需增加5次以上验证搜索’、‘买家立即转向’的行为阈值），这些属于市场行为经验事实，无法从第一性原理严格推导，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

second hand marketplace buyer search cost threshold A/B test premium price signal filtering
