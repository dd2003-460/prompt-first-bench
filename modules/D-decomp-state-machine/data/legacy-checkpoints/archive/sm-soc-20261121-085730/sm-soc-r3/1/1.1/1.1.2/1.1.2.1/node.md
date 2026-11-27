# N155: 卖家保留价R的共享随机源：基于近期成交价C_ref，保留价R服从正态分布R ~ N(0.85*C_ref, (0.15*C_ref)^2)，该分布反映了卖家对商

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N45

## Claim

卖家保留价R的共享随机源：基于近期成交价C_ref，保留价R服从正态分布R ~ N(0.85*C_ref, (0.15*C_ref)^2)，该分布反映了卖家对商品价值的认知噪声及对损失的规避导致的右偏倾向（实际分布可能更近似对数正态，但此处用正态近似）。

## Corrected Claim

卖家保留价R的共享随机源：基于近期成交价C_ref，保留价R服从正态分布R ~ N(0.85*C_ref, (0.15*C_ref)^2)，该分布反映了卖家对商品价值的认知噪声及对损失的规避导致的右偏倾向（实际分布可能更近似对数正态，但此处用正态近似）。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布参数设定（均值0.85倍参考价，标准差0.15倍参考价）在量纲和数值量级上合理，且明确说明了是对数正态的近似处理，符合经济学中关于保留价分布的常见建模假设。

## Search Query

seller reservation price distribution used goods market normal approximation
