# N163: 工作点B (20x32TB NVMe) 的RAID-5有效容量计算：物理容量640TB，RAID-5奇偶校验开销为1/N_disks (1/20=5%)，有效容

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

工作点B (20x32TB NVMe) 的RAID-5有效容量计算：物理容量640TB，RAID-5奇偶校验开销为1/N_disks (1/20=5%)，有效容量 = 640TB * (1 - 0.05) = 608TB；若考虑文件系统元数据开销(~5%)，最终可用容量 = 608TB * 0.95 ≈ 577.6TB，而非题目假设的500TB，需重新核算单位成本。

## Corrected Claim

工作点B (20x32TB NVMe) 的RAID-5有效容量计算：物理容量640TB，RAID-5奇偶校验开销为1/N_disks (1/20=5%)，有效容量 = 640TB * (1 - 0.05) = 608TB；若考虑文件系统元数据开销(~5%)，最终可用容量 = 608TB * 0.95 ≈ 577.6TB，而非题目假设的500TB，需重新核算单位成本。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-5有效容量计算公式正确（640TB * 19/20 = 608TB），文件系统开销估算合理（~5%），最终可用容量约577.6TB的计算无误。
