# N30: 下游投影2：成交周期 T_deal 的完整表达式 T_deal = [C0 * N_active_listings^δ] / (1 + α * N_active

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

下游投影2：成交周期 T_deal 的完整表达式 T_deal = [C0 * N_active_listings^δ] / (1 + α * N_active_listings)，对 N_active_listings 求导可得 dT_deal/dN = C0 * N^(δ-1) * (1 + αN - αN) / (1+αN)^2，当 δ < 1 时，随着 N 增加，T_deal 先增后减或单调变化取决于 α 和 δ 的相对大小，解释了高挂价维持高 N 时 T_deal 可能缩短的机制。

## Corrected Claim

下游投影2：成交周期 T_deal 的完整表达式 T_deal = [C0 * N_active_listings^δ] / (1 + α * N_active_listings)。对 N_active_listings 求导，当 δ < 1 时，随着 N 增加，T_deal 单调递减，解释了高挂价维持高 N 时 T_deal 缩短的机制。

## Evidence

[质询]求导公式存在明显的代数错误：对分式函数求导后，分子中不应出现 (1 + αN - αN) 这种恒等于 1 的项，且该错误导致后续关于单调性的结论缺乏严谨的数学推导支撑（实际上当 δ<1 时，分母的增长通常主导，T_deal 应单调递减，而非‘先增后减’）。 | 先验知识/题面给定，但逻辑校验发现求导过程存在代数错误，导致结论推导不严谨，故降级。

## Search Query

transaction time function listing volume network effects
