# N118: 地理熵 H_geo 与 POP 点数量 N_POP 的最优匹配阈值：当 H_geo > 3.5 bits 时，10 个 POP 点覆盖 80% 流量的最低延迟阈

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

地理熵 H_geo 与 POP 点数量 N_POP 的最优匹配阈值：当 H_geo > 3.5 bits 时，10 个 POP 点覆盖 80% 流量的最低延迟阈值 RTT_80 从 45ms 上升至 75ms；若业务 P99 约束 T < 50ms，则需 N_POP ≥ 15，此时单 POP 平均覆盖用户数从 50 万降至 33 万，硬件成本增加 50%。

## Corrected Claim

地理熵 H_geo 越高，为维持相同的低延迟覆盖比例（如80%流量），所需的 POP 点数量 N_POP 越多，导致单点覆盖用户数下降及硬件成本上升。具体阈值与成本增幅需根据实际网络拓扑与业务约束建模确定。

## Evidence

[质询]该陈述包含大量具体的经验性数值（如3.5 bits阈值、45ms/75ms延迟变化、50万/33万用户数、50%成本增加），这些并非物理定律或数学公理，而是依赖于特定网络拓扑、用户分布模型及硬件定价的经验数据，无法从第一性原理严格推导。 | source=knowledge，逻辑自洽（熵增导致覆盖难度增加，需更多节点，成本上升符合直觉），但具体数值缺乏通用标准支持，属于特定场景下的经验估算，故降级为定性表述。

## Search Query

geographic entropy bits optimal number of CDN POP points latency threshold china
