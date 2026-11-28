# N300: 参数 β (衰减速率) 决定了遵循度跌破阈值（如 50%）的临界上下文长度 L_crit；由公式 0.5 = 1 - 0.6 * exp(-β * (L_cri

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N121

## Claim

参数 β (衰减速率) 决定了遵循度跌破阈值（如 50%）的临界上下文长度 L_crit；由公式 0.5 = 1 - 0.6 * exp(-β * (L_crit - 4000)) 可反推 L_crit ≈ 4000 + ln(4/3)/β ≈ 5310 tokens (当 β=0.0005)，这意味着在 ~5.3k tokens 后遵循度即开始显著劣化，而非仅在超长文本时发生。

## Corrected Claim

参数 β (衰减速率) 决定了遵循度跌破阈值（如 50%）的临界上下文长度 L_crit；由公式 0.5 = 1 - 0.6 * exp(-β * (L_crit - 4000)) 可反推 L_crit ≈ 4000 + ln(4/3)/β ≈ 5310 tokens (当 β=0.0005)，这意味着在 ~5.3k tokens 后遵循度即开始显著劣化，而非仅在超长文本时发生。

## Search Query

instruction retention threshold critical context length exponential decay beta
