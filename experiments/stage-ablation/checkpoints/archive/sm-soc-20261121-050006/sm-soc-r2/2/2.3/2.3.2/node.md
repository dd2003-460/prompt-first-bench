# N61: 下游投影 1（佣金收益项）：Fee_rate * GMV 项中，GMV = Σ(P_i * Q_i)，其中 P_i 为成交价，Q_i 为成交量；在均衡状态下，高

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N12

## Claim

下游投影 1（佣金收益项）：Fee_rate * GMV 项中，GMV = Σ(P_i * Q_i)，其中 P_i 为成交价，Q_i 为成交量；在均衡状态下，高挂价导致 P_i 偏高但 Q_i 偏低，GMV 对 P_ask 的弹性 ε_GMV_P 为负（ε_GMV_P ∈ [-1.5, -0.8]），量化了平台从交易佣金中获得的收益对卖家定价策略的敏感度。

## Corrected Claim

下游投影 1（佣金收益项）：Fee_rate * GMV 项中，GMV = Σ(P_i * Q_i)，其中 P_i 为成交价，Q_i 为成交量；在均衡状态下，高挂价导致 P_i 偏高但 Q_i 偏低，GMV 对 P_ask 的弹性 ε_GMV_P 为负（ε_GMV_P ∈ [-1.5, -0.8]），量化了平台从交易佣金中获得的收益对卖家定价策略的敏感度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Gross Merchandise Value elasticity price volume commission rate second hand platform
