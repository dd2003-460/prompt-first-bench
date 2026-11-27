# N142: P_hit_on_updated 的精确数值取决于缓存策略对热度分布的截断阈值 f_th；在 LRU 策略下，f_th 由缓存容量 C 和对象大小 S 决定，需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

P_hit_on_updated 的精确数值取决于缓存策略对热度分布的截断阈值 f_th；在 LRU 策略下，f_th 由缓存容量 C 和对象大小 S 决定，需通过积分 ∫_{f_th}^{∞} f(f) df 计算，而非固定常数 0.005。

## Corrected Claim

P_hit_on_updated 的精确数值取决于缓存策略对热度分布的截断阈值 f_th；在 LRU 策略下，f_th 由缓存容量 C 和对象大小 S 决定，需通过积分 ∫_{f_th}^{∞} f(f) df 计算，而非固定常数 0.005。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU缓存的命中率确实取决于容量C与对象大小S决定的截断阈值，需通过热度分布积分计算，而非固定常数。
