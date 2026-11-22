# N47: 在LRU缓存中，对象i的更新导致其被驱逐并重新加载的概率 p_evict_i 取决于对象i在缓存中的驻留时间 T_res_i 与更新间隔 T_upd 的比值，近

- **status**: degraded
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

[质询]公式 p_evict_i ≈ 1 - exp(-T_res_i / T_upd) 在逻辑上存在严重缺陷：若 T_res_i 是对象在缓存中的驻留时间，而 T_upd 是更新间隔，通常 T_res_i 会远大于 T_upd（否则对象会被频繁更新从而保持热度，不易被驱逐），此时指数项趋近于0，概率趋近于1，意味着只要驻留时间超过一个更新间隔，驱逐概率就接近100%，这违背了LRU缓存中‘频繁访问/更新对象更可能驻留’的基本直觉。实际上，LRU的驱逐概率通常与‘自上次访问以来经过的时间’相对于‘缓存容量/访问速率’的关系有关，或者基于访问间隔分布的生存函数，而非简单的驻留时间与更新间隔的比值。此外，T_res_i 本身是随机变量，用其期望值代入指数公式缺乏严格的概率论推导支持。 | 先验知识/题面给定，逻辑校验发现公式物理/逻辑直觉不符（驻留时间长反而驱逐概率高？），且缺乏标准LRU理论支持，故降级。

## Search Query

LRU cache eviction probability upon object update steady state
