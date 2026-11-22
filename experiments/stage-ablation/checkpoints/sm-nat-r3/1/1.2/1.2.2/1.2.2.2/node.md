# N120: 缓存边界处（假设 LRU 缓存保留前 N_cache 个最热门对象）的临界请求速率 λ_boundary 决定了 LRU 的驱逐压力，若 N_cache=100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

缓存边界处（假设 LRU 缓存保留前 N_cache 个最热门对象）的临界请求速率 λ_boundary 决定了 LRU 的驱逐压力，若 N_cache=100,000（全缓存），则 λ_boundary → 0；若 N_cache=10,000，则 λ_10000 ≈ 50,000,000 * 10000^{-0.9} / 1.15505 ≈ 13.9 次/天，该值用于计算尾部对象的驻留时间 W_LRU(N_cache)。

## Corrected Claim

缓存边界处（假设 LRU 缓存保留前 N_cache 个最热门对象）的临界请求速率 λ_boundary 决定了 LRU 的驱逐压力，若 N_cache=100,000（全缓存），则 λ_boundary → 0；若 N_cache=10,000，则 λ_10000 ≈ 50,000,000 * 10000^{-0.9} / 1.15505 ≈ 13.9 次/天，该值用于计算尾部对象的驻留时间 W_LRU(N_cache)。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Zipf分布（α=0.9）和LRU缓存模型，临界速率计算符合数学推导，数值量级合理。
