# N260: 流量加权系数 w 对成交量 Q_new 的弹性系数 ε_Qw = (ΔQ_new/Q_new)/(Δw/w) 需量化；若 ε_Qw = 0.5，则 w 增加 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

流量加权系数 w 对成交量 Q_new 的弹性系数 ε_Qw = (ΔQ_new/Q_new)/(Δw/w) 需量化；若 ε_Qw = 0.5，则 w 增加 10% 仅带来 Q_new 增加 5%，这限制了 w* 的上界，防止过度补贴导致效用负增长。

## Corrected Claim

流量加权系数 w 对成交量 Q_new 的弹性系数 ε_Qw = (ΔQ_new/Q_new)/(Δw/w) 需量化；若 ε_Qw = 0.5，则 w 增加 10% 仅带来 Q_new 增加 5%，这限制了 w* 的上界，防止过度补贴导致效用负增长。

## Evidence

先验知识/题面给定，逻辑校验通过：弹性系数定义及数值示例（0.5 * 10% = 5%）符合数学逻辑，且作为模型假设/约束条件在逻辑上自洽。
