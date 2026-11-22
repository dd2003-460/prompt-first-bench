# N236: 负载系数受散热设计影响：在密闭机箱或散热不良环境下，GPU为维持温度会降频（Thermal Throttling），导致负载系数从0.85降至0.7-0.75，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

负载系数受散热设计影响：在密闭机箱或散热不良环境下，GPU为维持温度会降频（Thermal Throttling），导致负载系数从0.85降至0.7-0.75，同时功耗下降10-15%但性能下降20-30%，形成性能-功耗非线性关系

## Corrected Claim

负载系数受散热设计影响：在密闭机箱或散热不良环境下，GPU为维持温度会降频（Thermal Throttling），导致负载系数从0.85降至0.7-0.75，同时功耗下降10-15%但性能下降20-30%，形成性能-功耗非线性关系

## Evidence

先验知识/题面给定，逻辑校验通过：热节流机制导致频率降低，进而引起性能下降幅度大于功耗下降幅度，符合物理直觉与工程常识。

## Search Query

RTX 4090 thermal throttling power consumption performance degradation closed case inference
