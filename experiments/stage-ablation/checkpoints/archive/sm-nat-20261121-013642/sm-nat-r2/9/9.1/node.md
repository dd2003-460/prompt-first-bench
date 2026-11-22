# N87: LFU 计数老化机制的噪声干扰量化：在 β=0.9 的平缓热度下，LFU 计数器标准差 σ_count 与请求频率 r_i 的比值 σ_count/r_i ≈ 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

LFU 计数老化机制的噪声干扰量化：在 β=0.9 的平缓热度下，LFU 计数器标准差 σ_count 与请求频率 r_i 的比值 σ_count/r_i ≈ 1/√r_i，当 r_i < 100 次/天时，噪声占比超过 10%，导致 LFU 误驱逐高热度对象

## Corrected Claim

LFU 计数老化机制的噪声干扰量化：在 β=0.9 的平缓热度下，LFU 计数器标准差 σ_count 与请求频率 r_i 的比值 σ_count/r_i ≈ 1/√r_i，当 r_i < 100 次/天时，噪声占比超过 10%，导致 LFU 误驱逐高热度对象

## Evidence

先验知识/题面给定，逻辑校验通过：基于泊松分布近似，计数标准差与均值之比为1/√r，当r<100时比值>0.1，推导自洽。

## Search Query

LFU counter noise interference flat frequency distribution beta 0.9
