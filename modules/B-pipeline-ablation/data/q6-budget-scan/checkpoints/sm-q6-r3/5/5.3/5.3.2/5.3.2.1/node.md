# N247: 预热期间回源概率 p_miss_warm 的构成：p_miss_warm = p_miss_base * (1 - H_warm_instant)，其中 H_w

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

预热期间回源概率 p_miss_warm 的构成：p_miss_warm = p_miss_base * (1 - H_warm_instant)，其中 H_warm_instant 为预热对象在预热期间的瞬时命中率，对于 Top-K 预热，H_warm_instant ≈ F(K) * (1 - e^(-B_warm * T_warm / (K * s_avg)))，当 B_warm * T_warm >> K * s_avg 时 H_warm_instant → F(K)

## Corrected Claim

预热期间回源概率 p_miss_warm 的构成：p_miss_warm = p_miss_base * (1 - H_warm_instant)，其中 H_warm_instant 为预热对象在预热期间的瞬时命中率，对于 Top-K 预热，H_warm_instant ≈ F(K) * (1 - e^(-B_warm * T_warm / (K * s_avg)))，当 B_warm * T_warm >> K * s_avg 时 H_warm_instant → F(K)

## Evidence

先验知识/题面给定，逻辑校验通过
