# N208: IOPS 计算公式修正：IOPS_required = (Total_Data_TB * 1024^2 KB/TB) / (Block_Size_KB * T_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

IOPS 计算公式修正：IOPS_required = (Total_Data_TB * 1024^2 KB/TB) / (Block_Size_KB * T_RTO_seconds)，原 N82 遗漏了 TB 到 KB 的单位换算（1024^2 倍），正确值应为 61,000 * 1,048,576 ≈ 6.4 × 10^10 IOPS，表明原估算存在数量级错误。

## Corrected Claim

IOPS 计算公式修正：IOPS_required = (Total_Data_TB * 1024^2 KB/TB) / (Block_Size_KB * T_RTO_seconds)，原 N82 遗漏了 TB 到 KB 的单位换算（1024^2 倍），正确值应为 61,000 * 1,048,576 ≈ 6.4 × 10^10 IOPS，表明原估算存在数量级错误。

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算系数 1024^2 = 1,048,576 正确，乘法运算 61,000 * 1,048,576 ≈ 6.396 × 10^10 与陈述中的 6.4 × 10^10 一致，量级推导符合物理/数学直觉。
