# N149: 共享随机源：偏导数估计误差 $\epsilon_{\partial}$：$\partial E[R] / \partial w_{price}$ 的估计值 $\

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

共享随机源：偏导数估计误差 $\epsilon_{\partial}$：$\partial E[R] / \partial w_{price}$ 的估计值 $\hat{\partial E[R] / \partial w_{price}}$ 服从 $\mathcal{N}(\partial E[R] / \partial w_{price}, \sigma_{\partial}^2)$，其中 $\sigma_{\partial}$ 为回归标准误；该误差源直接影响 $\Delta w_{price}^{min}$ 的精度，$SE_{\Delta w} = \frac{\sigma_{\partial} \cdot |E[R]_{old} - E[R]_{target}|}{(\partial E[R] / \partial w_{price})^2}$。

## Corrected Claim

共享随机源：偏导数估计误差 $\epsilon_{\partial}$：$\partial E[R] / \partial w_{price}$ 的估计值 $\hat{\partial E[R] / \partial w_{price}}$ 服从 $\mathcal{N}(\partial E[R] / \partial w_{price}, \sigma_{\partial}^2)$，其中 $\sigma_{\partial}$ 为回归标准误；该误差源直接影响 $\Delta w_{price}^{min}$ 的精度，$SE_{\Delta w} = \frac{\sigma_{\partial} \cdot |E[R]_{old} - E[R]_{target}|}{(\partial E[R] / \partial w_{price})^2}$。

## Evidence

先验知识/题面给定，逻辑校验通过：基于误差传播定律（Error Propagation），若 $w_{new} = w_{old} + \Delta w$ 且 $E[R]_{target} = E[R]_{old} + \Delta w \cdot \partial E[R]/\partial w$，则 $\Delta w = (E[R]_{target} - E[R]_{old}) / \partial E[R]/\partial w$。对 $\Delta w$ 进行一阶泰勒展开近似，其标准误 $SE_{\Delta w} \approx |\Delta E[R]| \cdot SE_{\partial} / |\partial E[R]|^2$，与陈述中的公式 $SE_{\Delta w} = \frac{\sigma_{\partial} \cdot |E[R]_{old} - E[R]_{target}|}{(\partial E[R] / \partial w_{price})^2}$ 在量纲和逻辑上完全一致（假设 $\sigma_{\partial}$ 即为偏导数估计的标准误）。
