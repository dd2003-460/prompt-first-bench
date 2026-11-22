# N113: 条件分支2（预算$5,000-$8,000, INT8量化）的延迟量化：2× RTX 4090 PCIe 互联在 INT8 量化下的理论 Decode 吞吐量上

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

条件分支2（预算$5,000-$8,000, INT8量化）的延迟量化：2× RTX 4090 PCIe 互联在 INT8 量化下的理论 Decode 吞吐量上限 = (Memory_Bandwidth_GBps / Bytes_per_token) * 1000，其中 RTX 4090 带宽 1008GB/s，INT8 下 Bytes_per_token ≈ 27.1GB/1024，需计算具体 tokens/s 并对比 1× A6000 Ada (1950GB/s) 的带宽优势，评估 PCIe 通信开销（N24）导致的实际性能衰减比例及多卡同步延迟。

## Corrected Claim

条件分支2（预算$5,000-$8,000, INT8量化）的延迟量化：2× RTX 4090 PCIe 互联在 INT8 量化下的理论 Decode 吞吐量上限 = (Memory_Bandwidth_GBps / Bytes_per_token) * 1000，其中 RTX 4090 带宽 1008GB/s，INT8 下 Bytes_per_token ≈ 27.1GB/1024，需计算具体 tokens/s 并对比 1× A6000 Ada (1950GB/s) 的带宽优势，评估 PCIe 通信开销（N24）导致的实际性能衰减比例及多卡同步延迟。

## Evidence

父节点级核验未通过：不完备（子节点覆盖了带宽计算、通信开销、吞吐量推导及对比方案验证，逻辑链条完整且无重复。但父节点明确要求评估‘多卡同步延迟’，而现有子节点仅量化了通信带宽开销（Communication_Overhead_Ratio），未涉及同步等待时间（Sync Latency）对整体 Decode 步骤时间的具体影响，导致覆盖不全。）
