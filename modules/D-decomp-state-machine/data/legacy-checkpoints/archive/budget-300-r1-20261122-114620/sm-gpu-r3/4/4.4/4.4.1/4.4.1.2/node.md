# N350: 工作点 B（中性价比/基准）：采用消费级 GPU（如 RTX 4090/3090），MTBF 为 50,000 小时，λ_single = 2e-5 failu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

工作点 B（中性价比/基准）：采用消费级 GPU（如 RTX 4090/3090），MTBF 为 50,000 小时，λ_single = 2e-5 failures/hour，年均故障 0.1752 次/年，对应年均维护成本 C_maint = 0.1752 * $50/hour * 3h + 0.1752 * $1,600 = $307/年，初始成本低但故障率是数据中心级的 2 倍。

## Corrected Claim

工作点 B（中性价比/基准）：采用消费级 GPU（如 RTX 4090/3090），MTBF 为 50,000 小时，λ_single = 2e-5 failures/hour，年均故障 0.1752 次/年，对应年均维护成本 C_maint = 0.1752 * $50/hour * 3h + 0.1752 * $1,600 = $307/年，初始成本低但故障率是数据中心级的 2 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：MTBF 50,000小时对应λ=2e-5/h，年均故障率0.1752次/年，维护成本计算逻辑自洽且数值量级合理。
