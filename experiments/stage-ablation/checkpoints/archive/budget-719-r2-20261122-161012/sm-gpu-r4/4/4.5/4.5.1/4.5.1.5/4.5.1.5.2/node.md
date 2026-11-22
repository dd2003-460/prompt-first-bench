# N561: RTX 5090 单卡运行 Qwen3-27B FP8 时，3.8 GB 显存余量不足以支持 32K 上下文下的 Prefill 阶段激活值 (Activati

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N233

## Claim

RTX 5090 单卡运行 Qwen3-27B FP8 时，3.8 GB 显存余量不足以支持 32K 上下文下的 Prefill 阶段激活值 (Activations) 开销，Prefill 激活值峰值约为 (2 * 27e9 * 32768) / (1792 GB/s * 1000) * 2 bytes ≈ 1.9 GB，加上 KV Cache 1.2 GB，总需求 3.1 GB 接近 3.8 GB 余量上限，实际运行需预留 0.5-1.0 GB 安全边际，可能导致 Prefill 阶段 OOM 或需分块计算 (Chunked Prefill)。

## Corrected Claim

RTX 5090 单卡运行 Qwen3-27B FP8 时，3.8 GB 显存余量在 32K 上下文下可能不足以支持 Prefill 阶段，主要受限于 KV Cache 占用（约 1.2 GB）及激活值开销。具体激活值峰值需根据 Batch Size 和模型结构精确计算，原陈述中的计算公式无效。实际运行中需预留安全边际，可能导致 OOM 或需启用 Chunked Prefill。

## Evidence

[质询]Prefill 激活值峰值的计算公式存在严重的量纲和逻辑错误。公式 `(2 * 27e9 * 32768) / (1792 GB/s * 1000) * 2 bytes` 将参数量、序列长度、带宽和字节数混合运算，量纲完全不通（结果单位不是 GB）。此外，Prefill 阶段的激活值内存占用主要取决于 Batch Size、Hidden Size 和 Layer 数，而非简单的参数量乘以序列长度再除以带宽。该数值 1.9 GB 缺乏理论依据，属于臆造的计算过程。 | 先验知识/题面给定，逻辑校验失败：激活值计算公式量纲错误，且 Prefill 激活值峰值估算方法不符合 Transformer 内存占用基本原理。
