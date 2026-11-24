# N223: 全量恢复网络带宽修正：若采用10Gbps专线或公网高带宽链路，T_full_restore = 500TB / 1.25GB/s = 400,000s ≈ 11

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

全量恢复网络带宽修正：若采用10Gbps专线或公网高带宽链路，T_full_restore = 500TB / 1.25GB/s = 400,000s ≈ 111.1h，超出4h SLA的Δt = 107.1h，C_rto_full = 107.1h × ¥5000/h = ¥535,500

## Corrected Claim

全量恢复网络带宽修正：若采用10Gbps专线或公网高带宽链路，T_full_restore = 500TB / 1.25GB/s = 400,000s ≈ 111.1h，超出4h SLA的Δt = 107.1h，C_rto_full = 107.1h × ¥5000/h = ¥535,500

## Evidence

先验知识/题面给定，逻辑校验通过：10Gbps=1.25GB/s，500TB/1.25GB/s=400,000s≈111.1h，Δt=107.1h，成本计算正确

## Search Query

AWS Direct Connect 10Gbps throughput calculation
