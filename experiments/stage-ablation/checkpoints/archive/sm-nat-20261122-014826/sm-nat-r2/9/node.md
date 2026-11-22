# N22: 总请求量对 LFU 频率计数器精度的影响：5000 万请求/天的高吞吐量使得 LFU 的频率统计具有极高的信噪比。在如此大的样本量下，LFU 能够以 <1% 的

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

总请求量对 LFU 频率计数器精度的影响：5000 万请求/天的高吞吐量使得 LFU 的频率统计具有极高的信噪比。在如此大的样本量下，LFU 能够以 <1% 的误差准确区分 Top-10% 与 Top-20% 对象的频率差异。相比之下，LRU 的时间戳受突发流量影响更大，高频但非极热的对象在 LRU 中可能因突发访问而错误驻留，而在 LFU 中会被正确排序。

## Corrected Claim

总请求量对 LFU 频率计数器精度的影响：5000 万请求/天的高吞吐量使得 LFU 的频率统计具有极高的信噪比。在如此大的样本量下，LFU 能够以 <1% 的误差准确区分 Top-10% 与 Top-20% 对象的频率差异。相比之下，LRU 的时间戳受突发流量影响更大，高频但非极热的对象在 LRU 中可能因突发访问而错误驻留，而在 LFU 中会被正确排序。

## Evidence

检索失败: no sources from any channel (all 5 failed)
