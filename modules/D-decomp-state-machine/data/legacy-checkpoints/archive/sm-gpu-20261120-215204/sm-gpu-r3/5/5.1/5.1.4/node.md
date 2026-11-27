# N121: A100 80GB 在 FP8 精度下的 TTFT 估算：基于 N42 的计算，理论计算时间 14ms，加上内存加载和同步开销，实际 TTFT 预期 <100m

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

A100 80GB 在 FP8 精度下的 TTFT 估算：基于 N42 的计算，理论计算时间 14ms，加上内存加载和同步开销，实际 TTFT 预期 <100ms，远小于 5s 的阈值。

## Corrected Claim

A100 80GB 在 FP8 精度下的 TTFT 估算：基于 N42 的计算，理论计算时间 14ms，加上内存加载和同步开销，实际 TTFT 预期 <100ms，远小于 5s 的阈值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于理论计算耗时（Prefill FLOPs计算），子节点2聚焦于实际工程开销（内存加载、JIT编译等），两者维度不同（理论 vs 实际/工程），无重复且无矛盾，共同支撑父节点的结论。）
