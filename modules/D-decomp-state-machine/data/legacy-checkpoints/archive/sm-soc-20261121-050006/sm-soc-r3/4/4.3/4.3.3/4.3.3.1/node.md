# N280: 平台用户增长阶段（Exploration vs Exploitation）的量化边界条件为：当 DAU 月增长率 g_dau > 10% 时，算法进入探索模式，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88

## Claim

平台用户增长阶段（Exploration vs Exploitation）的量化边界条件为：当 DAU 月增长率 g_dau > 10% 时，算法进入探索模式，价格信号权重 w_price 线性下降至 0.2 * w_base；当 g_dau < 2% 时，进入利用模式，w_price 稳定在 0.4 * w_base 以上，该阈值基于某头部二手平台 2021-2023 年的 A/B 测试流量分配日志。

## Corrected Claim

平台用户增长阶段（Exploration vs Exploitation）的量化边界条件通常涉及DAU月增长率阈值，具体数值（如10%、2%）及价格信号权重调整系数需依据特定平台的A/B测试数据确定，当前缺乏公开可靠来源证实该特定数值组合。

## Evidence

[质询]该陈述包含具体的经验性参数（10%、2%、0.2、0.4）及特定来源（某头部二手平台2021-2023 A/B日志），属于无法从第一性原理推导的经验事实，且检索无可用来源支持，存在数值臆造或来源不可靠的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

platform DAU growth rate threshold exploration exploitation algorithm weight adjustment historical log
