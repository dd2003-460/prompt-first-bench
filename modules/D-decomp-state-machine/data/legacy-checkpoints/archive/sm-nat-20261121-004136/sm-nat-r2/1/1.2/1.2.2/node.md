# N30: 前 k 个最热门对象占总请求量的比例 H_prefix(k) = 1 - (k/N)^(1-β)，当 k=1 时，最热对象占比为 1 - (1/N)^(0.1)

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

前 k 个最热门对象占总请求量的比例 H_prefix(k) = 1 - (k/N)^(1-β)，当 k=1 时，最热对象占比为 1 - (1/N)^(0.1) ≈ 0.55，表明头部效应极强。

## Corrected Claim

前 k 个最热门对象占总请求量的比例 H_prefix(k) = 1 - (k/N)^(1-β)，当 k=1 时，最热对象占比为 1 - (1/N)^(0.1) ≈ 0.55，表明头部效应极强。
