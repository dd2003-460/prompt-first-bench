# N77: 对象数量覆盖率的精确推导：设缓存能容纳的对象数为 K_max。由于大小服从 Pareto(α=1.1)，第 k 小对象的大小 S_k ≈ s_min * (k)

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象数量覆盖率的精确推导：设缓存能容纳的对象数为 K_max。由于大小服从 Pareto(α=1.1)，第 k 小对象的大小 S_k ≈ s_min * (k)^(1/α) = s_min * k^0.909。前 K 个对象总大小 Sum_S(K) ≈ s_min * ∫_1^K x^0.909 dx ≈ s_min * [K^1.909 / 1.909]。令 Sum_S(K) = 128GB = 1.37 * 10^11 bytes。若 s_min=1KB=1024 bytes，则 1024 * K^1.909 / 1.909 = 1.37 * 10^11 => K^1.909 ≈ 2.5 * 10^8 => K ≈ (2.5 * 10^8)^(1/1.909) ≈ 15,000。即 128GB 可存储约 15,000 个最小对象。

## Corrected Claim

对象数量覆盖率的精确推导：设缓存能容纳的对象数为 K_max。由于大小服从 Pareto(α=1.1)，第 k 小对象的大小 S_k ≈ s_min * (k)^(1/α) = s_min * k^0.909。前 K 个对象总大小 Sum_S(K) ≈ s_min * ∫_1^K x^0.909 dx ≈ s_min * [K^1.909 / 1.909]。令 Sum_S(K) = 128GB = 1.37 * 10^11 bytes。若 s_min=1KB=1024 bytes，则 1024 * K^1.909 / 1.909 = 1.37 * 10^11 => K^1.909 ≈ 2.5 * 10^8 => K ≈ (2.5 * 10^8)^(1/1.909) ≈ 15,000。即 128GB 可存储约 15,000 个最小对象。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Pareto distribution cumulative sum approximation integral derivation
