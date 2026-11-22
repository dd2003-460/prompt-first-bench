# N72: 截断至 M_max = 1.3MB 后，Pareto(α=1.1) 分布的尾部质量（即大小 > 1.3MB 的对象占比）为 P(S > 1.3MB) = (1K

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

截断至 M_max = 1.3MB 后，Pareto(α=1.1) 分布的尾部质量（即大小 > 1.3MB 的对象占比）为 P(S > 1.3MB) = (1KB/1.3MB)^1.1 ≈ (1/1300)^1.1 ≈ 0.0004，即仅 0.04% 的对象被截断，对总存储和命中率的量化影响可忽略。

## Corrected Claim

截断至 M_max = 1.3MB 后，Pareto(α=1.1) 分布的尾部质量（即大小 > 1.3MB 的对象占比）为 P(S > 1.3MB) = (1KB/1.3MB)^1.1 ≈ (1/1300)^1.1 ≈ 0.0004，即仅 0.04% 的对象被截断，对总存储和命中率的量化影响可忽略。

## Evidence

父节点级核验失败（LLM 错误）：Expecting ',' delimiter: line 9 column 162 (char 831)
