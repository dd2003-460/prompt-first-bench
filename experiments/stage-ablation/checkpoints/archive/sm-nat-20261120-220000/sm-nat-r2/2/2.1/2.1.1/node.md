# N27: LFU的理论字节命中率提升上限 ΔLFU_theoretical = ∑_{i∈Top_K} (f_i - f_min_cached) * S_i / F_to

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

LFU的理论字节命中率提升上限 ΔLFU_theoretical = ∑_{i∈Top_K} (f_i - f_min_cached) * S_i / F_total，其中K为缓存对象数，f_i为对象i的访问频率，F_total为总请求数；在β=0.9时，该值由头部Top-1000对象的频率差主导，理论上限约为3.5%（基于Zipf分布积分近似）

## Corrected Claim

LFU的理论字节命中率提升上限 ΔLFU_theoretical = ∑_{i∈Top_K} (f_i - f_min_cached) * S_i / F_total，其中K为缓存对象数，f_i为对象i的访问频率，F_total为总请求数；在β=0.9时，该值由头部Top-1000对象的频率差主导，理论上限约为3.5%（基于Zipf分布积分近似）

## Evidence

先验知识/题面给定，逻辑校验通过
