# N129: N54 公式 T_LRU = K_LRU / R_total 的适用性批判：该公式计算的是 '缓存中任意对象被访问的平均间隔' 或 '缓存更新周期的倒数'，而非

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

N54 公式 T_LRU = K_LRU / R_total 的适用性批判：该公式计算的是 '缓存中任意对象被访问的平均间隔' 或 '缓存更新周期的倒数'，而非单个对象的 '驻留时间'（Residency Time）。驻留时间是指对象从进入缓存到被驱逐的时间，对于热门对象，其驻留时间远大于 1/λ_i，因为 LRU 保护了频繁访问的对象。

## Corrected Claim

N54 公式 T_LRU = K_LRU / R_total 的适用性批判：该公式计算的是 '缓存中任意对象被访问的平均间隔' 或 '缓存更新周期的倒数'，而非单个对象的 '驻留时间'（Residency Time）。驻留时间是指对象从进入缓存到被驱逐的时间，对于热门对象，其驻留时间远大于 1/λ_i，因为 LRU 保护了频繁访问的对象。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

difference between cache hit rate and object residency time LRU
