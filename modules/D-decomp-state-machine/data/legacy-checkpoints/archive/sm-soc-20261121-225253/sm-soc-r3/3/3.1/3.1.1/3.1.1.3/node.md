# N83: 排名从Top 10%降至Top 50%的量化定义：设商品总数为 $N$，Top 10% 对应排名 $R_{10} = 0.1N$，Top 50% 对应排名 $R

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

排名从Top 10%降至Top 50%的量化定义：设商品总数为 $N$，Top 10% 对应排名 $R_{10} = 0.1N$，Top 50% 对应排名 $R_{50} = 0.5N$；要使高挂价商品排名从 $R_{10}$ 降至 $R_{50}$，需满足 $Score_{new} < Score_{threshold}$，其中 $Score_{threshold}$ 为Top 50%的最低得分；具体 $Score_{threshold}$ 需基于平台得分分布的分位数计算，假设得分服从对数正态分布，则 $Score_{threshold} = \mu_{score} - 0.52\sigma_{score}$（对应50%分位）。

## Corrected Claim

排名从Top 10%降至Top 50%的量化定义：设商品总数为 $N$，Top 10% 对应排名 $R_{10} = 0.1N$，Top 50% 对应排名 $R_{50} = 0.5N$；要使高挂价商品排名从 $R_{10}$ 降至 $R_{50}$，需满足 $Score_{new} < Score_{threshold}$，其中 $Score_{threshold}$ 为Top 50%的最低得分（即得分分布的中位数）。若假设得分服从正态分布，则 $Score_{threshold} = \mu_{score}$；若假设得分服从对数正态分布，则 $Score_{threshold} = \exp(\mu_{score})$。

## Evidence

[质询]陈述中假设得分服从对数正态分布，并据此得出 Top 50% 的阈值公式 $Score_{threshold} = \mu_{score} - 0.52\sigma_{score}$。然而，对数正态分布的中位数（50%分位）是 $\exp(\mu_{score})$，而非 $\mu_{score} - 0.52\sigma_{score}$。后者是正态分布中位数（均值）附近的某种线性组合，且系数 0.52 缺乏统计学依据（正态分布中位数即均值，系数应为0；若指其他分位，系数也不对）。将正态分布的线性分位公式错误地套用到对数正态分布上，属于严重的逻辑/数学错误。 | 逻辑校验失败：对数正态分布的中位数公式与陈述中的线性公式矛盾，且系数 0.52 无统计学依据。

## Search Query

quantile definition for search ranking threshold
