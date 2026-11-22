# N152: LFU 策略下对象的平均驻留时间 λ_f 的计算公式为 λ_f = C / (Q_f * E[S_f])，其中 Q_f 为 LFU 缓存对象的总请求率，E[S_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

LFU 策略下对象的平均驻留时间 λ_f 的计算公式为 λ_f = C / (Q_f * E[S_f])，其中 Q_f 为 LFU 缓存对象的总请求率，E[S_f] 为 LFU 缓存对象的平均大小；由于 LFU 保留高频小对象，Q_f 通常大于 LRU 的 Q_l，E[S_f] 小于 E[S_l]。

## Corrected Claim

LFU 策略下对象的平均驻留时间 λ_f 的计算公式为 λ_f = C / (Q_f * E[S_f])，其中 Q_f 为 LFU 缓存对象的总请求率，E[S_f] 为 LFU 缓存对象的平均大小；由于 LFU 保留高频小对象，Q_f 通常大于 LRU 的 Q_l，E[S_f] 小于 E[S_l]。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合利特尔法则（Little's Law）在缓存驻留时间上的应用（驻留时间=容量/吞吐量），且LFU保留高频小对象的特性导致Q_f高、E[S_f]低符合缓存理论直觉。
