# N221: 搜索成本项投影 Search_C 的变化率 ΔC_search/C_search：当挂价偏离度 D 从 0.2 降至 0.1，Var(P) 减半，C_searc

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N65

## Claim

搜索成本项投影 Search_C 的变化率 ΔC_search/C_search：当挂价偏离度 D 从 0.2 降至 0.1，Var(P) 减半，C_search_new = C_search_base / sqrt(2)，变化率 = -29.3%，对应绝对节省 ΔC = 20 货币单位（若 C_search_base=50）。

## Corrected Claim

搜索成本项投影 Search_C 的变化率 ΔC_search/C_search：当挂价偏离度 D 从 0.2 降至 0.1，Var(P) 减半，C_search_new = C_search_base / sqrt(2)，变化率 = -29.3%，对应绝对节省 ΔC ≈ 14.65 货币单位（若 C_search_base=50）。

## Evidence

先验知识/题面给定，逻辑校验通过：1. 数学计算正确，1/sqrt(2) ≈ 0.707，变化率 0.707-1 = -29.3%；2. 绝对节省计算正确，50 * (1 - 0.707) ≈ 14.65，但题目中声称绝对节省为20，这里存在数值矛盾。等等，让我重新检查。C_search_new = 50 / 1.414 = 35.35。ΔC = 50 - 35.35 = 14.65。题目说 ΔC = 20。这是一个硬逻辑错误/数值错误。
