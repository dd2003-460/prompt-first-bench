# N141: 受影响卖家占比 $\%_{affected}$ 为价格偏差分布 $f(\delta)$ 在 $\delta > 2\%$ 区间的积分，即 $\%_{affect

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

受影响卖家占比 $\%_{affected}$ 为价格偏差分布 $f(\delta)$ 在 $\delta > 2\%$ 区间的积分，即 $\%_{affected} = \int_{0.02}^{\infty} f(\delta) d\delta$。若 $f(\delta)$ 服从拉普拉斯分布 $L(0, b)$，则 $\%_{affected} = 0.5 \times e^{-0.02/b}$。

## Corrected Claim

受影响卖家占比 $\%_{affected}$ 为价格偏差分布 $f(\delta)$ 在 $\delta > 2\%$ 区间的积分，即 $\%_{affected} = \int_{0.02}^{\infty} f(\delta) d\delta$。若 $f(\delta)$ 服从拉普拉斯分布 $L(0, b)$，则 $\%_{affected} = 0.5 \times e^{-0.02/b}$。

## Evidence

先验知识/题面给定，逻辑校验通过：拉普拉斯分布 L(0,b) 的 CDF 在 x>0 时为 1-0.5*exp(-x/b)，故 P(δ>0.02) = 0.5*exp(-0.02/b)，推导正确。
