# N220: 搜索成本项投影 Search_C 的基准值 C_search_base：C_search_base = c_time · t_base · sqrt(Var(P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N65

## Claim

搜索成本项投影 Search_C 的基准值 C_search_base：C_search_base = c_time · t_base · sqrt(Var(P_hist))，其中 c_time 为买家时间机会成本（货币/小时），t_base 为基准搜索时间（小时），sqrt(Var(P_hist)) 为价格离散度。

## Corrected Claim

搜索成本项投影 Search_C 的基准值 C_search_base：C_search_base = c_time · t_base · sqrt(Var(P_hist))，其中 c_time 为买家时间机会成本（货币/小时），t_base 为基准搜索时间（小时），sqrt(Var(P_hist)) 为价格离散度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

search cost model price dispersion sqrt variance
