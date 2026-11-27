# N141: INT8权重大小计算：Size_INT8 = 27e9 * 1 byte = 27GB（注意：INT8通常为per-channel或per-token量化，需额

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

INT8权重大小计算：Size_INT8 = 27e9 * 1 byte = 27GB（注意：INT8通常为per-channel或per-token量化，需额外存储scale和zero_point，额外占用约1-5%）

## Corrected Claim

INT8权重大小计算：Size_INT8 = 27e9 * 1 byte = 27GB（注意：INT8通常为per-channel或per-token量化，需额外存储scale和zero_point，额外占用约1-5%）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1侧重于对比Per-Channel与Per-Token两种策略的理论差异及元数据占比估算，子节点2侧重于针对Qwen3-27B具体架构进行Per-Channel策略下的精确计算与验证。两者视角不同（策略对比 vs 具体实例验证），内容互补且不重复，共同覆盖了父节点中关于‘额外存储scale/zero_point’及‘1-5%占比’的核心关注点。）
