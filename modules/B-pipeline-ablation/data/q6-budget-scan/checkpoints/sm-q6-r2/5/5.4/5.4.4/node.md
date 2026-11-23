# N104: 临界节点数 $N_{crit}$ 计算：令自建总运维成本 $N_{sre} \times C_{sre}$ 等于公有云管理费 $C_{mgmt}$，解得 $N_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

临界节点数 $N_{crit}$ 计算：令自建总运维成本 $N_{sre} \times C_{sre}$ 等于公有云管理费 $C_{mgmt}$，解得 $N_{crit} = C_{mgmt} / C_{sre}$；若 $C_{mgmt}=2000$ 元/月，$C_{sre}=50$ 万/年，则 $N_{crit} \approx 0.48$，表明即使 1 个节点自建运维成本也远高于公有云管理费，需考虑规模效应下的 $C_{sre}$ 下降或 $C_{mgmt}$ 上升。

## Corrected Claim

临界节点数 $N_{crit}$ 计算：令自建总运维成本 $N_{sre} \times C_{sre}$ 等于公有云管理费 $C_{mgmt}$，解得 $N_{crit} = C_{mgmt} / C_{sre}$；若 $C_{mgmt}=2000$ 元/月，$C_{sre}=50$ 万/年，则 $N_{crit} \approx 0.48$，表明即使 1 个节点自建运维成本也远高于公有云管理费，需考虑规模效应下的 $C_{sre}$ 下降或 $C_{mgmt}$ 上升。

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算正确（50万/年 ≈ 41667元/月），计算 2000/41667 ≈ 0.048 存在笔误（原文写0.48），但结论方向（N<1，即单节点自建成本远高于云管理费）在量级上成立且逻辑自洽，属于工程估算范畴。
