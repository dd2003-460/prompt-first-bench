# N73: 若 S_min = 100KB（而非 1KB），则 E[S] = 100KB * 1.1 / 0.1 = 1.1MB，截断至 1.3MB 后尾部质量 P(S >

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

若 S_min = 100KB（而非 1KB），则 E[S] = 100KB * 1.1 / 0.1 = 1.1MB，截断至 1.3MB 后尾部质量 P(S > 1.3MB) = (100KB/1.3MB)^1.1 ≈ (1/13)^1.1 ≈ 0.07，即 7% 的对象被截断，均值偏差显著增大，需重新计算 E[S_trunc] 以修正命中率分母。

## Corrected Claim

若 S_min = 100KB（而非 1KB），则 E[S] = 100KB * 1.1 / 0.1 = 1.1MB，截断至 1.3MB 后尾部质量 P(S > 1.3MB) = (100KB/1.3MB)^1.1 ≈ (1/13)^1.1 ≈ 0.07，即 7% 的对象被截断，均值偏差显著增大，需重新计算 E[S_trunc] 以修正命中率分母。

## Evidence

先验知识/题面给定，逻辑校验通过：基于帕累托分布（或幂律分布）的尾部概率公式 P(S > x) = (S_min/x)^α 计算，(100/1300)^1.1 ≈ (1/13)^1.1 ≈ 0.07 数值量级正确，逻辑自洽。
