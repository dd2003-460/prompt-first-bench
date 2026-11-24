# N480: 实际每日写入放大系数(DWAF)修正：NVMe SSD在TRIM支持良好且文件系统对齐的情况下，DWAF通常为1.1-1.3。假设DWAF=1.2，则实际每日写

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N162

## Claim

实际每日写入放大系数(DWAF)修正：NVMe SSD在TRIM支持良好且文件系统对齐的情况下，DWAF通常为1.1-1.3。假设DWAF=1.2，则实际每日写入量 W_actual = W_logical * 1.2。若逻辑写入量为0.5 DWPD，实际磨损为0.6 DWPD。

## Corrected Claim

实际每日写入放大系数(DWAF)修正：NVMe SSD在TRIM支持良好且文件系统对齐的情况下，DWAF通常为1.1-1.3。假设DWAF=1.2，则实际每日写入量 W_actual = W_logical * 1.2。若逻辑写入量为0.5 DWPD，实际磨损为0.6 DWPD。

## Evidence

先验知识/题面给定，逻辑校验通过
