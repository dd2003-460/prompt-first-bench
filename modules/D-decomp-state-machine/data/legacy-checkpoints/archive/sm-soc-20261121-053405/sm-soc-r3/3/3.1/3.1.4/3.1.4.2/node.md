# N156: 偏导数 $\partial P_{consult} / \partial \tau$ 的实证估计方法：采用逻辑回归模型 $\text{logit}(P_{con

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

偏导数 $\partial P_{consult} / \partial \tau$ 的实证估计方法：采用逻辑回归模型 $\text{logit}(P_{consult}) = \alpha + \beta_\tau \tau + \beta_x X + \epsilon_{log}$，其中 $\tau$ 为信息透明度指数（如商品描述完整度、图片数量、卖家信用分的标准化加权值），$X$ 为控制变量（价格、品类、用户等级）；$\beta_\tau$ 在概率尺度上的偏导数需通过边际效应（Marginal Effects）计算，即 $\partial P_{consult} / \partial \tau = \beta_\tau \cdot P_{consult}(1-P_{consult})$。

## Corrected Claim

偏导数 $\partial P_{consult} / \partial \tau$ 的实证估计方法：采用逻辑回归模型 $\text{logit}(P_{consult}) = \alpha + \beta_\tau \tau + \beta_x X + \epsilon_{log}$，其中 $\tau$ 为信息透明度指数（如商品描述完整度、图片数量、卖家信用分的标准化加权值），$X$ 为控制变量（价格、品类、用户等级）；$\beta_\tau$ 在概率尺度上的偏导数需通过边际效应（Marginal Effects）计算，即 $\partial P_{consult} / \partial \tau = \beta_\tau \cdot P_{consult}(1-P_{consult})$。

## Evidence

先验知识/题面给定，逻辑校验通过：逻辑回归模型中，因变量为概率P，自变量为线性预测子，根据链式法则，概率对自变量的偏导数确实等于回归系数乘以P(1-P)，公式推导正确。
