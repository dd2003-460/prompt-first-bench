# N369: SWE-bench Verified 中同时满足 'patch 行数 ∈ [50, 200]' 且 '依赖库数量 ≤ 3' 的题目交集数量为 142 道，与 N

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N117

## Claim

SWE-bench Verified 中同时满足 'patch 行数 ∈ [50, 200]' 且 '依赖库数量 ≤ 3' 的题目交集数量为 142 道，与 N117 声称的 ~150 道偏差为 5.3% [待核验]

## Corrected Claim

SWE-bench Verified 中同时满足 'patch 行数 ∈ [50, 200]' 且 '依赖库数量 ≤ 3' 的题目交集数量约为 140-150 道，与 N117 声称的 ~150 道偏差较小。

## Evidence

[质询]具体数值（142道）及偏差百分比（5.3%）属于经验统计数据，无法从第一性原理推导，且缺乏来源支持其精确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

SWE-bench Verified subset filtering patch lines AND dependency count intersection
