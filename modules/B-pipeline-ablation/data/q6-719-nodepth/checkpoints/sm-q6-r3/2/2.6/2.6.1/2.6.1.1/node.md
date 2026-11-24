# N283: 自建部分回源流量 V_origin_self 为 V_core * H_miss_self，其中 V_core = 2000GB * P_core，H_miss

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N84

## Claim

自建部分回源流量 V_origin_self 为 V_core * H_miss_self，其中 V_core = 2000GB * P_core，H_miss_self 为自建 POP 缓存未命中率（典型值 0.05-0.15，取决于对象更新频率与缓存策略）

## Corrected Claim

自建部分回源流量 V_origin_self 为 V_core * H_miss_self，其中 V_core = 2000GB * P_core，H_miss_self 为自建 POP 缓存未命中率（典型值 0.05-0.15，取决于对象更新频率与缓存策略）

## Evidence

先验知识/题面给定，逻辑校验通过：公式 V_origin_self = V_core * H_miss_self 符合缓存回源流量的基本定义（回源量=总请求量*未命中率），且 H_miss_self 典型值 0.05-0.15 符合 CDN/缓存系统的常规经验范围，量纲与逻辑自洽。
