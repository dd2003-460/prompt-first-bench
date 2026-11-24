# N333: geo_share 三种分布形态 {Uniform, Zipf(1.0), Zipf(1.5)} 的具体参数化：Uniform 对应 α_i=1 (i=1..N

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

geo_share 三种分布形态 {Uniform, Zipf(1.0), Zipf(1.5)} 的具体参数化：Uniform 对应 α_i=1 (i=1..N_regions)；Zipf(1.0) 对应 α_i=1/i；Zipf(1.5) 对应 α_i=1/i^1.5，归一化后 Σα_i=1，用于模拟从均匀分散到高度集中的用户地理分布

## Corrected Claim

geo_share 三种分布形态 {Uniform, Zipf(1.0), Zipf(1.5)} 的具体参数化：Uniform 对应 α_i=1 (i=1..N_regions)；Zipf(1.0) 对应 α_i=1/i；Zipf(1.5) 对应 α_i=1/i^1.5，归一化后 Σα_i=1，用于模拟从均匀分散到高度集中的用户地理分布

## Evidence

先验知识/题面给定，逻辑校验通过：Uniform分布对应权重相等（归一化后α_i=1/N，比例上等价于α_i=1），Zipf分布标准定义为权重与排名成反比（α_i ∝ 1/i^s），归一化后满足Σα_i=1，符合地理分布模拟的常规参数化逻辑。
