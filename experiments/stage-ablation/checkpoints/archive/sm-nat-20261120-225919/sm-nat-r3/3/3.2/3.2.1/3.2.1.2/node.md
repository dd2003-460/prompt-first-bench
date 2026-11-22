# N159: Pareto(β=0.9) 分布下平均请求频率 R_avg 的计算公式为 R_avg = (Total_Requests / N) * E[Rank], 其中 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55, N56, N57

## Claim

Pareto(β=0.9) 分布下平均请求频率 R_avg 的计算公式为 R_avg = (Total_Requests / N) * E[Rank], 其中 E[Rank] 为 Pareto 分布的期望秩，需结合截断条件计算具体次/天数值

## Corrected Claim

Pareto(β=0.9) 分布下，平均请求频率 R_avg 应直接由分布的期望值 E[Freq] 给出，或通过总请求量除以时间窗口和实体数计算，而非乘以期望秩 E[Rank]。具体公式需根据 Pareto 分布的参数定义（如最小值 x_min）推导 E[Freq] = β * x_min / (β - 1) (当 β > 1)，并结合截断条件修正。

## Evidence

[质询]公式 R_avg = (Total_Requests / N) * E[Rank] 在量纲和逻辑上存在严重错误。Total_Requests/N 是平均每个实体的请求数（次/实体），而 E[Rank] 是无量纲的秩（或位置索引）。两者相乘得到的量纲是“次/实体 * 秩”，这并不等于“平均请求频率”（通常指次/时间单位，如次/天）。此外，Pareto 分布描述的是频率分布，其期望值 E[Freq] 直接给出平均频率，无需乘以 E[Rank]。该公式混淆了“平均频率”与“基于秩的加权平均”或“总请求量”的概念，且未体现时间维度（天），导致无法直接得出“次/天”的数值。 | 逻辑校验失败：公式量纲不一致，且 Pareto 分布的期望频率计算不应简单乘以期望秩。来源无可用证据，但基于基本统计学原理，该公式表述错误。
