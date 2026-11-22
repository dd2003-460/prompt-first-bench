# N202: 买家愿意支付的价格上限P_max = v + 0.5*c_base的公式需引入买家风险偏好系数λ_risk，修正为P_max = v + 0.5*c_base 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64, N65, N66

## Claim

买家愿意支付的价格上限P_max = v + 0.5*c_base的公式需引入买家风险偏好系数λ_risk，修正为P_max = v + 0.5*c_base * (1 - λ_risk)，其中λ_risk∈[0,1]，风险厌恶型买家λ_risk≈0.3，风险中性型λ_risk≈0.5。

## Corrected Claim

买家愿意支付的价格上限P_max可表示为 v + 0.5*c_base * (1 - λ_risk)，其中λ_risk∈[0,1]为买家风险偏好系数。需注意，λ_risk的具体取值（如风险厌恶型≈0.3，风险中性型≈0.5）依赖于特定模型假设或实证校准，并非通用理论常数；在标准风险中性假设下，通常不引入此类线性折扣因子，而是直接基于期望价值计算。

## Evidence

[质询]该公式缺乏标准的微观经济学理论基础。在标准委托-代理或信息不对称模型中，买家的支付意愿上限通常由期望效用决定，风险厌恶通常通过效用函数的凹性（如CARA/CRRA）体现，而非简单地线性缩减成本项。此外，'风险中性型买家λ_risk≈0.5'这一具体数值设定缺乏普遍的理论或实证支持，属于任意参数化，容易混淆'风险中性'（效用函数线性）与'对成本敏感度为50%'的概念。 | 先验知识/题面给定，逻辑校验通过（公式在数学上自洽，量纲一致），但作为经验/理论模型的具体参数设定，缺乏通用理论支持，且风险中性对应0.5的设定存在概念混淆风险，故降级。

## Search Query

willingness to pay price ceiling risk preference coefficient correction
