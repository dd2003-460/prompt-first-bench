# N153: 工作点1（短驻留/高失效）：假设对象平均驻留时间 T_resident = 10 天（高频更新场景），M_invalidation = 1 - exp(-0.0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N50

## Claim

工作点1（短驻留/高失效）：假设对象平均驻留时间 T_resident = 10 天（高频更新场景），M_invalidation = 1 - exp(-0.01 * 10) ≈ 0.00995（约1.0%），适用于小对象或高竞争场景，命中率折扣极小。

## Corrected Claim

工作点1（短驻留/高失效）：假设对象平均驻留时间 T_resident = 10 天（高频更新场景），M_invalidation = 1 - exp(-0.01 * 10) ≈ 0.00995（约1.0%），适用于小对象或高竞争场景，命中率折扣极小。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

cache invalidation probability formula exponential decay
