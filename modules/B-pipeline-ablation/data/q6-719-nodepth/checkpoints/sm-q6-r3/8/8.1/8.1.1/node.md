# N375: 自建策略工作点1（高CapEx低OpEx）：采用全闪存SSD存储（30TB/POP），单POP CapEx为20万元（服务器+存储+网络），10 POP总Cap

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N131

## Claim

自建策略工作点1（高CapEx低OpEx）：采用全闪存SSD存储（30TB/POP），单POP CapEx为20万元（服务器+存储+网络），10 POP总CapEx 200万元，按5年直线折旧 Annualized_CapEx = 200万/5 = 40万元/年；OpEx_Monthly = 10.5万元/月，Infra_Annualized = 40万 + 126万 = 166万元/年。

## Corrected Claim

自建策略工作点1（高CapEx低OpEx）：采用全闪存SSD存储（30TB/POP），单POP CapEx为20万元（服务器+存储+网络），10 POP总CapEx 200万元，按5年直线折旧 Annualized_CapEx = 200万/5 = 40万元/年；OpEx_Monthly = 10.5万元/月，Infra_Annualized = 40万 + 126万 = 166万元/年。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算（20万*10=200万，200万/5=40万，10.5万*12=126万，40万+126万=166万）完全正确，量级符合自建IDC基础设施成本常识。

## Search Query

Alibaba Cloud ECS i2 instance price SSD 30TB 2024
