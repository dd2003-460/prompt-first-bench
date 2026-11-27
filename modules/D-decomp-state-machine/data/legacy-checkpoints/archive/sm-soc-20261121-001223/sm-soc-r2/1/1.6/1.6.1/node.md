# N47: 联合概率模型P(Short Cycle | High Price, High Consultation)的具体形式：P(Short Cycle) = P(Con

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

联合概率模型P(Short Cycle | High Price, High Consultation)的具体形式：P(Short Cycle) = P(Consultation | High Price) * P(Short Cycle | Consultation)，其中P(Consultation | High Price) = k_consult(P) / k_consult_base，P(Short Cycle | Consultation) = 1 - e^(-k_deal * T_observation)，用于量化高挂价+高咨询对成交周期的联合影响。

## Corrected Claim

联合概率模型P(Short Cycle | High Price, High Consultation)的具体形式：P(Short Cycle) = P(Consultation | High Price) * P(Short Cycle | Consultation)，其中P(Consultation | High Price) = k_consult(P) / k_consult_base，P(Short Cycle | Consultation) = 1 - e^(-k_deal * T_observation)，用于量化高挂价+高咨询对成交周期的联合影响。

## Evidence

先验知识/题面给定，逻辑校验通过
