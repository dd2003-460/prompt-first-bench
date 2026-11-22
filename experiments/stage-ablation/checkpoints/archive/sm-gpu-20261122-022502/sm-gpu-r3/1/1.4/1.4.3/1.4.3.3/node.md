# N139: CXL 内存扩展方案的可行性与延迟：CXL 1.1/2.0 内存池化可提供 TB 级容量，但访问延迟比本地 DRAM 高 10-20% (约 100-150ns

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

CXL 内存扩展方案的可行性与延迟：CXL 1.1/2.0 内存池化可提供 TB 级容量，但访问延迟比本地 DRAM 高 10-20% (约 100-150ns)，比 PCIe 传输 KV Cache 快但比本地内存慢；对于 32K 上下文，CXL 方案可避免 Offload 至 CPU 的瓶颈，但需主板和 CPU 支持 (如 Intel Sapphire Rapids)，当前消费级平台不支持。

## Corrected Claim

CXL 内存扩展方案的可行性与延迟：CXL 1.1/2.0 内存池化可提供 TB 级容量，但访问延迟比本地 DRAM 高 10-20% (约 100-150ns)，比 PCIe 传输 KV Cache 快但比本地内存慢；对于 32K 上下文，CXL 方案可避免 Offload 至 CPU 的瓶颈，但需主板和 CPU 支持 (如 Intel Sapphire Rapids)，当前消费级平台不支持。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CXL memory latency ns vs DRAM LLM inference feasibility
