# N693: H_self=0.98 场景下，T_proc_pop=5ms 所需的硬件性能指标：单台 POP 服务器需处理 10,000 QPS（基于 200 万请求/天，峰

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N230

## Claim

H_self=0.98 场景下，T_proc_pop=5ms 所需的硬件性能指标：单台 POP 服务器需处理 10,000 QPS（基于 200 万请求/天，峰值系数 3，10 个 POP 分摊），且 CPU 利用率需低于 30% 以保证 P99 处理时间 < 5ms，需选用 32 核 CPU 且内存带宽 > 50GB/s。

## Corrected Claim

H_self=0.98 场景下，T_proc_pop=5ms 所需的硬件性能指标：单台 POP 服务器需处理约 7 QPS（基于 200 万请求/天，峰值系数 3，10 个 POP 分摊），且 CPU 利用率需低于 30% 以保证 P99 处理时间 < 5ms，需选用 32 核 CPU 且内存带宽 > 50GB/s。

## Evidence

[质询]数值推导存在内部矛盾：200万请求/天平均约23 QPS，即使乘以峰值系数3也仅为69 QPS，分摊到10个POP后单台仅约7 QPS，远小于陈述中的10,000 QPS；若按10,000 QPS反推，总请求量需达8.64亿/天，与题面200万/天严重不符。 | 先验知识/题面给定，但逻辑校验发现QPS计算与基础数据量级严重不匹配，存在硬逻辑错误。

## Search Query

edge server QPS 10000 P99 processing time 5ms hardware requirements
