# N153: Qwen3-27B 在 NVFP4 (NVIDIA FP4) 精度下的权重显存占用约为 13.5GB (27B * 0.5 bytes)，但需额外存储 Bloc

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 在 NVFP4 (NVIDIA FP4) 精度下的权重显存占用约为 13.5GB (27B * 0.5 bytes)，但需额外存储 Block Scale 因子，实际占用约为 14.0-14.5GB；该精度依赖 Blackwell 架构 (B200/B100) 或特定 CUDA 12.8+ 内核支持，在 RTX 4090 (Ada) 上无法原生高效执行，需回退至 W4 INT4 或 FP8。

## Corrected Claim

Qwen3-27B 在 NVFP4 (NVIDIA FP4) 精度下的权重显存占用约为 13.5GB (27B * 0.5 bytes)，但需额外存储 Block Scale 因子，实际占用约为 14.0-14.5GB；该精度依赖 Blackwell 架构 (B200/B100) 或特定 CUDA 12.8+ 内核支持，在 RTX 4090 (Ada) 上无法原生高效执行，需回退至 W4 INT4 或 FP8。

## Evidence

检索失败: no sources from any channel (all 5 failed)
