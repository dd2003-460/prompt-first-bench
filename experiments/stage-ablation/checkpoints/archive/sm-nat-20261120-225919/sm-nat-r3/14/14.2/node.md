# N286: 在 Pareto(β=0.9) 分布下，LFU 相比 LRU 的增益主要来源于对'突发热点'（bursty hot spots）的捕获；量化上，增益 ΔH ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

在 Pareto(β=0.9) 分布下，LFU 相比 LRU 的增益主要来源于对'突发热点'（bursty hot spots）的捕获；量化上，增益 ΔH ≈ P(Burst) * (H_LFU|Burst - H_LRU|Burst)，其中 P(Burst) 为突发请求占比。若假设突发占比为 5% 且突发期间 LFU 命中率比 LRU 高 20 个百分点，则 ΔH ≈ 0.05 * 0.20 = 1%。

## Corrected Claim

在 Pareto(β=0.9) 分布下，LFU 相比 LRU 的增益主要来源于对'突发热点'（bursty hot spots）的捕获；量化上，增益 ΔH ≈ P(Burst) * (H_LFU|Burst - H_LRU|Burst)，其中 P(Burst) 为突发请求占比。若假设突发占比为 5% 且突发期间 LFU 命中率比 LRU 高 20 个百分点，则 ΔH ≈ 0.05 * 0.20 = 1%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 ΔH = P(Burst) * ΔH_Burst 符合全概率公式的分解逻辑，数值计算 0.05 * 0.20 = 0.01 (1%) 准确无误，且符合 LFU 在突发热点场景下优于 LRU 的缓存理论直觉。

## Search Query

LFU vs LRU bursty workload hit rate improvement percentage Pareto distribution
