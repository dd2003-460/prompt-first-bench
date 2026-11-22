# N380: 基线挂价偏差标准差 σ_δ_base 的计算：基于平台历史数据，计算 σ_δ_base = sqrt(Σ(δ_i - μ_δ)^2 / N)，其中 δ_i 为每

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N128

## Claim

基线挂价偏差标准差 σ_δ_base 的计算：基于平台历史数据，计算 σ_δ_base = sqrt(Σ(δ_i - μ_δ)^2 / N)，其中 δ_i 为每个商品的挂价与近期成交中位价之比减1；需确定 σ_δ_base 的具体数值（如 0.15 或 0.20）以作为 30% 下降幅度的计算基准。

## Corrected Claim

基线挂价偏差标准差 σ_δ_base 的计算公式为 sqrt(Σ(δ_i - μ_δ)^2 / N)，其中 δ_i 定义为商品挂价与近期成交中位价之比减1；具体数值需基于特定平台的历史数据实证计算得出，而非固定常数。

## Evidence

[质询]该陈述包含具体的经验数值（如0.15或0.20）和特定的统计口径（近期成交中位价），属于经验事实，无法从第一性原理推导，且缺乏外部来源支持其具体数值或口径的普适性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

second hand marketplace listing price deviation standard deviation baseline calculation
