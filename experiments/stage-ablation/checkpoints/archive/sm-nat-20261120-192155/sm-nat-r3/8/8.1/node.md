# N47: 在LRU缓存中，对象i的更新导致其被驱逐并重新加载的概率 p_evict_i 取决于对象i在缓存中的驻留时间 T_res_i 与更新间隔 T_upd 的比值，近

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N19

## Claim

在LRU缓存中，对象i的更新导致其被驱逐并重新加载的概率 p_evict_i 取决于对象i在缓存中的驻留时间 T_res_i 与更新间隔 T_upd 的比值，近似公式为 p_evict_i ≈ 1 - exp(-T_res_i / T_upd)，其中 T_upd = 1 / (U * f_i) 为对象i的平均更新间隔（f_i为对象i的访问频率占比）。

## Corrected Claim

在LRU缓存中，对象i被驱逐的概率主要取决于其自上次访问以来的时间间隔与缓存中其他对象访问频率的相对关系，通常可用访问间隔的生存函数或基于缓存容量的近似模型（如LRU-approximation）来描述，而非简单的 1 - exp(-T_res_i / T_upd) 形式。

## Evidence

父节点级核验未通过：有冗余（子节点2和3本质上是同一通用公式在特定边界条件（头部对象i=1和尾部对象i=k）下的具体数值代入与定性结论，属于高度冗余的实例化描述，而非正交的独立概念。此外，父节点给出的近似公式 p ≈ 1 - exp(-x) 与子节点1中使用的线性近似 p ≈ x 在数学上不完全一致（仅在x趋近于0时成立），虽然子节点结论中隐含了x<<1的前提，但子节点1未明确声明这一近似条件，存在逻辑跳跃。）

## Search Query

LRU cache eviction probability upon object update steady state
