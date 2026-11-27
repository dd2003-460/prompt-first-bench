# N165: 尾部对象（Bottom 90%）的访问频率 λ_cold 极低，接近 0，其驻留时间 T_residence_cold 由缓存淘汰策略决定，在 LRU 下可能长

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

尾部对象（Bottom 90%）的访问频率 λ_cold 极低，接近 0，其驻留时间 T_residence_cold 由缓存淘汰策略决定，在 LRU 下可能长达数天或永久（若无更新），导致平均驻留时间加权值被冷对象拉高

## Corrected Claim

尾部对象（Bottom 90%）的访问频率 λ_cold 极低，接近 0，其驻留时间 T_residence_cold 由缓存淘汰策略决定，在 LRU 下可能长达数天或永久（若无更新），导致平均驻留时间加权值被冷对象拉高

## Evidence

先验知识/题面给定，逻辑校验通过：LRU策略下冷对象若长期未被访问确实会驻留直至被新热对象挤出，其驻留时间取决于缓存容量和访问模式，量级合理且符合缓存理论基本直觉。
