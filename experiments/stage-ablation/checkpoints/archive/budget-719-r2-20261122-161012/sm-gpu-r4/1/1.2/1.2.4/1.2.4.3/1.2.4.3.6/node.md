# N367: N152 中 'Decode 吞吐量上限降至 ~0.14 tokens/s' 的计算逻辑错误：Decode 速度主要受限于显存带宽 (1008 GB/s) 而非

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N151, N152, N153

## Claim

N152 中 'Decode 吞吐量上限降至 ~0.14 tokens/s' 的计算逻辑错误：Decode 速度主要受限于显存带宽 (1008 GB/s) 而非 PCIe 带宽 (8 GB/s)，除非模型权重或 KV Cache 被 Offload 到 CPU 内存并通过 PCIe 传输；若 GPU 显存足够 (24GB) 且未启用 Offload，PCIe 带宽瓶颈仅影响初始化加载或 P2P 通信，不影响稳态 Decode 速度；因此，若 2x 4090 显存总和 48GB 足以容纳 FP8 模型 (27GB) + KV Cache，则 Decode 速度应接近单卡带宽限制的 2 倍 (考虑 TP 效率)，而非 0.14 tokens/s。

## Corrected Claim

N152 中 'Decode 吞吐量上限降至 ~0.14 tokens/s' 的计算逻辑错误：Decode 速度主要受限于显存带宽 (1008 GB/s) 而非 PCIe 带宽 (8 GB/s)，除非模型权重或 KV Cache 被 Offload 到 CPU 内存并通过 PCIe 传输；若 GPU 显存足够 (24GB) 且未启用 Offload，PCIe 带宽瓶颈仅影响初始化加载或 P2P 通信，不影响稳态 Decode 速度；因此，若 2x 4090 显存总和 48GB 足以容纳 FP8 模型 (27GB) + KV Cache，则 Decode 速度应接近单卡带宽限制的 2 倍 (考虑 TP 效率)，而非 0.14 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：GPU Decode 阶段主要受显存带宽限制，若模型完全驻留显存且未启用 Offload，PCIe 带宽确实不构成稳态瓶颈，原陈述中 0.14 tokens/s 的结论在逻辑上站不住脚。
