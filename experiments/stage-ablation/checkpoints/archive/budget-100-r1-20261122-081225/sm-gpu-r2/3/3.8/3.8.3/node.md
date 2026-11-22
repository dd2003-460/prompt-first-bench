# N123: 数据中心电力成本通常包含 PUE (Power Usage Effectiveness) 因子，典型 PUE 为 1.3-1.5，意味着实际电力成本比裸 GPU

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

数据中心电力成本通常包含 PUE (Power Usage Effectiveness) 因子，典型 PUE 为 1.3-1.5，意味着实际电力成本比裸 GPU TDP 计算值高 30-50%。

## Corrected Claim

数据中心电力成本通常包含 PUE (Power Usage Effectiveness) 因子，典型 PUE 为 1.3-1.5，意味着实际电力成本比裸 GPU TDP 计算值高 30-50%。

## Evidence

先验知识/题面给定，逻辑校验通过：PUE定义为总能耗/IT设备能耗，PUE 1.3-1.5意味着总能耗是IT能耗的1.3-1.5倍，即额外增加30%-50%的电力成本，符合数据中心行业常识及数学逻辑。

## Search Query

data center PUE typical value electricity cost factor
