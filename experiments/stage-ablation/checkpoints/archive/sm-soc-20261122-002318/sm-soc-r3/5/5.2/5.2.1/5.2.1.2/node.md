# N222: 公式 P(D|H1) = 1 - exp(-Q_buyer * T_window / (T_base * (1-ΔT_decision))) 中的买家流量 Q_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

公式 P(D|H1) = 1 - exp(-Q_buyer * T_window / (T_base * (1-ΔT_decision))) 中的买家流量 Q_buyer 与观察窗口 T_window 的具体数值，需基于平台后台日志中特定品类在 T_window 内的独立访客数(UV)确定。

## Corrected Claim

公式 P(D|H1) = 1 - exp(-Q_buyer * T_window / (T_base * (1-ΔT_decision))) 中的买家流量 Q_buyer 与观察窗口 T_window 的具体数值，通常需基于平台后台日志中特定品类在 T_window 内的独立访客数(UV)确定，具体数值需根据实际业务数据填充。

## Evidence

[质询]该陈述属于经验事实/操作定义，无法从第一性原理推导，且缺乏具体数值或来源支持，存在定义模糊风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

second-hand platform buyer traffic Q_buyer observation window T_window log data
