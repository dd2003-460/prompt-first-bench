# N75: 缓存容量覆盖率理论上限：在 Pareto(α=1.1) 分布下，前 K 个最小对象覆盖的字节比例 Mass_bytes(K) ≈ (K/N)^(1-1/α) =

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

缓存容量覆盖率理论上限：在 Pareto(α=1.1) 分布下，前 K 个最小对象覆盖的字节比例 Mass_bytes(K) ≈ (K/N)^(1-1/α) = (K/N)^0.0909。若总数据量由截断均值决定（如 N66 所述，Total_Bytes ≈ 5.2 * 10^14 bytes），128GB 仅覆盖总字节的 ~0.025%。但在热度加权下，缓存应覆盖 Top-K 最热对象。由于大小与热度负相关，Top-K 最热对象的大小之和 Sum_S_Hot(K) 远小于 K * E[S]。理论上限是找到最大 K 使得 Sum_{i=1}^K S_i <= 128GB。鉴于 S_i 服从 Pareto 且与热度负相关，K 可能高达 10,000-50,000 个对象，覆盖请求量的 90%-99%。

## Corrected Claim

缓存容量覆盖率理论上限：在 Pareto(α=1.1) 分布下，前 K 个最小对象覆盖的字节比例 Mass_bytes(K) ≈ (K/N)^(1-1/α) = (K/N)^0.0909。若总数据量由截断均值决定（如 N66 所述，Total_Bytes ≈ 5.2 * 10^14 bytes），128GB 仅覆盖总字节的 ~0.025%。但在热度加权下，缓存应覆盖 Top-K 最热对象。由于大小与热度负相关，Top-K 最热对象的大小之和 Sum_S_Hot(K) 远小于 K * E[S]。理论上限是找到最大 K 使得 Sum_{i=1}^K S_i <= 128GB。鉴于 S_i 服从 Pareto 且与热度负相关，K 可能高达 10,000-50,000 个对象，覆盖请求量的 90%-99%。

## Evidence

检索失败: no sources from any channel (all 5 failed)
