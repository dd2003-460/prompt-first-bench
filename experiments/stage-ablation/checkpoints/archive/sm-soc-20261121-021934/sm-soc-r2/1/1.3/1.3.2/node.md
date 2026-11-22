# N29: 下游投影1：搜索成本 T_search_base 与 N_active_listings 的非线性关系 T_search_base = C0 * N_activ

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

下游投影1：搜索成本 T_search_base 与 N_active_listings 的非线性关系 T_search_base = C0 * N_active_listings^δ，其中 C0 为基准常数，δ 为搜索效率指数（通常 δ ∈ [0.5, 1.0]，表示边际递减），该公式量化了供给规模对基础搜索时间的影响，是 T_deal 公式中的分子项。

## Corrected Claim

下游投影1：搜索成本 T_search_base 与 N_active_listings 的非线性关系 T_search_base = C0 * N_active_listings^δ，其中 C0 为基准常数，δ 为搜索效率指数（通常 δ ∈ [0.5, 1.0]，表示边际递减），该公式量化了供给规模对基础搜索时间的影响，是 T_deal 公式中的分子项。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

search cost function listing volume diminishing returns
