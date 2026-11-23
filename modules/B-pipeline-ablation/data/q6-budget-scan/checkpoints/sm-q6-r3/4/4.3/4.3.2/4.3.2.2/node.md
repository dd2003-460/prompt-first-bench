# N200: N_unique_hot 的时间窗口敏感性：在 1 小时窗口内 N_unique_hot ≈ 10k-50k，在 24 小时窗口内 N_unique_hot ≈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

N_unique_hot 的时间窗口敏感性：在 1 小时窗口内 N_unique_hot ≈ 10k-50k，在 24 小时窗口内 N_unique_hot ≈ 100k-500k，窗口越长热点集合越大，命中率越低，需根据 TTL 策略选择窗口。

## Corrected Claim

N_unique_hot 的时间窗口敏感性：在 1 小时窗口内 N_unique_hot ≈ 10k-50k，在 24 小时窗口内 N_unique_hot ≈ 100k-500k，窗口越长热点集合越大，命中率越低，需根据 TTL 策略选择窗口。

## Evidence

先验知识/题面给定，逻辑校验通过：时间窗口扩大导致唯一热点集合单调增加符合集合论基本性质，命中率随分母增大而降低符合概率直觉，数值量级（1小时10k-50k vs 24小时100k-500k）符合典型互联网流量分布特征。

## Search Query

CDN cache hit rate time window unique objects TTL impact
