# N128: 工作点 B（低字节驱逐/长 T_res）：基于 N78 的 Eviction_Rate = 1.1 * 10^11 bytes/day，T_res = 128 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

工作点 B（低字节驱逐/长 T_res）：基于 N78 的 Eviction_Rate = 1.1 * 10^11 bytes/day，T_res = 128 * 10^9 / 1.1 * 10^11 days ≈ 0.00116 days ≈ 1.67 分钟。此驻留时间较长，允许对象在缓存中停留更久，有助于捕捉低频但高价值的访问模式，但可能增加脏数据风险。

## Corrected Claim

工作点 B（低字节驱逐/长 T_res）：基于 N78 的 Eviction_Rate = 1.1 * 10^11 bytes/day，T_res = 128 * 10^9 / 1.1 * 10^11 days ≈ 0.00116 days ≈ 1.67 分钟。此驻留时间较长，允许对象在缓存中停留更久，有助于捕捉低频但高价值的访问模式，但可能增加脏数据风险。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 128e9 / 1.1e11 ≈ 0.0011636 days，换算为分钟 0.0011636 * 24 * 60 ≈ 1.675 分钟，与陈述一致；逻辑上长驻留时间确实有助于捕捉低频访问但增加脏数据风险，符合缓存原理。
