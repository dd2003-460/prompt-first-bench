# N45: 平台搜索算法的‘价格粘性’机制具体参数：商品重新进入买家高频推荐流（Re-indexing）所需的最低价格变动幅度阈值 $\Delta P_{min}$ 为 5

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

平台搜索算法的‘价格粘性’机制具体参数：商品重新进入买家高频推荐流（Re-indexing）所需的最低价格变动幅度阈值 $\Delta P_{min}$ 为 5%，且存在固定的时间延迟 $\tau_{delay}$ 为 24-48 小时，导致 48 小时内的降价无法触发即时流量增量。

## Corrected Claim

部分平台搜索算法存在‘价格粘性’机制，通常表现为商品需达到一定幅度的价格变动（如5%左右）并经过一定时间延迟（如24-48小时）后，才能重新进入高频推荐流，导致短期内的降价无法触发即时流量增量。

## Evidence

[质询]该陈述包含具体的工程参数（5%阈值、24-48小时延迟），属于特定平台内部算法的黑盒经验事实，无法从第一性原理推导，且不同平台或不同时期的策略可能完全不同，存在将特定案例或过时信息泛化为通用机制的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且属于不可推导的平台内部具体参数）

## Search Query

e-commerce platform search algorithm price volatility re-indexing delay threshold
