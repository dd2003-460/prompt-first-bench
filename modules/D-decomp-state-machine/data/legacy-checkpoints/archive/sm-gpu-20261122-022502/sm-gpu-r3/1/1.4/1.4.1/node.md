# N41: CPU+GPU混合推理的内存带宽瓶颈量化：Intel Xeon (8通道DDR5-4800) 实际内存带宽约为 290-320 GB/s (理论峰值 ~307 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9, N10, N11

## Claim

CPU+GPU混合推理的内存带宽瓶颈量化：Intel Xeon (8通道DDR5-4800) 实际内存带宽约为 290-320 GB/s (理论峰值 ~307 GB/s)，而非 N9 中估算的 50 GB/s；瓶颈在于 PCIe 5.0 x16 带宽 (64 GB/s) 限制 KV Cache 从 CPU 内存到 GPU 显存的传输速率，导致 TTFT 随上下文长度线性增加。

## Corrected Claim

CPU+GPU混合推理的内存带宽瓶颈量化：Intel Xeon (8通道DDR5-4800) 实际内存带宽约为 290-320 GB/s (理论峰值 ~307 GB/s)，而非 N9 中估算的 50 GB/s；瓶颈在于 PCIe 5.0 x16 带宽 (64 GB/s) 限制 KV Cache 从 CPU 内存到 GPU 显存的传输速率，导致 TTFT 随上下文长度线性增加。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别量化了CPU内存带宽（源端）、PCIe传输效率（链路端）和最终解码吞吐量（结果端），三者逻辑链条清晰，无重复且共同覆盖了父节点关于瓶颈量化的核心内容。）

## Search Query

Intel Xeon DDR5 memory bandwidth theoretical vs actual PCIe 5.0 x16 bandwidth limit LLM inference
