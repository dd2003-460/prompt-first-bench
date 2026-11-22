# N162: 对象 i 的驱逐速率 λ_evict_i 的解析表达式：λ_evict_i = (1 / T_res_i) * (1 - P_i_in_cache)，其中 P_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

对象 i 的驱逐速率 λ_evict_i 的解析表达式：λ_evict_i = (1 / T_res_i) * (1 - P_i_in_cache)，其中 P_i_in_cache 是对象 i 在缓存中的概率。在 LRU 稳态下，λ_evict_i 可近似为 (Sum_{j≠i} λ_j * P_j_in_cache) * (S_i / S_total_cache)，需基于缓存占用比例和竞争对象的频率分布计算。

## Corrected Claim

在 LRU 稳态且假设缓存空间主要被竞争对象占据的简化模型下，对象 i 的驱逐速率 λ_evict_i 可近似表示为 (Sum_{j≠i} λ_j * P_j_in_cache) * (S_i / S_total_cache)；该表达式依赖于缓存占用比例和竞争对象的频率分布，并非普适解析解。

## Evidence

[质询]该解析表达式缺乏普适性，仅在特定简化假设（如缓存完全由竞争对象填充且驱逐仅由竞争对象触发）下近似成立；在通用 LRU 稳态下，驱逐速率还受缓存总容量、对象大小分布及缓存命中率动态平衡的影响，直接给出此固定公式可能忽略边界条件或导致量纲/逻辑上的过度简化。 | 经验事实/理论模型结论，逻辑自洽但缺来源支持（本轮检索无可用来源），且公式为近似推导，无法排除其他更精确的稳态解可能性。

## Search Query

LRU eviction rate lambda_evict analytic formula cache occupancy competition frequency
