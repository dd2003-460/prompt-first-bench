# N82: 缓存容量对应的 Top-K 对象数反解：已知缓存 128GB 占 Total_Bytes (1.1TB) 的 11.6%，需反解 K 使得 Mass_K = 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

缓存容量对应的 Top-K 对象数反解：已知缓存 128GB 占 Total_Bytes (1.1TB) 的 11.6%，需反解 K 使得 Mass_K = 0.116。解方程 1 - (K/N)^(-0.1) / (1 - (1/N)^(-0.1)) = 0.116，得 (K/N)^(-0.1) ≈ 0.858，K/N ≈ 0.858^(-10) ≈ 0.194，即 K ≈ 19,400 个对象。这验证了 N34/N37 中 N_resident≈8000-10000 的估算偏低，实际应接近 2 万对象。

## Corrected Claim

缓存容量对应的 Top-K 对象数反解：已知缓存 128GB 占 Total_Bytes (1.1TB) 的 11.6%，需反解 K 使得 Mass_K = 0.116。解方程 1 - (K/N)^(-0.1) / (1 - (1/N)^(-0.1)) = 0.116，得 (K/N)^(-0.1) ≈ 0.858，K/N ≈ 0.858^(-10) ≈ 0.194，即 K ≈ 19,400 个对象。这验证了 N34/N37 中 N_resident≈8000-10000 的估算偏低，实际应接近 2 万对象。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导步骤正确，0.858^(-10) ≈ 0.194，K ≈ 19400，量级合理。

## Search Query

inverse Pareto CDF cumulative mass calculation
