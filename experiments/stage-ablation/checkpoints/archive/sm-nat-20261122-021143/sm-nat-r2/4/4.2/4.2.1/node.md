# N45: 对象在 LRU 缓存中的驻留时间 T_res(k) 由对象大小 S(k) 和该对象的热度 R(k) 决定：T_res(k) = S(k) / R(k)（单位：天

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

对象在 LRU 缓存中的驻留时间 T_res(k) 由对象大小 S(k) 和该对象的热度 R(k) 决定：T_res(k) = S(k) / R(k)（单位：天），其中 S(k) 服从 Pareto(α=1.1) 且与热度负相关，R(k) 服从 Zipf(β=0.9)。

## Corrected Claim

对象在 LRU 缓存中的驻留时间 T_res(k) 由对象大小 S(k) 和该对象的热度 R(k) 决定：T_res(k) = S(k) / R(k)（单位：天），其中 S(k) 服从 Pareto(α=1.1) 且与热度负相关，R(k) 服从 Zipf(β=0.9)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache residence time formula size over request rate
