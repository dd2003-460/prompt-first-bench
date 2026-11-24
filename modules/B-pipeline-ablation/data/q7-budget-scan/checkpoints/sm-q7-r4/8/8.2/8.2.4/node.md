# N268: 温数据盘活跃率 T_active_warm 修正：对于 20% 温数据，每日扫描 1-2 次，假设每次扫描覆盖全盘耗时 4h，则年活跃时间占比 = (365天 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128

## Claim

温数据盘活跃率 T_active_warm 修正：对于 20% 温数据，每日扫描 1-2 次，假设每次扫描覆盖全盘耗时 4h，则年活跃时间占比 = (365天 * 1.5次/天 * 4h) / 8760h ≈ 25%，N128 假设的 10% 严重低估了温数据盘的活跃率

## Corrected Claim

温数据盘活跃率 T_active_warm 修正：对于 20% 温数据，每日扫描 1-2 次，假设每次扫描覆盖全盘耗时 4h，则年活跃时间占比 = (365天 * 1.5次/天 * 4h) / 8760h ≈ 25%，N128 假设的 10% 严重低估了温数据盘的活跃率

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应低、中、高三种活跃场景，覆盖了参数变化的范围，逻辑上互斥且无矛盾（正交）。虽然本质上是同一公式在不同参数下的取值，但在系统分析中作为边界条件（Work Points）保留是合理的，不属于无意义的冗余。）

## Search Query

warm data daily scan duration storage access pattern calculation
