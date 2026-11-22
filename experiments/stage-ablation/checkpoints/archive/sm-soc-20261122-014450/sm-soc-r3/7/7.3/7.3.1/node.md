# N368: T_lag 的统计定义：T_lag 为算法权重变化日 t0 之后，卖家平均挂价 P_list(t) 的累计移动平均（CMA，窗口 7 天）首次显著偏离基准值（|

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N117

## Claim

T_lag 的统计定义：T_lag 为算法权重变化日 t0 之后，卖家平均挂价 P_list(t) 的累计移动平均（CMA，窗口 7 天）首次显著偏离基准值（|ΔP_list| > 2*σ_P）的最早日期 t1 与 t0 的差值，t1 - t0 即 T_lag。

## Corrected Claim

T_lag 的统计定义：T_lag 为算法权重变化日 t0 之后，卖家平均挂价 P_list(t) 的累计移动平均（CMA，窗口 7 天）首次显著偏离基准值（|ΔP_list| > 2*σ_P）的最早日期 t1 与 t0 的差值，t1 - t0 即 T_lag。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

statistical definition seller price adjustment lag time algorithm change
