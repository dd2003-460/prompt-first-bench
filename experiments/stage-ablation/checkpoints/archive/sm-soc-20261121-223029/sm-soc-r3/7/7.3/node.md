# N114: 成交周期 T_cycle 与高意愿买家到达率 λ_arrival 的关系：T_cycle ≈ 1 / (λ_arrival * P(W > P_ask))，其中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

成交周期 T_cycle 与高意愿买家到达率 λ_arrival 的关系：T_cycle ≈ 1 / (λ_arrival * P(W > P_ask))，其中 λ_arrival 为平台单位时间访客数，P(W > P_ask) 为支付意愿高于挂价的概率；该公式量化了为何高溢价（降低 P(W>P_ask)）可能在特定流量密度下反而因减少无效咨询而缩短平均等待时间。

## Corrected Claim

成交周期 T_cycle 与高意愿买家到达率 λ_arrival 的关系：T_cycle ≈ 1 / (λ_arrival * P(W > P_ask))，其中 λ_arrival 为平台单位时间访客数，P(W > P_ask) 为支付意愿高于挂价的概率；该公式量化了为何高溢价（降低 P(W>P_ask)）可能在特定流量密度下反而因减少无效咨询而缩短平均等待时间。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应公式中的三个核心变量/机制：1. 概率项 P(W>P_ask) 的分布估计；2. 流量项 λ_arrival 的分解与修正；3. 整体函数 T_cycle(δ) 的极值条件与临界点推导。三者逻辑独立，分别处理公式的不同组成部分，且共同覆盖了从参数估计到机制验证的完整链条，无重复或矛盾。）

## Search Query

arrival rate and transaction time relationship in market models
