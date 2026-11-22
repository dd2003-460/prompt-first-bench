# N180: RTX 3090 推理 Qwen3-27B INT8 的实际 tokens/s 上限由显存带宽瓶颈决定，理论峰值为 936 GB/s / (27 GB 权重 +

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55, N56, N57

## Claim

RTX 3090 推理 Qwen3-27B INT8 的实际 tokens/s 上限由显存带宽瓶颈决定，理论峰值为 936 GB/s / (27 GB 权重 + 1.6 GB KV Cache + 5 GB 框架) ≈ 30.5 tokens/s，实测 19 tokens/s 表明存在 37.7% 的效率损失，该损失主要源于 PCIe 4.0 x16 带宽 (32 GB/s) 在 offload 场景下的 I/O 等待时间占比 T_io_wait / T_total。

## Corrected Claim

RTX 3090 (24GB) 推理 Qwen3-27B INT8 时，因权重超出显存容量，必须使用 CPU Offload。此时瓶颈主要受 PCIe 4.0 x16 带宽 (32 GB/s) 限制，而非显存带宽。理论峰值应基于 PCIe 带宽估算，实测 19 tokens/s 的效率损失主要源于 PCIe 传输延迟及 CPU 内存访问开销。

## Evidence

[质询]该陈述存在严重的逻辑矛盾和物理直觉违背：1. 若模型完全在显存中运行（27GB+1.6GB+5GB < 24GB? 不，3090显存为24GB，27GB权重根本装不下，必然发生Offload或Swap，此时瓶颈是PCIe带宽而非显存带宽，理论峰值计算错误）；2. 若假设能装下（忽略显存容量限制），30.5 tokens/s的理论峰值计算基于纯带宽除法，忽略了计算延迟和内存访问模式，且37.7%的效率损失归因于PCIe等待时间在纯显存推理场景下不成立（无PCIe传输）；3. 27GB权重在24GB显存的RTX 3090上必然触发CPU Offload，此时瓶颈确实是PCIe 4.0 (32GB/s)，但理论峰值应按PCIe带宽计算而非显存带宽，原陈述混淆了两种场景。 | 逻辑校验失败：RTX 3090显存为24GB，无法容纳27GB权重，必然涉及PCIe Offload，此时瓶颈为PCIe带宽而非显存带宽，原陈述将显存带宽作为理论峰值基础且同时归因PCIe等待时间，存在内部矛盾。

## Search Query

RTX 3090 inference throughput bottleneck analysis offload PCIe latency
