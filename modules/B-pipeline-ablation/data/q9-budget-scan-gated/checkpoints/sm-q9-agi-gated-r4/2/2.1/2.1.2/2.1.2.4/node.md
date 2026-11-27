# N61: V100 SXM2的PCIe/NVLink拓扑对TP=4集合通信的影响：NVLink3带宽300GB/s但延迟约2μs，AllReduce的启动延迟在batch

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

V100 SXM2的PCIe/NVLink拓扑对TP=4集合通信的影响：NVLink3带宽300GB/s但延迟约2μs，AllReduce的启动延迟在batch_size=1时不可忽略，实际通信延迟 = 0.055ms + 2μs ≈ 0.057ms

## Corrected Claim

V100 SXM2的PCIe/NVLink拓扑对TP=4集合通信的影响：NVLink3带宽300GB/s但延迟约2μs，AllReduce的启动延迟在batch_size=1时不可忽略，实际通信延迟 = 0.055ms + 2μs ≈ 0.057ms

## Evidence

先验知识/题面给定，逻辑校验通过
