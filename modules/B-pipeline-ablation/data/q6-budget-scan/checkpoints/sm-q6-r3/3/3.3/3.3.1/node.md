# N73: 预留带宽模式下的峰值带宽需求 $B_{reserved}$ 计算：$B_{reserved} = B_{avg} \times K_{peak} \times 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

预留带宽模式下的峰值带宽需求 $B_{reserved}$ 计算：$B_{reserved} = B_{avg} \times K_{peak} \times (1 + M_{safety})$，其中 $B_{avg} = 2\text{TB}/86400\text{s} \approx 0.23\text{Gbps}$，$K_{peak} \in [1.5, 2.5]$，安全边际 $M_{safety}$ 通常取 10%-20% 以应对突发流量，故 $B_{reserved} \in [0.35, 0.7]\text{Gbps}$。

## Corrected Claim

预留带宽模式下的峰值带宽需求 $B_{reserved}$ 计算：$B_{reserved} = B_{avg} \times K_{peak} \times (1 + M_{safety})$，其中 $B_{avg} = 2\text{TB}/86400\text{s} \approx 0.23\text{Gbps}$，$K_{peak} \in [1.5, 2.5]$，安全边际 $M_{safety}$ 通常取 10%-20% 以应对突发流量，故 $B_{reserved} \in [0.35, 0.7]\text{Gbps}$。

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性不足：子节点2引入的 $K_{burst}$ 与父节点公式中的 $K_{peak}$ 概念高度重叠且定义冲突（父节点用小时/天级峰值，子节点用分钟/小时级），导致参数体系混乱；2. 完备性缺失：父节点核心是计算 $B_{reserved}$，但子节点3讨论的是“超售风险成本”，这属于后果评估而非计算过程，偏离了父节点主题；3. 逻辑断层：子节点1推导 $M_{safety}$ 合理，但子节点2试图修改 $K_{peak}$ 的定义而未明确其与父节点 $K_{peak}$ 的替换或叠加关系，导致公式无法闭环。）
