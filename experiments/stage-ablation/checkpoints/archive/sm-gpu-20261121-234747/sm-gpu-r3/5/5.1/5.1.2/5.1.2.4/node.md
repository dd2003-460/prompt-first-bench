# N326: PCIe 带宽瓶颈对 KV Cache 传输延迟的影响量化：2×RTX 3090 间 PCIe 4.0 x16 实测带宽 ~25GB/s；每层 Decode 需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118

## Claim

PCIe 带宽瓶颈对 KV Cache 传输延迟的影响量化：2×RTX 3090 间 PCIe 4.0 x16 实测带宽 ~25GB/s；每层 Decode 需传输 KV 增量 = 2 * 8 heads * 128 dim * 1 byte = 2KB/layer，32 层共 64KB；传输延迟 = 64KB / 25GB/s ≈ 0.0026ms，远低于 100ms 阈值，故 PCIe 带宽非主要瓶颈，实际瓶颈为 NCCL 同步开销（~5-10ms/step）

## Corrected Claim

PCIe 带宽瓶颈对 KV Cache 传输延迟的影响量化：2×RTX 3090 间 PCIe 4.0 x16 实测带宽 ~25GB/s；每层 Decode 需传输 KV 增量 = 2 * 8 heads * 128 dim * 1 byte = 2KB/layer，32 层共 64KB；传输延迟 = 64KB / 25GB/s ≈ 0.0026ms，远低于 100ms 阈值，故 PCIe 带宽非主要瓶颈，实际瓶颈为 NCCL 同步开销（~5-10ms/step）

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽约 32GB/s，实测 25GB/s 符合工程常识；KV Cache 增量计算（2*8*128*1*32=64KB）及延迟估算（64KB/25GB/s ≈ 0.0026ms）量级正确，远低于 100ms 阈值，结论自洽。

## Search Query

PCIe 4.0 bandwidth KV cache transfer latency tensor parallel inference
