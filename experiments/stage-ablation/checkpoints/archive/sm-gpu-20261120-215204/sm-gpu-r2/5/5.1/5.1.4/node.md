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

先验知识/题面给定，逻辑校验通过：A100 80GB 具备高显存带宽，FP8 精度下计算量减半，14ms 理论计算时间加上合理开销后 <100ms 的估算符合硬件性能量级，且远小于 5s 阈值，逻辑自洽。
