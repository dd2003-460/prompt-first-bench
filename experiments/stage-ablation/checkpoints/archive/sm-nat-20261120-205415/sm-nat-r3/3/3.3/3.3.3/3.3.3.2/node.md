# N153: LFU 与 LRU 驻留时间比 λ_f / λ_l 的估算：假设 LFU 缓存对象平均大小 s_f=0.8MB，LRU 缓存对象平均大小 s_l=1.2MB，且

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

LFU 与 LRU 驻留时间比 λ_f / λ_l 的估算：假设 LFU 缓存对象平均大小 s_f=0.8MB，LRU 缓存对象平均大小 s_l=1.2MB，且 LFU 对象平均热度 h_f=1.2 倍，LRU 对象平均热度 h_l=1.0 倍，则 λ_f / λ_l ≈ (s_l * h_l) / (s_f * h_f) = (1.2*1.0)/(0.8*1.2) = 1.25，表明 LFU 驻留时间比 LRU 长 25%。

## Corrected Claim

LFU 与 LRU 驻留时间比 λ_f / λ_l 的估算：假设 LFU 缓存对象平均大小 s_f=0.8MB，LRU 缓存对象平均大小 s_l=1.2MB，且 LFU 对象平均热度 h_f=1.2 倍，LRU 对象平均热度 h_l=1.0 倍，则 λ_f / λ_l ≈ (s_l * h_l) / (s_f * h_f) = (1.2*1.0)/(0.8*1.2) = 1.25，表明 LFU 驻留时间比 LRU 长 25%。

## Evidence

先验知识/题面给定，逻辑校验通过
