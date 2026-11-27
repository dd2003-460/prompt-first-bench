# N204: 投影2：抵消效应机制量化：定义抵消系数 \(C_{offset}\) 为其他变量（如价格调整、库存变化）对咨询量的反向影响系数。若 \(C_{offset} =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N77

## Claim

投影2：抵消效应机制量化：定义抵消系数 \(C_{offset}\) 为其他变量（如价格调整、库存变化）对咨询量的反向影响系数。若 \(C_{offset} = 0.5\)，则净敏感度 \(S_{net} = S_{gross} - C_{offset} = 0.5\)，从而将置信区间从 ±10% 压缩至 ±5%。需通过多变量回归估计 \(C_{offset}\) 的具体数值。

## Corrected Claim

投影2：抵消效应机制量化：定义抵消系数 \(C_{offset}\) 为其他变量（如价格调整、库存变化）对咨询量的反向影响系数。若 \(C_{offset} = 0.5\)，则净敏感度 \(S_{net} = S_{gross} - C_{offset} = 0.5\)，从而将置信区间从 ±10% 压缩至 ±5%。需通过多变量回归估计 \(C_{offset}\) 的具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

offsetting effect multivariate regression net sensitivity coefficient
