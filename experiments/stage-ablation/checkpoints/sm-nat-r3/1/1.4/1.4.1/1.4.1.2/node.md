# N129: 在 x_min=1KB 且 x_max=10GB 的典型 CDN 工作点下，截断 Pareto(α=1.1) 的均值 E[S] 约为 2-5KB 量级（具体取决

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

在 x_min=1KB 且 x_max=10GB 的典型 CDN 工作点下，截断 Pareto(α=1.1) 的均值 E[S] 约为 2-5KB 量级（具体取决于 x_max），此时 N_cache 将远大于 10万，导致缓存覆盖率 f_cache > 1，LRU 命中率下界趋近于 100%。

## Corrected Claim

在 x_min=1KB 且 x_max=10GB 的典型 CDN 工作点下，截断 Pareto(α=1.1) 的均值 E[S] 约为 10KB 量级（具体取决于 x_max 截断效应），若 N_cache 足够大（如 >100GB），缓存覆盖率 f_cache 可能接近或超过 1，LRU 命中率下界趋近于 100%。

## Evidence

[质询]数值量级与逻辑推导存在严重矛盾：Pareto(α=1.1) 在 x_min=1KB 时，理论均值 E[S] 约为 11KB（公式 x_min/(α-1)），而非 2-5KB；且若 E[S] 仅为 2-5KB，则 N_cache 需达到 TB 级才能远大于 10万，这与 CDN 典型缓存规模（GB-TB）及 x_max=10GB 的约束不符，导致 f_cache > 1 的结论缺乏稳健的数值支撑。 | 无可用外部证据；逻辑校验发现均值估算偏低（Pareto α=1.1, x_min=1KB 时 E[S]≈11KB），且 N_cache 与 f_cache 的推导依赖未明确的具体 N_cache 数值，存在内部数值不一致风险。

## Search Query

truncated Pareto distribution mean calculation alpha=1.1 x_min=1KB x_max=10GB
