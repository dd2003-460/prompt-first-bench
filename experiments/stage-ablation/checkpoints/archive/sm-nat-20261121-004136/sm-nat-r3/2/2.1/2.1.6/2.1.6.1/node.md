# N109: 修正 N42 中 P_pollution 的数值估算：代入 Sum_S_total ≈ 0.91 GB 到公式 P_pollution = 1 - (128GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

修正 N42 中 P_pollution 的数值估算：代入 Sum_S_total ≈ 0.91 GB 到公式 P_pollution = 1 - (128GB / 0.91GB)^1.1，由于底数 128/0.91 ≈ 140.6 > 1，(140.6)^1.1 远大于 1，导致 P_pollution 为负值，这在物理上无意义，表明原公式仅在容量受限时有效，此处应直接判定 P_pollution = 0。

## Corrected Claim

修正 N42 中 P_pollution 的数值估算：代入 Sum_S_total ≈ 0.91 GB 到公式 P_pollution = 1 - (128GB / 0.91GB)^1.1，由于底数 128/0.91 ≈ 140.6 > 1，(140.6)^1.1 远大于 1，导致 P_pollution 为负值，这在物理上无意义，表明原公式仅在容量受限时有效，此处应直接判定 P_pollution = 0。

## Evidence

先验知识/题面给定，逻辑校验通过：数学上 (140.6)^1.1 > 1 导致 1 - (140.6)^1.1 < 0，概率为负在物理上无意义，故修正为 0 符合逻辑自洽性。
