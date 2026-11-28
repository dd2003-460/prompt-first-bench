# N40: RTX 4090 显存带宽为 1008 GB/s，而 RTX 5090 预计提升至 ~1792 GB/s (GDDR7)，对于内存受限的 LLM 推理，吞吐量近

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

RTX 4090 显存带宽为 1008 GB/s，而 RTX 5090 预计提升至 ~1792 GB/s (GDDR7)，对于内存受限的 LLM 推理，吞吐量近似正比于带宽 (Tokens/s ≈ Bandwidth / Weights_GB)，因此 5090 在 FP8 下的理论峰值吞吐约为 4090 的 1.78 倍

## Corrected Claim

RTX 4090 显存带宽为 1008 GB/s，而 RTX 5090 预计提升至 ~1792 GB/s (GDDR7)，对于内存受限的 LLM 推理，吞吐量近似正比于带宽 (Tokens/s ≈ Bandwidth / Weights_GB)，因此 5090 在 FP8 下的理论峰值吞吐约为 4090 的 1.78 倍

## Evidence

检索失败: no sources from any channel (all 5 failed)
