# N403: 临界信号强度 S_crit 的推导基础：S_crit = (C_search_cost / C_matching_benefit) * (1/ε_price)，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130

## Claim

临界信号强度 S_crit 的推导基础：S_crit = (C_search_cost / C_matching_benefit) * (1/ε_price)，其中 C_search_cost 为买家单位时间搜索成本，C_matching_benefit 为匹配成功带来的效用增量，ε_price 为价格弹性。需量化 C_search_cost 在二手平台的实际值（如每分钟浏览成本）以校准 S_crit ≈ 0.6 的合理性。

## Corrected Claim

S_crit 的推导应基于搜索模型（如 Diamond 搜索模型）中买家停止搜索的边际条件，即当预期匹配收益的边际增量等于边际搜索成本时确定临界信号强度。具体数值需通过实证数据校准，而非简单套用价格弹性倒数。

## Evidence

[质询]公式结构缺乏理论依据：将搜索成本与匹配收益的比值直接乘以价格弹性的倒数（1/ε_price）在经济学逻辑上不自洽。价格弹性通常衡量需求对价格的敏感度，而非信号强度的阈值决定因素；且该公式未体现信号强度如何具体影响搜索成本或匹配概率，属于强行拼凑变量。 | 无可用外部证据；逻辑校验发现公式推导存在概念混淆，价格弹性与信号强度阈值之间缺乏直接因果或函数关系，且'每分钟浏览成本'作为量化指标过于简化，无法支撑S_crit≈0.6的精确校准。

## Search Query

search cost per minute online marketplace buyer behavior calibration
