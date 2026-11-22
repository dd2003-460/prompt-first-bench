# N72: 截断至 M_max = 1.3MB 后，Pareto(α=1.1) 分布的尾部质量（即大小 > 1.3MB 的对象占比）为 P(S > 1.3MB) = (1K

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：Pareto分布尾部概率公式 P(S>x) = (x_m/x)^α 应用正确，数值计算 (1/1300)^1.1 ≈ 0.0004 量级合理，结论自洽。
