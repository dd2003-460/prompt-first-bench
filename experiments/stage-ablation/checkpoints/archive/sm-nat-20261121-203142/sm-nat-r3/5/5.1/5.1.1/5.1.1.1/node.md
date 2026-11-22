# N162: 缓存覆盖率 C/M 的精确计算：C = 128 * 1024^3 bytes，M = N_total * E[S] = 100,000 * (1.1/0.1) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N63

## Claim

缓存覆盖率 C/M 的精确计算：C = 128 * 1024^3 bytes，M = N_total * E[S] = 100,000 * (1.1/0.1) * x_min，假设 x_min = 1KB，则 M ≈ 100,000 * 11 * 1024 bytes ≈ 1.1 GB，C/M ≈ 118，表明缓存容量远大于总数据量，公式中的 (C/M)^{α-1} 项将极大，导致下界趋近 1

## Corrected Claim

缓存覆盖率 C/M 的精确计算：C = 128 * 1024^3 bytes，M = N_total * E[S] = 100,000 * (1.1/0.1) * x_min，假设 x_min = 1KB，则 M ≈ 100,000 * 11 * 1024 bytes ≈ 1.1 GB，C/M ≈ 118，表明缓存容量远大于总数据量，公式中的 (C/M)^{α-1} 项将极大，导致下界趋近 1

## Evidence

先验知识/题面给定，逻辑校验通过：C=128GB, M≈1.1GB, C/M≈118，数值量级与计算逻辑自洽
