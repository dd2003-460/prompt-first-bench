# N563: A100 80GB 运行 Qwen3-27B BF16 时，Batch Size=20 的吞吐量上限受限于 GPU 计算能力而非显存，理论 Prefill 吞吐

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N234

## Claim

A100 80GB 运行 Qwen3-27B BF16 时，Batch Size=20 的吞吐量上限受限于 GPU 计算能力而非显存，理论 Prefill 吞吐量 = (989 TFLOPS * 0.5 MFU) / (2 * 27e9 * 32768) ≈ 28.7 tokens/s/请求，20 并发时总吞吐量 ≈ 574 tokens/s，但实际受内存带宽 (2039 GB/s) 限制，Decode 阶段单请求速度 ≈ (54 GB + 1.2 GB) / (2039 GB/s * 0.8) ≈ 35 ms/token，20 并发时总 Decode 吞吐量 ≈ 571 tokens/s，与 Prefill 吞吐量平衡。

## Corrected Claim

A100 80GB 运行 Qwen3-27B BF16 时，Batch Size=20 的 Decode 阶段受限于内存带宽，单请求速度约 35 ms/token，总吞吐量约 571 tokens/s；Prefill 阶段吞吐量远高于 Decode，通常不是瓶颈，具体数值需根据实际序列长度和 MFU 重新计算，原陈述中 Prefill 吞吐量 28.7 tokens/s/请求 的计算逻辑有误。

## Evidence

[质询]Prefill 吞吐量计算存在严重的量纲和逻辑错误：公式 (989 TFLOPS * 0.5) / (2 * 27e9 * 32768) 计算的是单次前向传播（处理 32768 个 token）所需的理论时间倒数或类似指标，其结果单位并非 tokens/s/请求。实际上，对于长序列 Prefill，吞吐量通常受限于总 FLOPs 与序列长度的关系，且 28.7 tokens/s/请求 的数值对于 A100 处理 32k 序列的 Prefill 阶段而言极低（通常 Prefill 速度远高于 Decode，且 28.7 更接近 Decode 速度而非 Prefill 速度，或者该公式完全误用了 FLOPs 定义）。此外，Decode 阶段显存占用 54GB 对于 27B BF16 模型（权重约 54GB）加上 KV Cache 和激活值，在 Batch=20 时可能超出 80GB 显存或接近极限，但主要错误在于 Prefill 吞吐量的推导逻辑不符合 LLM 推理的基本计算模型。 | 逻辑校验失败：Prefill 吞吐量公式量纲错误，将总 FLOPs 除以 (2*Params*SeqLen) 得到的数值无法直接解释为 tokens/s/请求，且数值量级与 A100 实际 Prefill 性能不符；Decode 阶段计算相对合理但受限于显存容量假设。
