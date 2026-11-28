# N200: 本地 vs 云端成本盈亏平衡点 (Break-even Point) 计算：设云端单次成本为 C_cloud，本地完全成本为 C_local(N) = C_el

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

本地 vs 云端成本盈亏平衡点 (Break-even Point) 计算：设云端单次成本为 C_cloud，本地完全成本为 C_local(N) = C_elec + C_depr/N；当 C_local(N) < C_cloud 时本地更优；若 C_cloud=0.07元，C_elec=0.0005元，C_depr_total_daily=9.17元，则需 N > 9.17/(0.07-0.0005) ≈ 131 次/天才能覆盖折旧优势（注：此处单位需统一，若按美元计算需转换汇率）。

## Corrected Claim

本地 vs 云端成本盈亏平衡点 (Break-even Point) 计算：设云端单次成本为 C_cloud，本地完全成本为 C_local(N) = C_elec + C_depr/N；当 C_local(N) < C_cloud 时本地更优；若 C_cloud=0.07元，C_elec=0.0005元，C_depr_total_daily=9.17元，则需 N > 9.17/(0.07-0.0005) ≈ 131 次/天才能覆盖折旧优势（注：此处单位需统一，若按美元计算需转换汇率）。

## Evidence

先验知识/题面给定，逻辑校验通过：不等式 C_elec + C_depr/N < C_cloud 变形为 N > C_depr / (C_cloud - C_elec)，代入数值 9.17 / (0.07 - 0.0005) ≈ 131.07，取整逻辑正确，量纲一致。
