# N87: Qwen3-27B 模型在 BF16 精度下，若采用 KV Cache 量化至 FP8，KV Cache 显存占用减半至 13.82 GB，总显存需求降至 67

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

Qwen3-27B 模型在 BF16 精度下，若采用 KV Cache 量化至 FP8，KV Cache 显存占用减半至 13.82 GB，总显存需求降至 67.82 GB，仍超出 RTX 4090 24GB 显存，需多卡或 offload [已验证]。

## Corrected Claim

Qwen3-27B 模型在 BF16 精度下，若采用 KV Cache 量化至 FP8，KV Cache 显存占用减半至 13.82 GB，总显存需求降至 67.82 GB，仍超出 RTX 4090 24GB 显存，需多卡或 offload [已验证]。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，KV Cache FP8量化后13.82GB，总和67.82GB，远超24GB显存，结论符合物理限制。
