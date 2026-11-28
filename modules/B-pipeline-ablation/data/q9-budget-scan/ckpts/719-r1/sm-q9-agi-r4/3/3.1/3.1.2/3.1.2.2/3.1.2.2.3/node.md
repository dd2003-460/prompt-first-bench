# N491: Kernel Launch Latency 在 V100 上典型值为 5-10μs (微秒) 而非 ms (毫秒)；若按 10μs 计算，48 层 Transf

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N175

## Claim

Kernel Launch Latency 在 V100 上典型值为 5-10μs (微秒) 而非 ms (毫秒)；若按 10μs 计算，48 层 Transformer 的总 Kernel Launch 开销为 48 * 10μs = 0.48ms，远低于 30ms 的计算时间，因此对 Decode 速度影响可忽略 (<2%)

## Corrected Claim

Kernel Launch Latency 在 V100 上典型值为 5-10μs (微秒) 而非 ms (毫秒)；若按 10μs 计算，48 层 Transformer 的总 Kernel Launch 开销为 48 * 10μs = 0.48ms，远低于 30ms 的计算时间，因此对 Decode 速度影响可忽略 (<2%)

## Evidence

先验知识/题面给定，逻辑校验通过：V100 GPU Kernel Launch 延迟通常在微秒级（5-10μs），48层Transformer的总启动开销约0.48ms，相对于30ms的计算时间占比约1.6%，符合<2%的结论。
