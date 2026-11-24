# N738: 1Gbps公网带宽下的实际有效吞吐量：1Gbps理论上限为125MB/s。考虑TCP/IP协议栈开销（约10-15%）、ISP QoS限速（通常保证95%峰值）

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N256, N257, N258

## Claim

1Gbps公网带宽下的实际有效吞吐量：1Gbps理论上限为125MB/s。考虑TCP/IP协议栈开销（约10-15%）、ISP QoS限速（通常保证95%峰值）及网络抖动重传，实际有效下载速率约为100-110MB/s。此前计算的46.3天基于理想125MB/s，若按100MB/s计算，T_rto_cloud_full = 500TB / 100MB/s / 86400 ≈ 57.9天。

## Corrected Claim

1Gbps公网带宽下的实际有效吞吐量：1Gbps理论上限为125MB/s。考虑TCP/IP协议栈开销（约10-15%）、ISP QoS限速（通常保证95%峰值）及网络抖动重传，实际有效下载速率约为100-110MB/s。此前计算的46.3天基于理想125MB/s，若按100MB/s计算，T_rto_cloud_full = 500TB / 100MB/s / 86400 ≈ 57.9天。

## Evidence

先验知识/题面给定，逻辑校验通过：1Gbps=125MB/s，扣除10-15%开销后100-110MB/s符合工程常识；500TB/100MB/s/86400s≈57.87天，计算无误。

## Search Query

effective throughput 1Gbps internet connection TCP overhead ISP QoS real-world speed
