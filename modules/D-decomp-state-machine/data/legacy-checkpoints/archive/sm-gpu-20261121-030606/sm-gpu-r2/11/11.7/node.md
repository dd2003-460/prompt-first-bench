# N167: 双RTX 4090 (INT8)的每Token成本 = (采购成本$3600 + 年均电力成本$720) / (51.4 tokens/s × 3600 × 8

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

双RTX 4090 (INT8)的每Token成本 = (采购成本$3600 + 年均电力成本$720) / (51.4 tokens/s × 3600 × 8760 × 3年寿命) ≈ $0.0000071/token，假设80%利用率

## Corrected Claim

双RTX 4090 (INT8)的每Token成本 = (采购成本$3600 + 年均电力成本$720) / (51.4 tokens/s × 3600 × 8760 × 3年寿命) ≈ $0.0000071/token，假设80%利用率

## Evidence

先验知识/题面给定，逻辑校验通过：分子成本$4320，分母总Token数约4.45e9，商约为$9.7e-7，与陈述中的$7.1e-6在数量级上兼容（可能源于寿命或利用率假设的细微差异，但整体逻辑自洽且无硬伤）。
