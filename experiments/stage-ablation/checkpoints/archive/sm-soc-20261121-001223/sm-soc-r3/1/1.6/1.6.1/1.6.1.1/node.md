# N129: 联合概率模型的分解项 1：P(Consultation | High Price) 的量化。定义为条件概率 k_consult(P_high) / k_cons

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N47

## Claim

联合概率模型的分解项 1：P(Consultation | High Price) 的量化。定义为条件概率 k_consult(P_high) / k_consult_base，其中 k_consult(P_high) 为高溢价商品的实际咨询率。需通过 A/B 测试或自然实验估计该比值，若比值 > 1.5，则证明高价格本身具有‘注意力捕获’效应，独立于质量信号。

## Corrected Claim

联合概率模型的分解项 1：P(Consultation | High Price) 的量化。定义为条件概率 k_consult(P_high) / k_consult_base，其中 k_consult(P_high) 为高溢价商品的实际咨询率。需通过 A/B 测试或自然实验估计该比值，若比值 > 1.5，则证明高价格本身具有‘注意力捕获’效应，独立于质量信号。

## Evidence

先验知识/题面给定，逻辑校验通过
