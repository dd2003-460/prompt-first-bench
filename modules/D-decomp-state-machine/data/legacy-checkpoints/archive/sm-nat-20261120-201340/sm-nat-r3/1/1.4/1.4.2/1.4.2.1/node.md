# N96: 保守估计工作点 (s_min=1KB, s_max=1GB)：代入公式 E[S] = 1.1*1KB/(0.1) * (1 - 10^-9)^{0.1} / (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

保守估计工作点 (s_min=1KB, s_max=1GB)：代入公式 E[S] = 1.1*1KB/(0.1) * (1 - 10^-9)^{0.1} / (1 - 10^-9) ≈ 11KB，此值对应 CDN 中纯元数据或小文件的极端场景，导致 W_total ≈ 1.1GB，缓存覆盖率 >100x，命中率理论上限为 100%。

## Corrected Claim

保守估计工作点 (s_min=1KB, s_max=1GB)：代入公式 E[S] = 1.1*1KB/(0.1) * (1 - 10^-9)^{0.1} / (1 - 10^-9) ≈ 11KB，此值对应 CDN 中纯元数据或小文件的极端场景，导致 W_total ≈ 1.1GB，缓存覆盖率 >100x，命中率理论上限为 100%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式代入计算正确（1.1*1024/0.1 * 1 ≈ 11264 Bytes ≈ 11KB），量级与结论自洽。
