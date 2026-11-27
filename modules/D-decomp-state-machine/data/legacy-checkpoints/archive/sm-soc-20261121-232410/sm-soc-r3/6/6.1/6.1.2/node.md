# N203: 因果方向检验：通过Granger因果检验或滞后分析，若Premium_t对CTR_{t+1}的预测系数显著（β=-0.2, p<0.01）而CTR_t对Prem

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

因果方向检验：通过Granger因果检验或滞后分析，若Premium_t对CTR_{t+1}的预测系数显著（β=-0.2, p<0.01）而CTR_t对Premium_{t+1}不显著，则确认平台算法对高溢价的惩罚是因果机制，而非反向选择。

## Corrected Claim

因果方向检验：通过Granger因果检验或滞后分析，若Premium_t对CTR_{t+1}的预测系数显著（β=-0.2, p<0.01）而CTR_t对Premium_{t+1}不显著，则确认平台算法对高溢价的惩罚是因果机制，而非反向选择。

## Evidence

先验知识/题面给定，逻辑校验通过：Granger因果检验通过比较双向预测系数显著性来排除反向选择，符合计量经济学因果推断的基本逻辑。
