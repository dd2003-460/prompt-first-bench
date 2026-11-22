# N271: 搜索成本 C_search 与满意度 S 的线性关系系数 k：k = (S_0 - S_min) / (C_search_max - C_search_min)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

搜索成本 C_search 与满意度 S 的线性关系系数 k：k = (S_0 - S_min) / (C_search_max - C_search_min)，其中 S_min 为最低可接受满意度，C_search_min/max 为搜索成本区间，需校准 k 以量化 20% 成本降低对 S 的具体提升幅度。

## Corrected Claim

搜索成本 C_search 与满意度 S 的线性关系系数 k：k = (S_0 - S_min) / (C_search_max - C_search_min)，其中 S_min 为最低可接受满意度，C_search_min/max 为搜索成本区间，需校准 k 以量化 20% 成本降低对 S 的具体提升幅度。

## Evidence

先验知识/题面给定，逻辑校验通过
