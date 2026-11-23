# N172: 偏远地区缓存命中率 H_remote 的降低原因：由于偏远地区用户基数小，本地缓存容量 C 可能较小或共享比例低，且热点分散（Zipf alpha 可能更低，如

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

偏远地区缓存命中率 H_remote 的降低原因：由于偏远地区用户基数小，本地缓存容量 C 可能较小或共享比例低，且热点分散（Zipf alpha 可能更低，如 0.8），导致 H_remote < H_city。假设 H_remote = 0.80 (N53)，需验证是否由容量限制或访问模式分散导致。若 C_remote = C_city * (20%/80%) = 20TB，则 H_remote 会显著低于 H_city。

## Corrected Claim

偏远地区缓存命中率 H_remote 的降低原因：由于偏远地区用户基数小，本地缓存容量 C 可能较小或共享比例低，且热点分散（Zipf alpha 可能更低，如 0.8），导致 H_remote < H_city。假设 H_remote = 0.80 (N53)，需验证是否由容量限制或访问模式分散导致。若 C_remote = C_city * (20%/80%) = 20TB，则 H_remote 会显著低于 H_city。

## Evidence

先验知识/题面给定，逻辑校验通过：偏远地区用户基数小导致缓存容量受限及热点分散（Zipf alpha降低），符合缓存命中率与容量、访问模式分布正相关的物理/经济直觉，数值量级合理。

## Search Query

cache hit rate rural users low population density
