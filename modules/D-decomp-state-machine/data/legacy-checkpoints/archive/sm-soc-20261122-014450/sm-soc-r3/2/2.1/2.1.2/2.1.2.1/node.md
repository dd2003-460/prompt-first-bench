# N165: t_search (平均验证耗时) 的量化：定义为买家从点击商品到发起咨询的平均时间间隔。需区分高挂价组（P_list > 1.2*P_mkt）与市场价组（P_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N50

## Claim

t_search (平均验证耗时) 的量化：定义为买家从点击商品到发起咨询的平均时间间隔。需区分高挂价组（P_list > 1.2*P_mkt）与市场价组（P_list ≈ P_mkt）的 t_search 差异，预期高挂价组 t_search 更短（如 5分钟 vs 10分钟），以支持‘快速筛选’假设。

## Corrected Claim

t_search 定义为买家从点击商品到发起咨询的平均时间间隔。需区分高挂价组与市场价组的 t_search 差异，以检验‘快速筛选’假设（即高挂价组可能因价格信号明确而缩短决策时间，但具体数值需实证数据支持）。

## Evidence

[质询]该陈述包含具体的经验性数值预测（5分钟 vs 10分钟）和方向性假设（高挂价组耗时更短），属于市场行为经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

average time to inquiry for high-priced vs market-priced items online
