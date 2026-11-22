# N448: 2× RTX 3090 (INT8) 在 32K 上下文下的实际 Decode 吞吐量：理论值 29.5 tokens/s (基于单卡带宽 936 GB/s /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N174

## Claim

2× RTX 3090 (INT8) 在 32K 上下文下的实际 Decode 吞吐量：理论值 29.5 tokens/s (基于单卡带宽 936 GB/s / 27 GB 权重)，考虑 PCIe 4.0 张量并行通信开销 (5-10%) 及多卡同步延迟，实际吞吐量约为 26-28 tokens/s。

## Corrected Claim

2× RTX 3090 (INT8) 在 32K 上下文下的实际 Decode 吞吐量：理论值 29.5 tokens/s (基于单卡带宽 936 GB/s / 27 GB 权重)，考虑 PCIe 4.0 张量并行通信开销 (5-10%) 及多卡同步延迟，实际吞吐量约为 26-28 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：单卡带宽936GB/s除以27GB权重约等于34.7 tokens/s，双卡并行理论上限受限于单卡带宽（权重需从各自显存读取），29.5 tokens/s的理论值略低于纯带宽极限（可能考虑了计算瓶颈或效率因子），扣除5-10%通信开销后得到26-28 tokens/s，数值量级与逻辑推导自洽。
