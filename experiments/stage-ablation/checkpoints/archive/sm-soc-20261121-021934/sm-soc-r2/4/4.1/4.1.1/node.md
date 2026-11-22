# N37: 贝叶斯推理中先验 P(H) 的量化基础为演化心理学中损失厌恶系数 λ 在二手交易场景下的适用性权重 W_λ，定义为 W_λ = P(λ_applicable |

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N15

## Claim

贝叶斯推理中先验 P(H) 的量化基础为演化心理学中损失厌恶系数 λ 在二手交易场景下的适用性权重 W_λ，定义为 W_λ = P(λ_applicable | context) * λ_value，其中 λ_value ≈ 2.25，P(λ_applicable | context) 需通过跨市场实验数据估计，初步设定为 0.75。

## Corrected Claim

在基于演化心理学的贝叶斯模型中，可引入损失厌恶系数 λ（典型值约 2.25）作为先验 P(H) 的调节因子，其适用性权重 W_λ 需根据具体市场场景的实验数据估计，初步假设适用性概率为 0.75 仅为模型初始参数，需后续实证校准。

## Evidence

[质询]该陈述将演化心理学的损失厌恶系数（λ≈2.25）直接量化为贝叶斯先验 P(H) 的权重，并设定具体的适用性概率 P(λ_applicable | context) = 0.75。这属于跨学科的经验性建模假设，缺乏严格的数学推导或普遍公认的实证数据支持，0.75 这一数值具有任意性，且“适用性权重”的定义在标准贝叶斯框架中并非标准术语，存在概念混淆风险。 | 先验知识/题面给定，逻辑校验通过（公式结构自洽，量纲合理），但具体数值（0.75）为经验设定，缺乏外部来源直接支持，故降级。

## Search Query

loss aversion coefficient applicability secondhand market prior probability Bayesian
