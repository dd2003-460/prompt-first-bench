# N65: 成交概率-价格函数：Prob(Sell|P_ask) = ψ((P_ask - V)/σ)，其中 ψ 为单调递减函数，且由于筛选效应，ψ 在 P_ask > V

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N15

## Claim

成交概率-价格函数：Prob(Sell|P_ask) = ψ((P_ask - V)/σ)，其中 ψ 为单调递减函数，且由于筛选效应，ψ 在 P_ask > V + θ·σ 时下降斜率小于 φ，导致高挂价商品成交率相对点击率衰减更慢。

## Corrected Claim

成交概率-价格函数：Prob(Sell|P_ask) = ψ((P_ask - V)/σ)，其中 ψ 为单调递减函数，且由于筛选效应，ψ 在 P_ask > V + θ·σ 时下降斜率小于 φ，导致高挂价商品成交率相对点击率衰减更慢。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

conversion rate price elasticity screening effect
