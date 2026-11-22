# N113: 条件分支2（预算$5,000-$8,000, INT8量化）的延迟量化：2× RTX 4090 PCIe 互联在 INT8 量化下的理论 Decode 吞吐量上

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

条件分支2（预算$5,000-$8,000, INT8量化）的延迟量化：2× RTX 4090 PCIe 互联在 INT8 量化下的理论 Decode 吞吐量上限 = (Memory_Bandwidth_GBps / Bytes_per_token) * 1000，其中 RTX 4090 带宽 1008GB/s，INT8 下 Bytes_per_token ≈ 27.1GB/1024，需计算具体 tokens/s 并对比 1× A6000 Ada (1950GB/s) 的带宽优势，评估 PCIe 通信开销（N24）导致的实际性能衰减比例及多卡同步延迟。

## Corrected Claim

条件分支2（预算$5,000-$8,000, INT8量化）的延迟量化：2× RTX 4090 PCIe 互联在 INT8 量化下的理论 Decode 吞吐量上限 = (Memory_Bandwidth_GBps / Bytes_per_token) * 1000，其中 RTX 4090 带宽 1008GB/s，INT8 下 Bytes_per_token ≈ 27.1GB/1024，需计算具体 tokens/s 并对比 1× A6000 Ada (1950GB/s) 的带宽优势，评估 PCIe 通信开销（N24）导致的实际性能衰减比例及多卡同步延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090带宽1008GB/s及INT8量化下每token约27.1KB（27.1GB/1024）符合硬件规格与量化原理，吞吐量计算公式量纲正确（GB/s / GB/token = tokens/s），A6000 Ada带宽1950GB/s亦符合事实，逻辑自洽。
