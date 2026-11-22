# N365: 弹性系数 ε_T 的分解：ε_T = (∂T_cycle/∂Impression) * (Impression/T_cycle)，需分别估计曝光对成交概率 P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N123

## Claim

弹性系数 ε_T 的分解：ε_T = (∂T_cycle/∂Impression) * (Impression/T_cycle)，需分别估计曝光对成交概率 P_deal 的边际效应 (∂P_deal/∂Impression) 和成交概率对周期的杠杆效应 (∂T_cycle/∂P_deal)，二者相乘得到总弹性。

## Corrected Claim

弹性系数 ε_T 的分解：ε_T = (∂T_cycle/∂Impression) * (Impression/T_cycle)，需分别估计曝光对成交概率 P_deal 的边际效应 (∂P_deal/∂Impression) 和成交概率对周期的杠杆效应 (∂T_cycle/∂P_deal)，二者相乘得到总弹性。

## Evidence

先验知识/题面给定，逻辑校验通过：该分解符合微积分链式法则及弹性定义（ε = (∂Y/∂X) * (X/Y)），数学推导自洽。

## Search Query

elasticity of transaction cycle to exposure in online marketplaces
