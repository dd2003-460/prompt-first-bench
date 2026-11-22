# N236: LRU 命中率下界对 x_max 的敏感性公式：H_LRU(x_max) = 1 - (Σ_{i: S_i > C/N_cache} p_i s_i) / (Σ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

LRU 命中率下界对 x_max 的敏感性公式：H_LRU(x_max) = 1 - (Σ_{i: S_i > C/N_cache} p_i s_i) / (Σ_all p_i s_i)，其中 C=128GB，N_cache=100,000，当 x_max 从 1GB 增至 10GB 时，缓存边界 S_boundary = 128GB/100,000 = 1.31KB 保持不变，因此命中率下界主要受对象大小分布变化影响而非截断点直接作用

## Corrected Claim

LRU 命中率下界对 x_max 的敏感性公式：H_LRU(x_max) = 1 - (Σ_{i: S_i > C/N_cache} p_i s_i) / (Σ_all p_i s_i)，其中 C=128GB，N_cache=100,000，当 x_max 从 1GB 增至 10GB 时，缓存边界 S_boundary = 128GB/100,000 = 1.31KB 保持不变，因此命中率下界主要受对象大小分布变化影响而非截断点直接作用

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 缓存边界由总容量与对象数决定，与最大对象大小 x_max 无关，故边界不变，命中率变化主要源于分布变化。
