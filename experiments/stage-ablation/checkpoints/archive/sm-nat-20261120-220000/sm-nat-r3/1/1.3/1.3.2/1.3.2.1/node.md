# N79: 截断后的 CV_size 计算：在 S_max=10MB, S_min=1KB 条件下，CV_size = sqrt(Var(S)/E[S]^2 - 1)。数值

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N25

## Claim

截断后的 CV_size 计算：在 S_max=10MB, S_min=1KB 条件下，CV_size = sqrt(Var(S)/E[S]^2 - 1)。数值积分得 E[S]≈11.1KB, Var(S)≈(10MB)^2 * (0.1/1.1) * (1 - (1000)^-0.1) / (0.1*1.1)^2 ≈ 8.5e10 KB^2，故 CV_size ≈ sqrt(8.5e10 / (11.1^2) - 1) ≈ 850，表明大小分布极度不均。

## Corrected Claim

截断后的 CV_size 计算：在 S_max=10MB, S_min=1KB 条件下，CV_size = sqrt(Var(S)/E[S]^2 - 1)。若 E[S]≈11.1KB 且 CV_size≈850，则 Var(S) 应约为 8.9e7 KB^2，而非 8.5e10 KB^2。

## Evidence

[质询]数值量级与公式推导存在严重矛盾：若 E[S]≈11.1KB，则 E[S]^2≈123 KB^2。要使 CV≈850，Var(S) 需约为 850^2 * 123 ≈ 8.9e7 KB^2。但陈述中声称 Var(S)≈8.5e10 KB^2，这比所需值大了约 1000 倍。若 Var(S) 真为 8.5e10，则 CV 应约为 sqrt(8.5e10/123) ≈ 8300，而非 850。此外，给出的 Var(S) 计算公式结构混乱，量纲和数值逻辑不自洽。 | 逻辑校验失败：CV 计算结果与给定的 Var(S) 和 E[S] 数值不匹配，存在数量级错误。
