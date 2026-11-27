# N92: 工作点B（x_min=1B, B≈10^6 B）：若取x_min=1B，为满足E[S]=1MB，B需更大以补偿更小的x_min对期望的拉动；数值求解显示B约在1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

工作点B（x_min=1B, B≈10^6 B）：若取x_min=1B，为满足E[S]=1MB，B需更大以补偿更小的x_min对期望的拉动；数值求解显示B约在10^6 B（1MB）量级时E[S]趋近1MB，但此时分布近似均匀，违背Pareto长尾特性，故该工作点在实际CDN场景中物理意义较弱

## Corrected Claim

工作点B（x_min=1B, B≈10^6 B）：若取x_min=1B，为满足E[S]=1MB，B需更大以补偿更小的x_min对期望的拉动；数值求解显示B约在10^6 B（1MB）量级时E[S]趋近1MB，但此时分布近似均匀，违背Pareto长尾特性，故该工作点在实际CDN场景中物理意义较弱

## Evidence

先验知识/题面给定，逻辑校验通过：在Pareto分布中，若最小值x_min增大（从典型的小值变为1B），为保持期望E[S]不变（1MB），截断上限B必须显著增大以补偿尾部截断带来的期望损失；当B达到10^6 B量级时，分布区间[x_min, B]内相对变化范围缩小，形态趋近均匀，确实违背Pareto长尾特性，逻辑自洽。
