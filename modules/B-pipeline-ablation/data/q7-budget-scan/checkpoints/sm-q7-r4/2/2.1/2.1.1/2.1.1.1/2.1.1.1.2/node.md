# N475: 文件系统开销 (FS_overhead) 的敏感性分析：XFS 的日志区 (log) 和 inode 分配通常占 2-5%。若取保守值 5%，C_eff = 3

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N160

## Claim

文件系统开销 (FS_overhead) 的敏感性分析：XFS 的日志区 (log) 和 inode 分配通常占 2-5%。若取保守值 5%，C_eff = 38 * 16 * 0.95 = 577.6 TB；若取乐观值 2%，C_eff = 38 * 16 * 0.98 = 595.52 TB。最小有效容量 577.6TB 仍满足 ≥500TB 需求，余量为 (577.6 - 500)/500 = 15.52%。

## Corrected Claim

文件系统开销 (FS_overhead) 的敏感性分析：XFS 的日志区 (log) 和 inode 分配通常占 2-5%。若取保守值 5%，C_eff = 38 * 16 * 0.95 = 577.6 TB；若取乐观值 2%，C_eff = 38 * 16 * 0.98 = 595.52 TB。最小有效容量 577.6TB 仍满足 ≥500TB 需求，余量为 (577.6 - 500)/500 = 15.52%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（38*16=608; 608*0.95=577.6; 608*0.98=595.52; (577.6-500)/500=15.52%），XFS开销比例符合工程常识。

## Search Query

XFS filesystem overhead percentage minimum space usage
