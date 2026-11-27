# N162: 低频对象（r < 1/100 day）贡献的字节流量占比 P_bytes = ∫_{r_min}^{r_threshold} (r * s(r) * f(r))

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

低频对象（r < 1/100 day）贡献的字节流量占比 P_bytes = ∫_{r_min}^{r_threshold} (r * s(r) * f(r)) dr / ∫_{r_min}^{r_max} (r * s(r) * f(r)) dr，其中 f(r) 为 Pareto(β=0.9) 的概率密度函数，s(r) 为与 r 负相关的对象大小函数。

## Corrected Claim

低频对象（r < 1/100 day）贡献的字节流量占比 P_bytes = ∫_{r_min}^{r_threshold} (r * s(r) * f(r)) dr / ∫_{r_min}^{r_max} (r * s(r) * f(r)) dr，其中 f(r) 为 Pareto(β=0.9) 的概率密度函数，s(r) 为与 r 负相关的对象大小函数。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合流量占比定义（分子为特定区间积分，分母为总积分），变量定义（Pareto分布、负相关大小函数）与低频对象流量建模逻辑自洽，量纲正确。
