# N143: 工作点 3 的 H_static ≈ 70% 需修正：在大对象主导场景（S > 1MB），由于缓存容量 C=128GB 远小于总字节量，H_static 实际等

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

工作点 3 的 H_static ≈ 70% 需修正：在大对象主导场景（S > 1MB），由于缓存容量 C=128GB 远小于总字节量，H_static 实际等于缓存可容纳的头部大对象字节占比，即 H_static_large = Σ_{i∈Top_k} S_i / Σ_{j∈All} S_j，其中 k 由 C 决定，需通过 Pareto(α=1.1) 的累积字节分布 B(x) = 1 - (s_min/x)^0.1 反解 k。

## Corrected Claim

在大对象主导场景下，若假设缓存仅存储头部大对象且忽略小对象干扰，H_static 可近似为缓存容量 C 内头部大对象的字节占比，具体数值需根据实际缓存策略和对象分布参数（如 Pareto 指数）计算，而非固定为 70%。

## Evidence

[质询]该陈述包含具体的经验参数（如缓存容量 C=128GB、Pareto 指数 α=1.1、对象大小阈值 S>1MB），这些属于硬件/系统配置的经验事实，无法仅从第一性原理推导。此外，'H_static 实际等于缓存可容纳的头部大对象字节占比'这一简化模型忽略了缓存替换策略（如 LRU/LFU）对非头部对象的影响，以及小对象对缓存空间的占用，逻辑上过于理想化。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且涉及具体系统参数与简化模型假设，无法仅凭逻辑验证其数值准确性）

## Search Query

Pareto cumulative byte distribution head object cache hit rate
