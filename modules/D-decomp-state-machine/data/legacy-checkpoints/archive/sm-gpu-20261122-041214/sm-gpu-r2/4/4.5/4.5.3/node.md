# N137: 对比 NVLink (A100/H100) 与 PCIe 在长上下文 Prefill 阶段的差异：在 Prefill 阶段 (seq_len=32K)，All-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

对比 NVLink (A100/H100) 与 PCIe 在长上下文 Prefill 阶段的差异：在 Prefill 阶段 (seq_len=32K)，All-Reduce 数据量变为 32K * 4096 * 2 bytes ≈ 256MB。此时 PCIe 带宽成为瓶颈，2x 4090 传输 256MB 需 ~10ms，而 2x A100 (NVLink 600GB/s) 仅需 ~0.4ms。因此，长上下文高负载场景下，NVLink 卡的通信优势显著，TCO 对比需区分 Prefill 密集型和 Decode 密集型负载。

## Corrected Claim

对比 NVLink (A100/H100) 与 PCIe 在长上下文 Prefill 阶段的差异：在 Prefill 阶段 (seq_len=32K)，All-Reduce 数据量变为 32K * 4096 * 2 bytes ≈ 256MB。此时 PCIe 带宽成为瓶颈，2x 4090 传输 256MB 需 ~10ms，而 2x A100 (NVLink 600GB/s) 仅需 ~0.4ms。因此，长上下文高负载场景下，NVLink 卡的通信优势显著，TCO 对比需区分 Prefill 密集型和 Decode 密集型负载。

## Evidence

先验知识/题面给定，逻辑校验通过：数据量计算 (32K*4096*2B=256MB) 正确；PCIe 3.0 x16 带宽约 12.5GB/s，传输 256MB 耗时约 20ms，文中估算 10ms 可能基于 PCIe 4.0 或理想情况，量级合理；NVLink 600GB/s 传输 256MB 耗时约 0.43ms，与文中 0.4ms 一致；结论符合硬件通信瓶颈的基本物理直觉。
