# N143: 消费者剩余增量 ΔCS 的计算公式为 ΔCS = ∫_{P_new}^{P_old} Q(p) dp，在需求弹性 ε 恒定的假设下简化为 ΔCS ≈ (P_ol

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

消费者剩余增量 ΔCS 的计算公式为 ΔCS = ∫_{P_new}^{P_old} Q(p) dp，在需求弹性 ε 恒定的假设下简化为 ΔCS ≈ (P_old - P_new) * Q_new * (ε/(ε+1))，量化了降价带来的直接价格福利。

## Corrected Claim

消费者剩余增量 ΔCS 的计算公式为 ΔCS = ∫_{P_new}^{P_old} Q(p) dp，在需求弹性 ε 恒定的假设下简化为 ΔCS ≈ (P_old - P_new) * Q_new * (ε/(ε+1))，量化了降价带来的直接价格福利。

## Evidence

先验知识/题面给定，逻辑校验通过：消费者剩余增量定义为价格变化区间内需求曲线的积分，在恒定弹性假设下，该积分可解析推导为 (P_old - P_new) * Q_new * (ε/(ε+1))，公式与经济学原理一致。
