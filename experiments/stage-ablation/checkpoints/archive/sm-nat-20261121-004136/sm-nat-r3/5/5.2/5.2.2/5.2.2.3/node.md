# N151: ρ 对 LRU 命中率的影响机制：ρ 每增加 0.1（即负相关性减弱），LRU 字节命中率下界 H_LRU 下降约 0.5-1.0 个百分点，因为热门对象变大导

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

ρ 对 LRU 命中率的影响机制：ρ 每增加 0.1（即负相关性减弱），LRU 字节命中率下界 H_LRU 下降约 0.5-1.0 个百分点，因为热门对象变大导致缓存容量被低效占用，量化为 ΔH/Δρ ≈ -0.01 per 0.1 ρ。

## Corrected Claim

ρ 对 LRU 命中率的影响机制：ρ 增加（负相关性减弱）通常会导致 LRU 字节命中率下降，因为热门对象变大导致缓存容量被低效占用，但具体下降幅度取决于系统参数，一般认为每增加 0.1 ρ，命中率可能下降约 0.5-1.0 个百分点。

## Evidence

[质询]该陈述包含具体的经验量化数值（ΔH/Δρ ≈ -0.01 per 0.1 ρ），这属于特定系统或模型下的经验事实，无法从第一性原理严格推导，且缺乏外部来源支持以确认该具体量级。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LRU cache hit rate sensitivity to correlation between object size and popularity
