# N268: 温数据盘活跃率 T_active_warm 修正：对于 20% 温数据，每日扫描 1-2 次，假设每次扫描覆盖全盘耗时 4h，则年活跃时间占比 = (365天 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N128

## Claim

温数据盘活跃率 T_active_warm 修正：对于 20% 温数据，每日扫描 1-2 次，假设每次扫描覆盖全盘耗时 4h，则年活跃时间占比 = (365天 * 1.5次/天 * 4h) / 8760h ≈ 25%，N128 假设的 10% 严重低估了温数据盘的活跃率

## Corrected Claim

温数据盘活跃率 T_active_warm 修正：对于 20% 温数据，每日扫描 1-2 次，假设每次扫描覆盖全盘耗时 4h，则年活跃时间占比 = (365天 * 1.5次/天 * 4h) / 8760h ≈ 25%，N128 假设的 10% 严重低估了温数据盘的活跃率

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (365 * 1.5 * 4) / 8760 = 2190 / 8760 ≈ 0.25 准确无误，且 25% 显著高于 10%，结论成立。

## Search Query

warm data daily scan duration storage access pattern calculation
