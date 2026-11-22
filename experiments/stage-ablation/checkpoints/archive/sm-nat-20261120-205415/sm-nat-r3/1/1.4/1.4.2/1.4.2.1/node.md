# N111: 工作点1（高覆盖/低效率）：假设缓存装满最小对象（S_min=0.09MB），K_max = 128GB/0.09MB ≈ 1,437,000 > N=100,

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

工作点1（高覆盖/低效率）：假设缓存装满最小对象（S_min=0.09MB），K_max = 128GB/0.09MB ≈ 1,437,000 > N=100,000，此时 Cov_byte 达到理论上限 100%，但此假设违背热度-大小负相关，实际不可达。

## Corrected Claim

工作点1（高覆盖/低效率）：假设缓存装满最小对象（S_min=0.09MB），K_max = 128GB/0.09MB ≈ 1,437,000 > N=100,000，此时 Cov_byte 达到理论上限 100%，但此假设违背热度-大小负相关，实际不可达。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB/0.09MB ≈ 1,437,000 计算正确，且基于热度-大小负相关原理指出该极端假设不可达，逻辑自洽。
