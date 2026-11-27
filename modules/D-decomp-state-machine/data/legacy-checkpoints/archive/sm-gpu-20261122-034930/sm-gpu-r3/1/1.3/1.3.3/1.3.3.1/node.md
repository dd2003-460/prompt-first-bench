# N177: 基于 N155 (vLLM/4090: 2.2GB) 和 N157 (vLLM/Act: 2.5GB)，在 RTX 4090 上使用 vLLM 运行 Qwen3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

基于 N155 (vLLM/4090: 2.2GB) 和 N157 (vLLM/Act: 2.5GB)，在 RTX 4090 上使用 vLLM 运行 Qwen3-27B INT8 时，非权重/KV 开销的保守预留值应修正为 4.7 GB，而非 N54 原建议的 4-6 GB 宽泛范围中的下限，这直接决定了单卡 24GB 显存是否足以容纳 27GB 权重（结论：不足，必须双卡或 Offload）。

## Corrected Claim

基于 N155 (vLLM/4090: 2.2GB) 和 N157 (vLLM/Act: 2.5GB)，在 RTX 4090 上使用 vLLM 运行 Qwen3-27B INT8 时，非权重/KV 开销的保守预留值应修正为 4.7 GB，而非 N54 原建议的 4-6 GB 宽泛范围中的下限，这直接决定了单卡 24GB 显存是否足以容纳 27GB 权重（结论：不足，必须双卡或 Offload）。

## Evidence

先验知识/题面给定，逻辑校验通过：2.2GB + 2.5GB = 4.7GB，且 27GB 权重 > 24GB 显存，结论自洽。
