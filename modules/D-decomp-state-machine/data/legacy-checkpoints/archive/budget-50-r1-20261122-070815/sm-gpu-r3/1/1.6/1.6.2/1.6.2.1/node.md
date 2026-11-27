# N205: 修正 N53 中的带宽假设：RTX 4090 与 CPU 间通信走 PCIe 4.0 x16，理论双向带宽为 64 GB/s (32 GB/s 单向)，而非 3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53, N54, N55

## Claim

修正 N53 中的带宽假设：RTX 4090 与 CPU 间通信走 PCIe 4.0 x16，理论双向带宽为 64 GB/s (32 GB/s 单向)，而非 32 GB/s；若 KV Cache 卸载至 CPU，每次生成需读取的 KV 数据量并非全量 2.15 GB，而是仅当前 token 对应的增量 KV 及注意力计算所需的局部 KV，具体读取频率取决于 vLLM/llama.cpp 的 PagedAttention 实现机制，需核实每步实际 PCIe 传输字节数。

## Corrected Claim

修正 N53 中的带宽假设：RTX 4090 与 CPU 间通信走 PCIe 4.0 x16，理论双向带宽为 64 GB/s (32 GB/s 单向)，而非 32 GB/s；若 KV Cache 卸载至 CPU，每次生成需读取的 KV 数据量并非全量 2.15 GB，而是仅当前 token 对应的增量 KV 及注意力计算所需的局部 KV，具体读取频率取决于 vLLM/llama.cpp 的 PagedAttention 实现机制，需核实每步实际 PCIe 传输字节数。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽确为 32 GB/s 单向（64 GB/s 双向），且 KV Cache 增量读取符合 PagedAttention 机制原理。

## Search Query

PCIe 4.0 x16 theoretical bandwidth bidirectional GB/s RTX 4090
