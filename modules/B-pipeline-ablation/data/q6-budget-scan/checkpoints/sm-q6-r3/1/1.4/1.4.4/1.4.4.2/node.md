# N179: 在激进预留工作点（高性低成），基于 $B_{peak}=370 \text{ Mbps}$，仅预留 10% 余量即 $B_{purchase} = 370 \t

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

在激进预留工作点（高性低成），基于 $B_{peak}=370 \text{ Mbps}$，仅预留 10% 余量即 $B_{purchase} = 370 \times 1.1 = 407 \text{ Mbps}$，向上取整至 400 Mbps，若实际峰值超过 400 Mbps 则触发拥塞控制导致 P99 延迟上升，需量化该风险下的延迟惩罚值。

## Corrected Claim

在激进预留工作点，基于 $B_{peak}=370 \text{ Mbps}$，预留 10% 余量计算得 $B_{purchase} = 407 \text{ Mbps}$。若实际购买带宽限制为 400 Mbps（向下取整或特定档位），则存在 7 Mbps 的潜在超额风险，若实际峰值超过 400 Mbps 将触发拥塞控制导致 P99 延迟上升，需量化该风险下的延迟惩罚值。

## Evidence

[质询]数值逻辑矛盾：407 Mbps 向上取整（ceiling）应为 410 Mbps（若按10Mbps粒度）或至少大于407，而 400 Mbps 小于 407 Mbps，属于向下取整或截断，与‘向上取整’表述矛盾；且‘激进预留’通常意味着更小的余量或更低的购买量，但此处计算逻辑存在内部不一致。 | 先验知识/题面给定，逻辑校验发现数值取整方向与描述矛盾（407 -> 400 为向下取整），且缺乏外部来源支持具体延迟惩罚值。
