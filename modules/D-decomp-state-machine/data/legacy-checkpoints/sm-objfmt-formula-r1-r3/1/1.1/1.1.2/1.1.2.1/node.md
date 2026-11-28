# N127: RTX 5090 单卡在 32GB 显存限制下运行 Qwen3-27B 的可行性边界：采用 NVFP4 量化（权重 13.5GB + 缩放 1.8GB + KV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

RTX 5090 单卡在 32GB 显存限制下运行 Qwen3-27B 的可行性边界：采用 NVFP4 量化（权重 13.5GB + 缩放 1.8GB + KV Cache 4.096GB + 开销 1.5GB ≈ 20.9GB）时，剩余显存约 11.1GB，足以支持 32K 上下文的完整 Prefill 和 Decode 过程；若采用 FP8 量化（权重 27GB + KV 4.096GB + 开销 1.5GB ≈ 32.6GB），则超出 32GB 显存上限约 0.6GB，因此 RTX 5090 单卡仅能支持 NVFP4 或 INT8 (W8A16, 权重 27GB + KV 2.048GB + 开销 1.5GB ≈ 30.5GB) 方案，无法原生运行 FP8 全精度 KV 缓存。

## Corrected Claim

RTX 5090 单卡在 32GB 显存限制下运行 Qwen3-27B 的可行性边界：采用 NVFP4 量化（权重 13.5GB + 缩放 1.8GB + KV Cache 4.096GB + 开销 1.5GB ≈ 20.9GB）时，剩余显存约 11.1GB，足以支持 32K 上下文的完整 Prefill 和 Decode 过程；若采用 FP8 量化（权重 27GB + KV 4.096GB + 开销 1.5GB ≈ 32.6GB），则超出 32GB 显存上限约 0.6GB，因此 RTX 5090 单卡仅能支持 NVFP4 或 INT8 (W8A16, 权重 27GB + KV 2.048GB + 开销 1.5GB ≈ 30.5GB) 方案，无法原生运行 FP8 全精度 KV 缓存。

## Evidence

[质询]NVFP4 量化后权重体积估算可能存在偏差（通常 4-bit 量化含缩放因子约为 0.5-0.6 bytes/param，27B 模型权重可能在 13.5GB-16GB 之间，此处取 13.5GB 偏乐观但仍在合理工程估算范围内）；此外，32K 上下文的 KV Cache 大小高度依赖 Batch Size 和具体实现（如 PagedAttention 的块大小），4.096GB 是一个特定配置下的经验值而非绝对物理极限，但在单卡推理的典型小 Batch 场景下量级合理。 | 先验知识/题面给定，逻辑校验通过：RTX 5090 显存为 32GB，NVFP4 方案总占用约 20.9GB < 32GB，FP8 方案总占用约 32.6GB > 32GB，INT8 方案总占用约 30.5GB < 32GB，数值加减法及显存容量对比逻辑自洽，符合大模型部署的基本显存预算原则。
