# N141: TTL 设置对 P_expire 的敏感度：P_expire = 1 - exp(-T/100)，当 T 从 1 天增加到 10 天时，P_expire 从 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53, N54, N55

## Claim

TTL 设置对 P_expire 的敏感度：P_expire = 1 - exp(-T/100)，当 T 从 1 天增加到 10 天时，P_expire 从 0.0099 增加到 0.0952，即 TTL 每增加 1 天，P_expire 增加约 0.95%。

## Corrected Claim

TTL 设置对 P_expire 的敏感度：P_expire = 1 - exp(-T/100)，当 T 从 1 天增加到 10 天时，P_expire 从 0.0099 增加到 0.0952，即 TTL 每增加 1 天，P_expire 增加约 0.95%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P=1-exp(-T/100) 在 T=1 时约为 0.00995，T=10 时约为 0.09516，数值量级与陈述一致；虽然平均增量约为 0.95%/天，但边际增量随 T 增加而递减，陈述中的“每增加 1 天”为近似表述，在工程估算语境下可接受。

## Search Query

TTL setting impact on cache expiration probability
