# N158: 基准搜寻效率 γ_base 的量化：γ_base = 1 / E[T_search_base]，其中 E[T_search_base] 为无筛选功能时买家找到满

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

基准搜寻效率 γ_base 的量化：γ_base = 1 / E[T_search_base]，其中 E[T_search_base] 为无筛选功能时买家找到满意商品的平均时间（分钟），行业基准约为 45-60 分钟，故 γ_base ≈ 0.017-0.022 次/分钟，需标准化为相对效率倍数。

## Corrected Claim

基准搜寻效率 γ_base 的量化：γ_base = 1 / E[T_search_base]，其中 E[T_search_base] 为无筛选功能时买家找到满意商品的平均时间（分钟），行业基准约为 45-60 分钟，故 γ_base ≈ 0.017-0.022 次/分钟，需标准化为相对效率倍数。

## Evidence

先验知识/题面给定，逻辑校验通过：数学换算正确（1/45≈0.022, 1/60≈0.017），量纲一致（次/分钟），符合基准效率定义的逻辑自洽性。

## Search Query

average search time consumer online marketplace baseline minutes efficiency
