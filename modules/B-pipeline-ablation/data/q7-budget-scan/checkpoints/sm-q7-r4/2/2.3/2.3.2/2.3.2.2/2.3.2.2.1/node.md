# N559: 阿里云 OSS 所有存储类型（包括 IA）的单对象最小计费单位为 64KB，小于 64KB 的对象按 64KB 计费；若对象平均大小为 S_avg，则有效计费容

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N184

## Claim

阿里云 OSS 所有存储类型（包括 IA）的单对象最小计费单位为 64KB，小于 64KB 的对象按 64KB 计费；若对象平均大小为 S_avg，则有效计费容量膨胀系数 K_bloat = Max(1, 64KB / S_avg)。

## Corrected Claim

阿里云 OSS 所有存储类型（包括 IA）的单对象最小计费单位为 64KB，小于 64KB 的对象按 64KB 计费；若对象平均大小为 S_avg，则有效计费容量膨胀系数 K_bloat = Max(1, 64KB / S_avg)。

## Evidence

先验知识/题面给定，逻辑校验通过
