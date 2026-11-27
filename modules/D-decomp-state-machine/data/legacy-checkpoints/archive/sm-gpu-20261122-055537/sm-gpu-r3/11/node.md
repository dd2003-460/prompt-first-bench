# N35: 2x RTX 4090 (PCIe x16/x8 互联) 运行 Qwen3-27B (BF16) 时的张量并行 (Tensor Parallelism) 通信开

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

2x RTX 4090 (PCIe x16/x8 互联) 运行 Qwen3-27B (BF16) 时的张量并行 (Tensor Parallelism) 通信开销：由于 PCIe 4.0 x16 带宽 (~32 GB/s) 远低于 NVLink，在 32K 上下文下，All-Reduce 操作导致的延迟增加可达 15-20%，使得总吞吐量仅比单卡 INT4 方案高 10-15%，但成本翻倍。

## Corrected Claim

2x RTX 4090 (PCIe x16/x8 互联) 运行 Qwen3-27B (BF16) 时的张量并行 (Tensor Parallelism) 通信开销：由于 PCIe 4.0 x16 带宽 (~32 GB/s) 远低于 NVLink，在 32K 上下文下，All-Reduce 操作导致的延迟增加可达 15-20%，使得总吞吐量仅比单卡 INT4 方案高 10-15%，但成本翻倍。

## Evidence

检索失败: no sources from any channel (all 5 failed)
