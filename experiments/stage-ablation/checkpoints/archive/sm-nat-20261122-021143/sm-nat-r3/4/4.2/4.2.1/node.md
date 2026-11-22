# N45: 对象在 LRU 缓存中的驻留时间 T_res(k) 由对象大小 S(k) 和该对象的热度 R(k) 决定：T_res(k) = S(k) / R(k)（单位：天

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（子节点2和子节点3本质上是同一解析表达式在不同k值下的特例（冗余）；且父节点强调S(k)与R(k)负相关，但子节点1推导中S(k)和R(k)均仅依赖k，未体现二者的联合分布或条件相关性（完备性缺失）。）

## Search Query

LRU cache residence time formula size over request rate
