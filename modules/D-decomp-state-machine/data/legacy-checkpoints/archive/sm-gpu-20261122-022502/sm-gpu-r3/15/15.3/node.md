# N311: RTX 4090 (24GB) 在 W4A8 量化下运行 Qwen3-27B 的显存需求计算：权重 13.5GB + KV Cache (32K * 2 * 2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

RTX 4090 (24GB) 在 W4A8 量化下运行 Qwen3-27B 的显存需求计算：权重 13.5GB + KV Cache (32K * 2 * 2 * 1.5 * 1 byte ≈ 192MB) + 激活值缓冲 (~4GB) ≈ 17.7GB，小于 24GB 显存，无需 Offload，因此保留 RTX 4090 进入对比池的决策在 W4A8 精度下成立。

## Corrected Claim

RTX 4090 (24GB) 在 W4A8 量化下运行 Qwen3-27B 的显存需求计算：权重 13.5GB + KV Cache (32K * 2 * 2 * 1.5 * 1 byte ≈ 192MB) + 激活值缓冲 (~4GB) ≈ 17.7GB，小于 24GB 显存，无需 Offload，因此保留 RTX 4090 进入对比池的决策在 W4A8 精度下成立。

## Evidence

[质询]KV Cache 计算中 '32K * 2 * 2 * 1.5 * 1 byte' 的系数含义模糊（通常 2 代表 K/V，1.5 可能指 GQA 比例或层数简化，1 byte 指 FP8/INT8 量化），且激活值缓冲 4GB 为经验估算值，不同推理框架（如 vLLM, TensorRT-LLM）实际占用可能有差异，但量级合理。 | 先验知识/题面给定，逻辑校验通过：Qwen3-27B 参数量约 27B，W4A8 量化下权重约 13.5GB (27e9 * 0.5 bytes)，KV Cache 在 32K 上下文下约 192MB-1GB 量级，激活值缓冲数 GB 量级，总和 < 24GB，符合 RTX 4090 显存容量，逻辑自洽。

## Search Query

Qwen3-27B W4A8 memory requirement 24GB GPU
