# N764: M2 Ultra 在 LLM Decode 场景下，内存控制器因非对齐访问（Non-aligned Access，如 16-byte vs 256-byte）导

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N236, N237, N238

## Claim

M2 Ultra 在 LLM Decode 场景下，内存控制器因非对齐访问（Non-aligned Access，如 16-byte vs 256-byte）导致的单次事务开销，使有效带宽从 800 GB/s 降至 440-520 GB/s (55-65%)，具体损耗系数取决于量化块大小（Block Size 64 vs 128）与内存对齐边界

## Corrected Claim

M2 Ultra 在 LLM Decode 场景下，受内存对齐及访问模式影响，有效带宽可能显著低于峰值 800 GB/s，具体损耗取决于量化块大小与对齐边界，但具体数值需实测验证。

## Evidence

[质询]该陈述包含具体的经验性数值（440-520 GB/s，55-65%损耗），属于硬件性能实测数据，无法从第一性原理推导。且‘非对齐访问导致带宽减半’这一因果机制在通用内存控制器理论中并非绝对定论，通常取决于具体的内存子系统实现和访问模式，存在将特定优化场景下的瓶颈泛化为通用物理限制的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值及因果机制的普适性）

## Search Query

Apple M2 Ultra memory controller non-aligned access penalty LLM decode bandwidth efficiency mlx benchmark
