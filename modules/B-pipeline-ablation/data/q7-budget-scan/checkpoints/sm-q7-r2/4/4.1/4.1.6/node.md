# N101: HDD RAID6 重建窗口 (W_HDD) 量化：对于 18TB HDD，RAID6 重建时间 W_HDD ≈ (18TB / 150MB/s) / 3600

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24, N25, N26

## Claim

HDD RAID6 重建窗口 (W_HDD) 量化：对于 18TB HDD，RAID6 重建时间 W_HDD ≈ (18TB / 150MB/s) / 3600 ≈ 33.3 小时（受限于机械寻道和带宽）

## Corrected Claim

HDD RAID6 重建窗口 (W_HDD) 量化：对于 18TB HDD，RAID6 重建时间 W_HDD ≈ (18TB / 150MB/s) / 3600 ≈ 33.3 小时（受限于机械寻道和带宽）

## Evidence

先验知识/题面给定，逻辑校验通过：18TB / 150MB/s ≈ 120,000秒 ≈ 33.3小时，计算无误且符合HDD RAID6重建的典型量级
