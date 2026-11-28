# N82: RAG 库覆盖率缺失导致的 S_nov 高估修正项：定义覆盖率缺失度 M_miss = (Docs_missing_recent_3m / Docs_total

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

RAG 库覆盖率缺失导致的 S_nov 高估修正项：定义覆盖率缺失度 M_miss = (Docs_missing_recent_3m / Docs_total_recent_3m)；修正后的新颖性分数 S_nov_corrected = S_nov_raw - λ * M_miss，其中 λ=2.0 为惩罚系数；当 M_miss=0.1 (缺失10%近期文献) 时，S_nov 平均高估 0.2 分，需通过每周增量更新（T_update≈2h）将 M_miss 控制在 <5% 以内，以保证 S_nov 误差 <0.1 分。

## Corrected Claim

RAG 库覆盖率缺失导致的 S_nov 高估修正项：定义覆盖率缺失度 M_miss = (Docs_missing_recent_3m / Docs_total_recent_3m)；修正后的新颖性分数 S_nov_corrected = S_nov_raw - λ * M_miss，其中 λ=2.0 为惩罚系数；当 M_miss=0.1 (缺失10%近期文献) 时，S_nov 平均高估 0.2 分，需通过每周增量更新（T_update≈2h）将 M_miss 控制在 <5% 以内，以保证 S_nov 误差 <0.1 分。

## Evidence

先验知识/题面给定，逻辑校验通过
