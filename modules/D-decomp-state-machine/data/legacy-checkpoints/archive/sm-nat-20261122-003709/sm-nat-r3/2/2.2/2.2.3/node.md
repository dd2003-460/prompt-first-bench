# N46: 量化 LFU 与 LRU 在 ρ=-0.3 条件下的命中率差值 ΔH_ρ = H_LFU - H_LRU，需通过对比两种策略在‘热小冷大’分布下的驱逐错误率（E

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N11

## Claim

量化 LFU 与 LRU 在 ρ=-0.3 条件下的命中率差值 ΔH_ρ = H_LFU - H_LRU，需通过对比两种策略在‘热小冷大’分布下的驱逐错误率（Eviction Error Rate）差异得出，该差值直接受 S_hot_avg/S_cold_avg 比值调制。

## Corrected Claim

量化 LFU 与 LRU 在特定访问分布（如 ρ=-0.3 的‘热小冷大’分布）下的命中率差值 ΔH_ρ，通常需通过对比两种策略的驱逐错误率差异得出，该差值受冷热数据大小比值（S_hot_avg/S_cold_avg）的影响。

## Evidence

[质询]该陈述包含具体的经验性参数（ρ=-0.3）和特定的机制归因（直接受 S_hot_avg/S_cold_avg 比值调制），属于经验事实而非第一性原理可推导的数学/逻辑恒等式。在缺乏外部来源支持的情况下，无法验证该特定参数下的具体差值及调制机制的准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

LFU vs LRU cache hit rate difference power law distribution correlation size popularity
