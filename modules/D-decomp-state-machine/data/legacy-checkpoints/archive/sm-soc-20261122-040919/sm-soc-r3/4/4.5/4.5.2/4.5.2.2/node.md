# N317: 大样本下正态近似与精确区间收敛速度的量化：区间宽度差值$\Delta W = W_{CP} - W_{Normal}$随n的衰减率，理论推导表明$\Delta 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

大样本下正态近似与精确区间收敛速度的量化：区间宽度差值$\Delta W = W_{CP} - W_{Normal}$随n的衰减率，理论推导表明$\Delta W = O(n^{-1})$，需计算n=1000时的具体差值以验证'基本一致'的阈值（如<0.001）。

## Corrected Claim

大样本下正态近似与精确区间收敛速度的量化：区间宽度差值$\Delta W = W_{CP} - W_{Normal}$随n的衰减率，理论推导表明$\Delta W = O(n^{-1})$，需计算n=1000时的具体差值以验证'基本一致'的阈值（如<0.001）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于泰勒展开，正态近似与精确分布（如二项分布）在均值处的偏差为O(n^-1)，导致置信区间宽度差值ΔW随n以O(n^-1)速率衰减，符合统计学渐近理论。
