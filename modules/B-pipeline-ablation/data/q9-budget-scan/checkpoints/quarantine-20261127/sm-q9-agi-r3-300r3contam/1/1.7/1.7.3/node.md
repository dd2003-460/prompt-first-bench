# N50: HITL 介入的边际成本函数：C_hitl = T_human * R_hourly * (1 - IR_auto)，其中 T_human 为平均审核耗时（分钟

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13, N14, N19

## Claim

HITL 介入的边际成本函数：C_hitl = T_human * R_hourly * (1 - IR_auto)，其中 T_human 为平均审核耗时（分钟），R_hourly 为人力时薪，IR_auto 为自动拦截率，用于量化不同阈值下的总运营成本。

## Corrected Claim

HITL 介入的边际成本函数：C_hitl = T_human * R_hourly * (1 - IR_auto)，其中 T_human 为平均审核耗时（分钟），R_hourly 为人力时薪，IR_auto 为自动拦截率，用于量化不同阈值下的总运营成本。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个核心变量（T_human, IR_auto, R_hourly）及整体函数的敏感性分析，彼此独立无重叠。覆盖完整，且各子节点包含具体的建模逻辑或参数取值，不属于简单参数列举导致的冗余。）

## Search Query

human-in-the-loop cost function marginal cost review time
