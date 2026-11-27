# N47: 联合概率模型P(Short Cycle | High Price, High Consultation)的具体形式：P(Short Cycle) = P(Con

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

联合概率模型P(Short Cycle | High Price, High Consultation)的具体形式：P(Short Cycle) = P(Consultation | High Price) * P(Short Cycle | Consultation)，其中P(Consultation | High Price) = k_consult(P) / k_consult_base，P(Short Cycle | Consultation) = 1 - e^(-k_deal * T_observation)，用于量化高挂价+高咨询对成交周期的联合影响。

## Corrected Claim

联合概率模型P(Short Cycle | High Price, High Consultation)的具体形式：P(Short Cycle) = P(Consultation | High Price) * P(Short Cycle | Consultation)，其中P(Consultation | High Price) = k_consult(P) / k_consult_base，P(Short Cycle | Consultation) = 1 - e^(-k_deal * T_observation)，用于量化高挂价+高咨询对成交周期的联合影响。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的两个独立条件概率项（P(Consultation | High Price) 和 P(Short Cycle | Consultation)），两者在逻辑上是串联的独立环节，不存在重叠或矛盾。两个子节点共同构成了父节点定义的完整乘积模型，覆盖了所有关键量化部分。每个子节点代表不同的物理/统计含义（注意力捕获 vs 成交转化），并非同一参数的不同取值，因此无冗余。）
