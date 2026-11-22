# N80: 匹配量 Q_matched 的约束：Q_matched ≤ min(Q_demand, Q_supply)；干预若仅降低 P_ask 而不增加 Q_supply

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

匹配量 Q_matched 的约束：Q_matched ≤ min(Q_demand, Q_supply)；干预若仅降低 P_ask 而不增加 Q_supply（如通过激励卖家降价），则 Q_matched 不变，ΔCS_buyer 可能为负

## Corrected Claim

匹配量 Q_matched 的约束：Q_matched ≤ min(Q_demand, Q_supply)；干预若仅降低 P_ask 而不增加 Q_supply（如通过激励卖家降价），则 Q_matched 不变，ΔCS_buyer 可能为负

## Evidence

父节点级核验未通过：不完备（子节点分别定义了约束中的两个上限项（Q_supply, Q_demand）以及后果指标（ΔCS_buyer），三者概念正交且无冗余。但在完备性上存在缺失：父节点核心逻辑是“干预仅降低P_ask而不增加Q_supply时，Q_matched不变”，这隐含了市场处于“供给受限”（Q_supply < Q_demand）的状态。子节点1和2仅给出了Q_supply和Q_demand的通用构成公式，未明确界定或约束当前市场处于供给受限状态这一前提条件，导致无法从子节点直接推导出父节点中“Q_matched不变”的结论（若市场为需求受限，降低P_ask通常会增加Q_matched）。）
