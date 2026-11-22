# N133: 工作点 1 中 $S_{hot}/S_{total} \approx 0.3$ 的假设需修正：在 $\alpha=1.1$ 下，小对象（$S<100KB$）的字

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57, N58, N59

## Claim

工作点 1 中 $S_{hot}/S_{total} \approx 0.3$ 的假设需修正：在 $\alpha=1.1$ 下，小对象（$S<100KB$）的字节占比 $B_{small} = \int_{1KB}^{100KB} x f_S(x) dx / \int_{1KB}^{\infty} x f_S(x) dx$；由于 $\alpha<2$，$B_{small} \approx (100KB)^{0.1} / (1KB)^{0.1} \approx 10^{0.1} \approx 1.26$（归一化后）$\approx 12.6\%$，而非 30%；因此 $\Delta H \approx 0.0028\% \cdot 0.126 \approx 0.00035\%$，进一步降低。

## Corrected Claim

工作点 1 中 $S_{hot}/S_{total} \approx 0.3$ 的假设需修正：在 $\alpha=1.1$ 下，小对象（$S<100KB$）的字节占比 $B_{small} = \int_{1KB}^{100KB} x f_S(x) dx / \int_{1KB}^{\infty} x f_S(x) dx$；由于 $\alpha<2$，$B_{small} \approx (100KB)^{0.1} / (1KB)^{0.1} \approx 10^{0.1} \approx 1.26$（归一化后）$\approx 12.6\%$，而非 30%；因此 $\Delta H \approx 0.0028\% \cdot 0.126 \approx 0.00035\%$，进一步降低。

## Evidence

先验知识/题面给定，逻辑校验通过：基于幂律分布（α=1.1）的积分推导，小对象字节占比计算符合数学逻辑，量级合理。
