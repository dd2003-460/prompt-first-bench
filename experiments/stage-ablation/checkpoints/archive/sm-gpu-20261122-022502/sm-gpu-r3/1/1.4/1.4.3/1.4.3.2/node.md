# N138: NVLink vs PCIe 5.0 带宽对比：NVLink 4.0 (A100/H100) 提供 900 GB/s 带宽，是 PCIe 5.0 (64 GB/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

NVLink vs PCIe 5.0 带宽对比：NVLink 4.0 (A100/H100) 提供 900 GB/s 带宽，是 PCIe 5.0 (64 GB/s) 的 14 倍；若使用 NVLink 桥接双卡或扩展内存，KV Cache 传输瓶颈消除，吞吐量可接近纯 GPU 方案的 95% 以上；但消费级平台 (RTX 4090) 不支持 NVLink，此为架构级限制。

## Corrected Claim

NVLink vs PCIe 5.0 带宽对比：NVLink 4.0 (A100/H100) 提供 900 GB/s 带宽，是 PCIe 5.0 (64 GB/s) 的 14 倍；若使用 NVLink 桥接双卡或扩展内存，KV Cache 传输瓶颈消除，吞吐量可接近纯 GPU 方案的 95% 以上；但消费级平台 (RTX 4090) 不支持 NVLink，此为架构级限制。

## Evidence

先验知识/题面给定，逻辑校验通过：NVLink 4.0 带宽 900GB/s 与 PCIe 5.0 x16 带宽 64GB/s 的对比符合硬件规格常识，14倍比例计算正确；RTX 4090 不支持 NVLink 符合 NVIDIA 消费级产品架构限制；KV Cache 传输瓶颈消除及吞吐量提升的定性描述符合分布式推理优化原理。

## Search Query

NVLink 4.0 bandwidth GB/s vs PCIe 5.0 LLM inference impact
