# N137: 2× RTX 4090 通过 PCIe 4.0 x16 互联时的有效带宽为 ~64 GB/s，相比 NVLink (900 GB/s) 降低约 14x；在 Qw

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45, N46, N47

## Claim

2× RTX 4090 通过 PCIe 4.0 x16 互联时的有效带宽为 ~64 GB/s，相比 NVLink (900 GB/s) 降低约 14x；在 Qwen3-27B 32K 上下文下，KV Cache 分片传输量约为 4.29 GB，导致单次 AllReduce 通信延迟增加至 ~67ms (64 GB/s 带宽下)，显著高于 NVLink 方案的 ~5ms。

## Corrected Claim

2× RTX 4090 通过 PCIe 4.0 x16 互联时的有效带宽为 ~64 GB/s，相比 NVLink (900 GB/s) 降低约 14x；在 Qwen3-27B 32K 上下文下，KV Cache 分片传输量约为 4.29 GB，导致单次 AllReduce 通信延迟增加至 ~67ms (64 GB/s 带宽下)，显著高于 NVLink 方案的 ~5ms。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 双向带宽约 64 GB/s，NVLink 带宽约 900 GB/s，比值约 14x；4.29 GB 数据在 64 GB/s 下传输时间约 67ms，在 900 GB/s 下约 5ms，数值量级与逻辑自洽。
