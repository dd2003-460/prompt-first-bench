# N72: 温数据顺序读IOPS需求 IOPS_seq = T_peak / Block_Size = 7GB/s / 1MB = 7000 IOPS（若块大小1MB）；若

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

温数据顺序读IOPS需求 IOPS_seq = T_peak / Block_Size = 7GB/s / 1MB = 7000 IOPS（若块大小1MB）；若块大小4MB，则 IOPS_seq = 7GB/s / 4MB = 1750 IOPS；与N27中估算的11-22 IOPS差异巨大，需澄清N27是基于总扫描时长24h而非4h窗口，实际4h窗口内IOPS为7000（1MB块）

## Corrected Claim

温数据顺序读IOPS需求 IOPS_seq = T_peak / Block_Size = 7GB/s / 1MB = 7000 IOPS（若块大小1MB）；若块大小4MB，则 IOPS_seq = 7GB/s / 4MB = 1750 IOPS；与N27中估算的11-22 IOPS差异巨大，需澄清N27是基于总扫描时长24h而非4h窗口，实际4h窗口内IOPS为7000（1MB块）

## Evidence

先验知识/题面给定，逻辑校验通过：7GB/s ÷ 1MB = 7000 IOPS，7GB/s ÷ 4MB = 1750 IOPS，数学推导正确，量纲一致。
