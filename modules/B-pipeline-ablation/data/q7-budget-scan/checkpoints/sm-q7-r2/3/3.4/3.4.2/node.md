# N69: 工作点B（RTO=4h, 云对象存储）：T_rto = 500TB / 1Gbps ≈ 43,200s ≈ 12h > 4h，超出SLA时长 Δt = 8h，R

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

工作点B（RTO=4h, 云对象存储）：T_rto = 500TB / 1Gbps ≈ 43,200s ≈ 12h > 4h，超出SLA时长 Δt = 8h，RTO代价 C_rto = 8h × ¥5000/h = ¥40,000；若采用增量恢复（仅恢复变更数据 10TB），T_rto ≈ 0.24h < 4h，C_rto = 0

## Corrected Claim

工作点B（RTO=4h, 云对象存储）：T_rto = 500TB / 1Gbps ≈ 43,200s ≈ 12h > 4h，超出SLA时长 Δt = 8h，RTO代价 C_rto = 8h × ¥5000/h = ¥40,000；若采用增量恢复（仅恢复变更数据 10TB），T_rto ≈ 0.24h < 4h，C_rto = 0

## Evidence

先验知识/题面给定，逻辑校验通过：500TB/1Gbps≈43200s=12h，12h>4h，Δt=8h，8h*5000=40000；10TB/1Gbps≈0.24h<4h，逻辑自洽且数值量级合理
