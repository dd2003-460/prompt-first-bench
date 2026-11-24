# N159: L_transmission 的带宽瓶颈分析：L_transmission = Object_Size / Effective_Bandwidth，其中 Eff

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

L_transmission 的带宽瓶颈分析：L_transmission = Object_Size / Effective_Bandwidth，其中 Effective_Bandwidth 受限于用户端上行/下行速率及 POP 出口带宽；对于 1.5MB 对象，若用户端带宽为 100Mbps，L_transmission ≈ 120ms，但 P99 用户可能带宽更低（如 50Mbps），导致 L_transmission 升至 240ms，需考虑长尾用户影响。

## Corrected Claim

L_transmission 的带宽瓶颈分析：L_transmission = Object_Size / Effective_Bandwidth，其中 Effective_Bandwidth 受限于用户端上行/下行速率及 POP 出口带宽；对于 1.5MB 对象，若用户端带宽为 100Mbps，L_transmission ≈ 120ms，但 P99 用户可能带宽更低（如 50Mbps），导致 L_transmission 升至 240ms，需考虑长尾用户影响。

## Evidence

先验知识/题面给定，逻辑校验通过：1.5MB * 8 / 100Mbps = 120ms，1.5MB * 8 / 50Mbps = 240ms，计算准确且符合物理直觉。
