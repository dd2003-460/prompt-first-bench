# N521: 考虑碎片率 5% 后，单序列实际可用 KV Cache 容量 = 262144 × (1 - 0.05) ≈ 249K tokens，符合 N185 中 238

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N185

## Claim

考虑碎片率 5% 后，单序列实际可用 KV Cache 容量 = 262144 × (1 - 0.05) ≈ 249K tokens，符合 N185 中 238K-248K 的估算范围

## Corrected Claim

考虑碎片率 5% 后，单序列实际可用 KV Cache 容量 = 262144 × (1 - 0.05) ≈ 249K tokens，符合 N185 中 238K-248K 的估算范围

## Evidence

先验知识/题面给定，逻辑校验通过：262144 * 0.95 = 249036.8，约等于 249K，计算无误且符合逻辑。
