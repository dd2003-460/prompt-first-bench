# N229: 工作点3（高成本低性）：采用跨大区公网BGP接入，RTT_pop_origin_p99 ≈ 40-80ms，带宽成本 C_bandwidth_per_GB ≈ 

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

工作点3（高成本低性）：采用跨大区公网BGP接入，RTT_pop_origin_p99 ≈ 40-80ms，带宽成本 C_bandwidth_per_GB ≈ ¥0.08/GB，总 P99(T_origin_fetch_self) ≈ 50-100ms，仅在 T=200ms 下合规，且受骨干网拥塞影响大。

## Corrected Claim

工作点3（高成本低性）：采用跨大区公网BGP接入，RTT_pop_origin_p99 ≈ 40-80ms，带宽成本 C_bandwidth_per_GB ≈ ¥0.08/GB，总 P99(T_origin_fetch_self) ≈ 50-100ms，仅在 T=200ms 下合规，且受骨干网拥塞影响大。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的（分别对应延迟构成、成本模型、拥塞影响），且无冗余。但在完备性上存在缺失：父节点明确指出了该工作点“仅在 T=200ms 下合规”这一关键约束条件，而三个子节点仅描述了延迟估算、成本计算和拥塞影响，均未涉及对“200ms 合规阈值”的具体验证逻辑或与该阈值的对比分析，导致无法完整支撑父节点关于合规性的结论。）
