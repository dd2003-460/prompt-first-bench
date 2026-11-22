# N43: CPU+GPU混合方案可行性阈值：仅当 Context_Length < 8K 或采用 INT4 量化将 KV Cache 大小压缩至 < 1 GB 时，PCI

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9, N10, N11

## Claim

CPU+GPU混合方案可行性阈值：仅当 Context_Length < 8K 或采用 INT4 量化将 KV Cache 大小压缩至 < 1 GB 时，PCIe 传输开销 (< 10ms) 才可忽略，此时吞吐量可接近纯 GPU 方案的 80-90%；对于 32K 上下文，除非使用 NVLink 或 CXL 内存扩展，否则 CPU+GPU 混合方案在交互式场景 (TTFT < 2s) 下不可行。

## Corrected Claim

CPU+GPU混合方案可行性阈值：仅当 Context_Length < 8K 或采用 INT4 量化将 KV Cache 大小压缩至 < 1 GB 时，PCIe 传输开销 (< 10ms) 才可忽略，此时吞吐量可接近纯 GPU 方案的 80-90%；对于 32K 上下文，除非使用 NVLink 或 CXL 内存扩展，否则 CPU+GPU 混合方案在交互式场景 (TTFT < 2s) 下不可行。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

hybrid CPU GPU inference feasibility threshold context length KV cache size optimization
