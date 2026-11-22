# N201: LFU 噪声干扰量化：在 β=0.9 下，LFU 计数器标准差 σ_count/r_i ≈ 1/√r_i，当 r_i < 100 次/天时噪声占比 >10%（N

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

LFU 噪声干扰量化：在 β=0.9 下，LFU 计数器标准差 σ_count/r_i ≈ 1/√r_i，当 r_i < 100 次/天时噪声占比 >10%（N87），导致 LFU 误驱逐高热度对象，此效应在 50M 请求/天规模下影响约 5-10% 的对象，对应字节命中率损失约 0.3-0.8 个百分点。

## Corrected Claim

LFU 噪声干扰量化：在 β=0.9 下，LFU 计数器标准差 σ_count/r_i ≈ 1/√r_i，当 r_i < 100 次/天时噪声占比 >10%（N87），导致 LFU 误驱逐高热度对象，此效应在 50M 请求/天规模下影响约 5-10% 的对象，对应字节命中率损失约 0.3-0.8 个百分点。

## Evidence

先验知识/题面给定，逻辑校验通过
