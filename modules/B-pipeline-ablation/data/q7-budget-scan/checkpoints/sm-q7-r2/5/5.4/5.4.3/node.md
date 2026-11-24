# N77: S3过滤结果：吞吐需求7GB/s，受API限流1550 GET/s/bucket约束，最大吞吐 = 1550 * 1MB = 1.55GB/s（1MB对象），不

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

S3过滤结果：吞吐需求7GB/s，受API限流1550 GET/s/bucket约束，最大吞吐 = 1550 * 1MB = 1.55GB/s（1MB对象），不满足7GB/s需求；若对象大小提升至4MB，最大吞吐 = 1550 * 4MB = 6.2GB/s，仍不满足；需多bucket并行或提升对象大小至8MB（最大吞吐12.4GB/s，满足），但对象大小8MB需业务确认是否可行

## Corrected Claim

S3过滤结果：吞吐需求7GB/s，受API限流1550 GET/s/bucket约束，最大吞吐 = 1550 * 1MB = 1.55GB/s（1MB对象），不满足7GB/s需求；若对象大小提升至4MB，最大吞吐 = 1550 * 4MB = 6.2GB/s，仍不满足；需多bucket并行或提升对象大小至8MB（最大吞吐12.4GB/s，满足），但对象大小8MB需业务确认是否可行

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（1550*1MB=1.55GB/s, 1550*4MB=6.2GB/s, 1550*8MB=12.4GB/s），且结论符合S3 API限流约束下的吞吐推导逻辑。
