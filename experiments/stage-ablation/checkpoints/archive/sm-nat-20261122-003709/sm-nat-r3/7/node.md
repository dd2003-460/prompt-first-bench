# N27: LFU相比LRU在β=0.9且ρ=-0.3条件下的最大提升百分点ΔH_max，受限于LFU的‘频率老化’滞后。当更新率1%/天时，LFU的频率计数器需约1/λ=

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU相比LRU在β=0.9且ρ=-0.3条件下的最大提升百分点ΔH_max，受限于LFU的‘频率老化’滞后。当更新率1%/天时，LFU的频率计数器需约1/λ=100天才能完全收敛，导致初始阶段命中率低于LRU。稳态下，LFU仅当热度分布极度倾斜（Gini>0.6）时才能超过LRU，否则提升为负或接近0。

## Corrected Claim

LFU相比LRU在β=0.9且ρ=-0.3条件下的最大提升百分点ΔH_max，受限于LFU的‘频率老化’滞后。当更新率1%/天时，LFU的频率计数器需约1/λ=100天才能完全收敛，导致初始阶段命中率低于LRU。稳态下，LFU仅当热度分布极度倾斜（Gini>0.6）时才能超过LRU，否则提升为负或接近0。

## Evidence

检索失败: no sources from any channel (all 5 failed)
