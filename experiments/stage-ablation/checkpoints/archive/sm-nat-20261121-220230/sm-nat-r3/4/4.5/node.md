# N21: 相关性对更新折损的交互影响：负相关 (ρ=-0.3) 意味着热门对象（小对象）更新频率可能独立于热度或存在特定关联。若更新率 u 与热度 H 独立，则折损因子 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

相关性对更新折损的交互影响：负相关 (ρ=-0.3) 意味着热门对象（小对象）更新频率可能独立于热度或存在特定关联。若更新率 u 与热度 H 独立，则折损因子 H_eff/H_steady 在 LRU 和 LFU 下不同，因为 LRU 驱逐的是久未访问对象（可能包含高热度但低频对象），而 LFU 保留高热度对象。需量化交互项：ΔDiscount = f(ρ, u, α, β)。

## Corrected Claim

相关性对更新折损的交互影响：当更新率 u 与热度 H 存在负相关（如 ρ=-0.3）时，表明高热度对象倾向于具有较低的更新频率。这种统计依赖会导致 LRU 和 LFU 的折损因子 H_eff/H_steady 产生差异，因为 LRU 基于时间戳驱逐可能误删高热度低频对象，而 LFU 基于频率保留高热度对象。需通过模型量化交互项 ΔDiscount = f(ρ, u, α, β)。

## Evidence

[质询]该陈述将具体的数值参数（ρ=-0.3）与定性结论（更新频率独立或存在特定关联）强行绑定，且未提供推导依据；此外，'负相关意味着独立'在逻辑上是不成立的，负相关恰恰意味着存在统计依赖，而非独立。 | 逻辑校验发现内部矛盾：负相关（ρ=-0.3）表示变量间存在负向统计依赖，不能直接推导出'独立'或'特定关联'的模糊结论，且缺乏来源支持该具体数值与机制的对应关系。

## Search Query

cache invalidation rate correlation between object size and request frequency impact on LRU LFU
