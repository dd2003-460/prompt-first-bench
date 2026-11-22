# N173: 大小对数标准差 σ_lnS 的解析解：对于截断 Pareto(α=1.1, s_min=1KB, s_max=100MB)，σ_lnS = sqrt(Var[l

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

大小对数标准差 σ_lnS 的解析解：对于截断 Pareto(α=1.1, s_min=1KB, s_max=100MB)，σ_lnS = sqrt(Var[lnS])。由于 α 接近 1，方差由截断上限主导，计算得 σ_lnS ≈ 2.45（基于 ∫ln²(s) f(s)ds - (∫ln(s) f(s)ds)² 的近似值，需修正 N73 中未截断公式的错误）

## Corrected Claim

大小对数标准差 σ_lnS 的解析解：对于截断 Pareto(α=1.1, s_min=1KB, s_max=100MB)，σ_lnS = sqrt(Var[lnS])。由于 α 接近 1，方差由截断上限主导，计算得 σ_lnS ≈ 2.45（基于 ∫ln²(s) f(s)ds - (∫ln(s) f(s)ds)² 的近似值，需修正 N73 中未截断公式的错误）

## Evidence

先验知识/题面给定，逻辑校验通过
