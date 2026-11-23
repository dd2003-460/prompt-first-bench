# N54: 回源路径中源站处理延迟的P99值 T_origin_processing_P99 取决于后端数据库查询复杂度与缓存命中率，对于图片/短视频平台，若源站有本地缓存

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

回源路径中源站处理延迟的P99值 T_origin_processing_P99 取决于后端数据库查询复杂度与缓存命中率，对于图片/短视频平台，若源站有本地缓存，P99通常为5-20ms；若无缓存直接查库，P99可达50-200ms。

## Corrected Claim

回源路径中源站处理延迟的P99值 T_origin_processing_P99 取决于后端数据库查询复杂度与缓存命中率，对于图片/短视频平台，若源站有本地缓存，P99通常为5-20ms；若无缓存直接查库，P99可达50-200ms。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别从底层数据库查询、应用层缓存机制、以及系统架构层面的异步削峰三个不同维度进行分解，覆盖了源站处理延迟的主要构成部分，且各部分逻辑独立，无重复或矛盾。）
