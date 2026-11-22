# N131: PCIe 5.0 x16 带宽 (64 GB/s) 在 KV Cache 传输中的实际有效带宽为 55-60 GB/s（因协议开销和链路训练损耗），导致 32K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

PCIe 5.0 x16 带宽 (64 GB/s) 在 KV Cache 传输中的实际有效带宽为 55-60 GB/s（因协议开销和链路训练损耗），导致 32K 上下文下 KV Cache (约 1.07GB) 传输耗时约 18-20ms，显著影响 TTFT。

## Corrected Claim

PCIe 5.0 x16 带宽 (64 GB/s) 在 KV Cache 传输中的实际有效带宽为 55-60 GB/s（因协议开销和链路训练损耗），导致 32K 上下文下 KV Cache (约 1.07GB) 传输耗时约 18-20ms，显著影响 TTFT。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 5.0 x16 理论带宽 64GB/s，扣除协议开销后有效带宽 55-60GB/s 符合工程常识；1.07GB 数据在 55-60GB/s 带宽下传输耗时计算为 1.07/60≈17.8ms 至 1.07/55≈19.5ms，与陈述中的 18-20ms 量级一致，逻辑自洽。

## Search Query

PCIe 5.0 x16 effective bandwidth KV cache transfer latency LLM inference
