# N113: 缓存内对象平均大小 S_avg_cached 的积分计算：S_avg_cached = (1/K) * ∫_{1}^{K} 116.36 * x^{-0.1} 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N43

## Claim

缓存内对象平均大小 S_avg_cached 的积分计算：S_avg_cached = (1/K) * ∫_{1}^{K} 116.36 * x^{-0.1} dx = (116.36 / K) * [x^{0.9}/0.9]_{1}^{K} ≈ 116.36 * K^{-0.1} / 0.9；代入 K=32000，K^{-0.1} ≈ 0.35，得 S_avg_cached ≈ 116.36 * 0.35 / 0.9 ≈ 45.1 bytes [verified: 基于 N47 的 S_k 公式和 N57 的 K 值]

## Corrected Claim

缓存内对象平均大小 S_avg_cached 的积分计算：S_avg_cached = (1/K) * ∫_{1}^{K} 116.36 * x^{-0.1} dx = (116.36 / K) * [x^{0.9}/0.9]_{1}^{K} ≈ 116.36 * K^{-0.1} / 0.9；代入 K=32000，K^{-0.1} ≈ 0.35，得 S_avg_cached ≈ 116.36 * 0.35 / 0.9 ≈ 45.1 bytes [verified: 基于 N47 的 S_k 公式和 N57 的 K 值]

## Evidence

先验知识/题面给定，逻辑校验通过：积分计算正确，数值量级合理（116.36 * 0.35 / 0.9 ≈ 45.1）
