# N73: 随机偏好噪声（Random Preference Noise）对成交周期的非线性影响：定义噪声强度 ε_noise。当卖家定价包含随机噪声 ε_noise 时，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

随机偏好噪声（Random Preference Noise）对成交周期的非线性影响：定义噪声强度 ε_noise。当卖家定价包含随机噪声 ε_noise 时，实际有效溢价 δ_eff = δ_signal + ε_noise。若 ε_noise 的标准差 σ_noise > 5%，则会导致约 20%-30% 的潜在买家因价格波动超出其心理阈值（θ_buyer）而流失，从而抵消信号筛选带来的转化提升，导致成交周期并未如理论预期般显著缩短，需通过控制 ε_noise 来验证因果链。

## Corrected Claim

随机偏好噪声（Random Preference Noise）对成交周期存在非线性影响：当卖家定价包含随机噪声 ε_noise 时，实际有效溢价 δ_eff = δ_signal + ε_noise。若噪声强度超过买家心理阈值容忍度，会导致部分潜在买家流失，从而抵消信号筛选带来的转化提升，需通过控制 ε_noise 来验证因果链。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（σ_noise > 5% 导致 20%-30% 买家流失），这属于特定市场或模型下的经验事实，无法从第一性原理严格推导，且参考来源完全未涉及此内容，存在数值缺乏实证支持的风险。 | 参考来源[1][2]讨论的是Web服务日志中的标签噪声过滤，与二手交易定价噪声及成交周期无关，属于无关来源；该事实为经验性量化结论，逻辑自洽但缺乏直接来源支持，依据经验事实排除条款降级。

## Retrieval Sources

- {'url': 'https://arxiv.org/html/2511.05808v2&rut=c37c5ed225b3c987c4d300c93adaa4577befffe290d524a1e3091f70e452393b', 'type': 'ddg', 'title': 'Turning Noise into Value: Uncovering Service Preferences from Ambiguous ...'}
- {'url': 'https://arxiv.org/abs/2511.05808v2&rut=885db15b64cec0d8c38726808212b1e29ba89f9165337f7a083dff37141050c9', 'type': 'ddg', 'title': '[2511.05808v2] Turning Noise into Value: Uncovering Service Preferences ...'}
