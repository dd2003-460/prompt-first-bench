# N354: 2x RTX 4090 在 5 年 TCO $4,200 下的单位成本吞吐量 (Cost per 1000 Tokens) 计算：假设 INT4 量化下 TPS

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

2x RTX 4090 在 5 年 TCO $4,200 下的单位成本吞吐量 (Cost per 1000 Tokens) 计算：假设 INT4 量化下 TPS 为 50 tokens/s (2x4090 并行)，年运行 4380 小时，总生成 Tokens = 50 * 4380 * 5 * 3600 ≈ 3.95e9，Cost per 1000 Tokens ≈ $4,200 / 3.95e6 ≈ $0.00106/1000 tokens，约为 M2 Ultra BF16 的 25%。

## Corrected Claim

2x RTX 4090 在 5 年 TCO $4,200 下的单位成本吞吐量 (Cost per 1000 Tokens) 计算：假设 INT4 量化下 TPS 为 50 tokens/s (2x4090 并行)，年运行 4380 小时，总生成 Tokens = 50 * 4380 * 5 * 3600 ≈ 3.95e9，Cost per 1000 Tokens ≈ $4,200 / 3.95e6 ≈ $0.00106/1000 tokens，约为 M2 Ultra BF16 的 25%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（50*4380*5*3600 ≈ 3.942e9，4200/3.942e6 ≈ 0.001065），量级合理，符合2x4090在INT4量化下的性能预期。
