# N170: 在价格弹性系数 β_price=1.5 且价格降幅为 15%（对应 P_new=P_base*0.85）的基准工作点下，短期成交量 Q_short 的相对变化量

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

在价格弹性系数 β_price=1.5 且价格降幅为 15%（对应 P_new=P_base*0.85）的基准工作点下，短期成交量 Q_short 的相对变化量为 15% * 1.5 = 22.5%，即 Q_short = 1.225 * Q_base。

## Corrected Claim

在价格弹性系数 β_price=1.5 且价格降幅为 15%（对应 P_new=P_base*0.85）的基准工作点下，短期成交量 Q_short 的相对变化量为 15% * 1.5 = 22.5%，即 Q_short = 1.225 * Q_base。

## Evidence

先验知识/题面给定，逻辑校验通过：根据价格弹性定义 ΔQ/Q = β * (ΔP/P)，代入 β=1.5 和 ΔP/P=-15% 得 ΔQ/Q = 1.5 * 15% = 22.5%，故 Q_new = 1.225 * Q_base，计算无误。
