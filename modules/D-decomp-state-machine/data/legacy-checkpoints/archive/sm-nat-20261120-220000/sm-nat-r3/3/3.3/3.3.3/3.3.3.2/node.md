# N121: Miss 成本在 S_min=1KB 和 S_max=10MB 处的边界值：cost_miss(1KB) = 6ms + 1KB/100MB/s ≈ 6.01m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

Miss 成本在 S_min=1KB 和 S_max=10MB 处的边界值：cost_miss(1KB) = 6ms + 1KB/100MB/s ≈ 6.01ms，cost_miss(10MB) = 6ms + 10MB/100MB/s = 6ms + 0.1s = 106ms，表明大对象的 miss 成本主要由重填充传输时间主导，固定处理开销可忽略。

## Corrected Claim

Miss 成本在 S_min=1KB 和 S_max=10MB 处的边界值：cost_miss(1KB) = 6ms + 1KB/100MB/s ≈ 6.01ms，cost_miss(10MB) = 6ms + 10MB/100MB/s = 6ms + 0.1s = 106ms，表明大对象的 miss 成本主要由重填充传输时间主导，固定处理开销可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（1KB/100MB/s≈0.01ms，10MB/100MB/s=100ms），量纲一致，结论符合物理直觉（大对象传输时间主导）。
