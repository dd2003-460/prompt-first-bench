# N22: 平台福利变化量化：GMV 增长 ΔGMV = Q_short * P_new - Q_base * P_base；若平台抽成率为 r，则平台收入增量 ΔRev 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

平台福利变化量化：GMV 增长 ΔGMV = Q_short * P_new - Q_base * P_base；若平台抽成率为 r，则平台收入增量 ΔRev = r * ΔGMV - 运营成本 ΔC。

## Corrected Claim

平台福利变化量化：GMV 增长 ΔGMV = Q_short * P_new - Q_base * P_base；若平台抽成率为 r，则平台收入增量 ΔRev = r * ΔGMV - 运营成本 ΔC。

## Evidence

父节点级核验未通过：不完备（子节点之间正交，分别处理了抽成率和运营成本。但父节点公式中明确包含 'Q_short', 'P_new', 'Q_base', 'P_base' 以及 'ΔGMV' 的计算，子节点完全忽略了 GMV 增长部分的量化（即供需和价格变化），导致分解不完备。）
