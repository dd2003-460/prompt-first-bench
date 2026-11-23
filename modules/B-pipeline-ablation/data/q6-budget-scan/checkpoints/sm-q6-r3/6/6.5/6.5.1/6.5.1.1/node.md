# N322: 全自建策略在流量增长 50% 后的单位固定成本 $C_{fixed, new}^{self} = C_{fixed, base}^{self} / R_{new

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N121

## Claim

全自建策略在流量增长 50% 后的单位固定成本 $C_{fixed, new}^{self} = C_{fixed, base}^{self} / R_{new}$，其中 $C_{fixed, base}^{self}$ 为基准流量下的月固定总成本（¥/月），$R_{new}$ 为增长后的日均请求量（req/day），需计算具体数值降幅。

## Corrected Claim

全自建策略在流量增长 50% 后的单位固定成本 $C_{fixed, new}^{self} = C_{fixed, base}^{self} / (R_{new} / R_{base})$，其中 $R_{base}$ 为基准日均请求量，$R_{new}$ 为增长后的日均请求量；或者表述为：单位固定成本与流量成反比，即 $C_{unit, new} = C_{unit, base} \times (R_{base} / R_{new})$。

## Evidence

[质询]公式中分母 $R_{new}$ 的量纲为 req/day（请求量），而分子 $C_{fixed, base}^{self}$ 的量纲为 ¥/月（货币/时间）。直接相除得到的量纲为 ¥/(月·req/day)，并非标准的单位固定成本（¥/req 或 ¥/月）。若 $R_{new}$ 意指“相对于基准流量的倍数”（无量纲），则符号定义与“日均请求量”矛盾；若 $R_{new}$ 确为绝对请求量，则公式缺少基准请求量 $R_{base}$ 作为分母或归一化因子，导致量纲不匹配。 | 先验知识/题面给定，逻辑校验发现量纲不一致：货币/时间 除以 请求/时间 不等于 货币/请求 或 货币/时间，存在内部逻辑矛盾。
