# N8: INT8/W8A8量化下的显存总需求 = 模型权重(27B * 1 byte = 27GB) + KV Cache(32K tokens * 2 * 27B /

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

INT8/W8A8量化下的显存总需求 = 模型权重(27B * 1 byte = 27GB) + KV Cache(32K tokens * 2 * 27B / 27B_hidden_dim * 2 bytes ≈ 2.0GB) + 激活值(1-2GB) + 校准常数(0.5GB) ≈ 30.5-31.5GB

## Corrected Claim

INT8/W8A8量化下的显存总需求 = 模型权重(27GB) + KV Cache(需根据具体模型层数、KV头数及序列长度重新计算，32K tokens 下通常显著高于 2GB) + 激活值(1-2GB) + 校准常数(0.5GB)。

## Evidence

[质询]KV Cache 计算公式存在严重的逻辑与量纲错误：'32K tokens * 2 * 27B / 27B_hidden_dim * 2 bytes' 中，分子分母同时出现 27B（总参数量）和 hidden_dim（隐藏层维度），且未明确层数（layers）。对于 27B 模型（如 Llama-3-70B 或类似架构），KV Cache 大小通常由 `2 * layers * num_kv_heads * head_dim * seq_len * dtype_size` 决定。若按常规 27B 模型（约 40-60 层，GQA 或 MHA），32K 上下文的 KV Cache 往往远超 2GB（例如 Llama-3-70B 在 32K 下 KV Cache 约为 10-20GB 量级，取决于具体配置；即使是较小的 27B 模型，32K 的 KV Cache 也通常在数 GB 到十几 GB 之间，2GB 的估算极可能偏低或基于错误的简化假设）。此外，'27B / 27B_hidden_dim' 这一项在物理意义上不明确，疑似混淆了参数量与维度。 | 先验知识/题面给定，但逻辑校验发现 KV Cache 估算公式存在量纲/逻辑错误，导致数值量级可能严重失真，无法确认为 verified。

## Search Query

Qwen3-27B INT8 quantization memory footprint
