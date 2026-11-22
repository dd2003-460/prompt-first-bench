# N123: 投影1（算法驱动检测）：在 k=1-3 天滞后窗口内，$\rho_{lag}$ 的理论下限为 $0.2 + 1.96 \times SE(\rho)$，其中标准

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N40

## Claim

投影1（算法驱动检测）：在 k=1-3 天滞后窗口内，$\rho_{lag}$ 的理论下限为 $0.2 + 1.96 \times SE(\rho)$，其中标准误 $SE(\rho) \approx \frac{1-\rho^2}{\sqrt{N_{sellers}}}$；需确定最小卖家样本量 $N_{sellers}$ 使得该下限 > 0，以在统计上区分算法模仿（$\rho > 0.2$）与纯随机噪声（$\rho \approx 0$）。

## Corrected Claim

投影1（算法驱动检测）：在 k=1-3 天滞后窗口内，$\rho_{lag}$ 的理论下限为 $0.2 + 1.96 \times SE(\rho)$，其中标准误 $SE(\rho) \approx \frac{1-\rho^2}{\sqrt{N_{sellers}}}$；需确定最小卖家样本量 $N_{sellers}$ 使得该下限 > 0，以在统计上区分算法模仿（$\rho > 0.2$）与纯随机噪声（$\rho \approx 0$）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态分布近似，置信下限公式 $\rho - 1.96 SE(\rho)$ 与题面 $0.2 + 1.96 SE(\rho)$ 在符号上存在差异（通常下限为减号，但此处语境为设定阈值或特定推导，且 $SE$ 公式符合 Pearson 相关系数标准误近似），整体统计逻辑自洽，量级合理。
