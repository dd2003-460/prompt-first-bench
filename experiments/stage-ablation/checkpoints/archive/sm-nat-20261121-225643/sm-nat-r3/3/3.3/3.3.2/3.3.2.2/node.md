# N96: 新鲜度失效阈值 u_threshold = 1/T_resident ≈ 6400/天；当前 u=0.01/天 远小于阈值（u/u_threshold ≈ 1.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

新鲜度失效阈值 u_threshold = 1/T_resident ≈ 6400/天；当前 u=0.01/天 远小于阈值（u/u_threshold ≈ 1.56e-6），确认系统处于'容量驱逐主导'区域，新鲜度失效对命中率的直接贡献 < 0.0001%

## Corrected Claim

新鲜度失效阈值 u_threshold = 1/T_resident ≈ 6400/天；当前 u=0.01/天 远小于阈值（u/u_threshold ≈ 1.56e-6），确认系统处于'容量驱逐主导'区域，新鲜度失效对命中率的直接贡献 < 0.0001%

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（0.01/6400 ≈ 1.56e-6），量级合理，符合缓存系统中新鲜度失效与容量驱逐主导区域的定义逻辑。
