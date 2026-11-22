# N159: ε_seller 的时间序列特性：卖家的估计误差并非独立同分布，而是存在自相关性，AR(1) 系数 ρ_ε ≈ 0.6，意味着前一次定价失误会影响下一次定价，导

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N47

## Claim

ε_seller 的时间序列特性：卖家的估计误差并非独立同分布，而是存在自相关性，AR(1) 系数 ρ_ε ≈ 0.6，意味着前一次定价失误会影响下一次定价，导致偏差持续存在而非随机抵消。

## Corrected Claim

ε_seller 的时间序列特性：卖家的估计误差并非独立同分布，而是存在自相关性，AR(1) 系数 ρ_ε ≈ 0.6，意味着前一次定价失误会影响下一次定价，导致偏差持续存在而非随机抵消。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

autocorrelation of seller pricing errors dynamic pricing behavior
