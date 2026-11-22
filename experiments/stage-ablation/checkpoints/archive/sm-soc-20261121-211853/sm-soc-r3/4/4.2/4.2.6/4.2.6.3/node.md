# N104: 权重调整对高溢价卖家（$D > 0.2$）的差异化影响系数：定义边际惩罚强度 $\Delta P_{margin} = \frac{\partial \Delt

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

权重调整对高溢价卖家（$D > 0.2$）的差异化影响系数：定义边际惩罚强度 $\Delta P_{margin} = \frac{\partial \Delta E}{\partial D} = -k_w \Delta w$。当 $D$ 超过阈值 $D_{threshold} = \frac{1}{k_w \Delta w} \times E_{min\_loss}$ 时，曝光损失将超过卖家可承受的流动性下限（通常设定为 5%），导致该部分卖家退出概率显著上升。

## Corrected Claim

权重调整对高溢价卖家（$D > 0.2$）的差异化影响系数：定义边际惩罚强度 $\Delta P_{margin} = \frac{\partial \Delta E}{\partial D} = -k_w \Delta w$。当 $D$ 超过阈值 $D_{threshold} = \frac{1}{k_w \Delta w} \times E_{min\_loss}$ 时，曝光损失将超过卖家可承受的流动性下限（通常设定为 5%），导致该部分卖家退出概率显著上升。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导自洽，量纲一致，阈值定义符合经济直觉（损失超过下限导致退出）。
