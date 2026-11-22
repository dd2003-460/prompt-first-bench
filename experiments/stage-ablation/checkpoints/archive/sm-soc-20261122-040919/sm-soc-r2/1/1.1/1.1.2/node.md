# N32: 卖家定价噪声方差分解：$\text{Var}(\epsilon_{seller}) = \sigma^2_{\text{bias}} + \sigma^2_{\

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N5

## Claim

卖家定价噪声方差分解：$\text{Var}(\epsilon_{seller}) = \sigma^2_{\text{bias}} + \sigma^2_{\text{info}}$，其中 $\sigma^2_{\text{bias}}$ 源于损失厌恶导致的系统性高估偏差，$\sigma^2_{\text{info}}$ 源于对同类商品近期成交数据样本量不足导致的估计误差，二者需独立量化以区分行为偏差与信息缺失。

## Corrected Claim

卖家定价噪声方差分解：$\text{Var}(\epsilon_{seller}) = \sigma^2_{\text{bias}} + \sigma^2_{\text{info}}$，其中 $\sigma^2_{\text{bias}}$ 源于损失厌恶导致的系统性高估偏差，$\sigma^2_{\text{info}}$ 源于对同类商品近期成交数据样本量不足导致的估计误差，二者需独立量化以区分行为偏差与信息缺失。

## Evidence

先验知识/题面给定，逻辑校验通过：方差分解公式符合统计学基本定义，行为经济学中损失厌恶与信息不对称导致定价噪声的机制描述符合理论直觉，量纲与逻辑自洽。

## Search Query

decomposition of seller pricing noise variance into bias and information error
