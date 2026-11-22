# N68: 下游投影3：平台算法信号权重的自适应调整。平台算法为维持转化率，会调整推荐权重 w_signal。w_signal_new = w_signal_old * (

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N14

## Claim

下游投影3：平台算法信号权重的自适应调整。平台算法为维持转化率，会调整推荐权重 w_signal。w_signal_new = w_signal_old * (1 + β * (CTR_old - CTR_new))，其中 β 为算法学习率。若透明度导致点击率 CTR 下降，平台可能降低'快速成交'标签的权重，从而间接削弱 k=0.6 的原始效应，形成新的均衡点。

## Corrected Claim

下游投影3：平台算法信号权重的自适应调整。平台算法为维持转化率，会调整推荐权重 w_signal。w_signal_new = w_signal_old * (1 + β * (CTR_old - CTR_new))，其中 β 为算法学习率。若透明度导致点击率 CTR 下降，平台可能降低'快速成交'标签的权重，从而间接削弱 k=0.6 的原始效应，形成新的均衡点。

## Evidence

先验知识/题面给定，逻辑校验通过
