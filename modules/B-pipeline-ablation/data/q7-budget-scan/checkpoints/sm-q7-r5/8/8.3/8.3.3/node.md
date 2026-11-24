# N272: PDU 与 UPS 转换效率链：PDU 效率 η_pdu ≈ 0.98，UPS 在线模式效率 η_ups ≈ 0.92-0.95（取决于负载率，最佳负载率 50

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N129

## Claim

PDU 与 UPS 转换效率链：PDU 效率 η_pdu ≈ 0.98，UPS 在线模式效率 η_ups ≈ 0.92-0.95（取决于负载率，最佳负载率 50-70% 时效率最高），故从 IT 负载到市电输入的总转换效率 η_total ≈ 0.90-0.93，意味着额外电力损耗约为 7-10%，而非 5%

## Corrected Claim

PDU 与 UPS 转换效率链：PDU 效率 η_pdu ≈ 0.98，UPS 在线模式效率 η_ups ≈ 0.92-0.95（取决于负载率，最佳负载率 50-70% 时效率最高），故从 IT 负载到市电输入的总转换效率 η_total ≈ 0.90-0.93，意味着额外电力损耗约为 7-10%，而非 5%

## Evidence

父节点级核验未通过：不完备, 有冗余（工作点A和B本质上是同一物理模型（η_total = η_pdu * η_ups）在不同负载率下的参数取值，存在高度冗余；此外，父节点核心论述是'总效率约为0.90-0.93，损耗7-10%'，子节点C引入了ECO模式（效率高达0.978），这超出了父节点定义的效率范围，破坏了上下文的逻辑一致性（除非父节点明确包含混合模式，否则C属于离群点或矛盾点）。）

## Search Query

ups pdu power conversion efficiency data center tco calculation
