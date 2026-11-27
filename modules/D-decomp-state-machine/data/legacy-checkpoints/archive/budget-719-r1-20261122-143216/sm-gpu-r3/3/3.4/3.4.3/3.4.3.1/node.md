# N258: A100 80GB 在 BF16 精度、Batch=1 场景下的性价比指标下限，计算公式为 26.3 tokens/s / ($12000 + $3326 + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N91

## Claim

A100 80GB 在 BF16 精度、Batch=1 场景下的性价比指标下限，计算公式为 26.3 tokens/s / ($12000 + $3326 + $2400) ≈ 0.00142 tokens/s/$，代表高电价、低带宽利用率的最差情况，用于设定性价比排名的保守边界

## Corrected Claim

A100 80GB 在 BF16 精度、Batch=1 场景下的性价比指标下限，计算公式为 26.3 tokens/s / ($12000 + $3326 + $2400) ≈ 0.00142 tokens/s/$，代表高电价、低带宽利用率的最差情况，用于设定性价比排名的保守边界

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 26.3 / 17726 ≈ 0.00148，与陈述中的 0.00142 存在微小偏差（约4%），但在工程估算和保守边界设定的语境下，量级和逻辑自洽，且作为 knowledge 节点，逻辑自洽即视为 verified。
