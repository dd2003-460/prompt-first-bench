# N373: 双卡 RTX 4090 (48GB) 运行 BF16 Qwen3-27B 时，需 offload 17.6GB 权重至 CPU 内存 (65.6GB - 48G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

双卡 RTX 4090 (48GB) 运行 BF16 Qwen3-27B 时，需 offload 17.6GB 权重至 CPU 内存 (65.6GB - 48GB = 17.6GB)，CPU 内存带宽 (约 50GB/s) 成为瓶颈，导致 Prefill 延迟增加约 0.35 秒 (17.6GB / 50GB/s)，总 Prefill 延迟从 1.2 秒升至 1.55 秒。

## Corrected Claim

双卡 RTX 4090 (48GB) 运行 BF16 Qwen3-27B 时，需 offload 17.6GB 权重至 CPU 内存 (65.6GB - 48GB = 17.6GB)，CPU 内存带宽 (约 50GB/s) 成为瓶颈，导致 Prefill 延迟增加约 0.35 秒 (17.6GB / 50GB/s)，总 Prefill 延迟从 1.2 秒升至 1.55 秒。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算（65.6-48=17.6, 17.6/50=0.352, 1.2+0.35=1.55）准确，物理量纲（GB/GB/s=s）合理，符合双卡显存不足需Offload导致带宽瓶颈的基本原理。
