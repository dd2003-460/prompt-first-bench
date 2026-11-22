# N136: 工作点 2 的驻留时间 T_resident ≈ 10 天是由 LRU 缓存容量 C=128GB 和头部对象访问频率决定的。具体推导：T_resident = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

工作点 2 的驻留时间 T_resident ≈ 10 天是由 LRU 缓存容量 C=128GB 和头部对象访问频率决定的。具体推导：T_resident = C / (Σ_{i=1}^{k_res} λ_i * S_i)。在混合场景下，假设 k_res 对应热度分位点 q，使得累计字节占缓存容量 100%。若头部 1% 对象占据 50% 字节流量（基于 ρ=-0.3 修正），则 T_resident 的计算需代入 λ_i = R * p_i (p_i 为热度概率) 和 S_i 的条件期望。此值直接决定 P_invalidate 的指数项。

## Corrected Claim

工作点 2 的驻留时间 T_resident ≈ 10 天是由 LRU 缓存容量 C=128GB 和头部对象访问频率决定的。具体推导：T_resident = C / (Σ_{i=1}^{k_res} λ_i * S_i)。在混合场景下，假设 k_res 对应热度分位点 q，使得累计字节占缓存容量 100%。若头部 1% 对象占据 50% 字节流量（基于 ρ=-0.3 修正），则 T_resident 的计算需代入 λ_i = R * p_i (p_i 为热度概率) 和 S_i 的条件期望。此值直接决定 P_invalidate 的指数项。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 T_resident = C / (Σ λ_i * S_i) 量纲正确（GB / (GB/s) = s），且符合 LRU 缓存驻留时间的定义（缓存容量除以头部对象的字节流出率），数值量级在合理范围内。

## Search Query

LRU cache residency time calculation Pareto workload
