# N188: LFU 驱逐头部对象的概率 E_evict_LFU 在稳态下近似为 0，其非零部分来源于频率计数器精度误差或负载突变。量化形式为 E_evict_LFU ≈ P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

LFU 驱逐头部对象的概率 E_evict_LFU 在稳态下近似为 0，其非零部分来源于频率计数器精度误差或负载突变。量化形式为 E_evict_LFU ≈ P(λ_i < f_threshold | i ∈ Top 10%)，在理想稳态且计数器无限精度下该值为 0。

## Corrected Claim

LFU 驱逐头部对象的概率 E_evict_LFU 在稳态下近似为 0，其非零部分来源于频率计数器精度误差或负载突变。量化形式为 E_evict_LFU ≈ P(λ_i < f_threshold | i ∈ Top 10%)，在理想稳态且计数器无限精度下该值为 0。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 算法定义即基于访问频率，稳态下头部对象频率最高，驱逐概率理论上为 0，非零仅源于误差或突变，符合算法原理。
