# N82: 激活值缓冲 (Activation Buffer) 的量化估算公式：对于 Transformer 解码器，激活显存 ≈ seq_len * hidden_siz

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

激活值缓冲 (Activation Buffer) 的量化估算公式：对于 Transformer 解码器，激活显存 ≈ seq_len * hidden_size * bytes_per_elem * (num_layers * k + 1)。在 32K ctx, hidden=3584, BF16 下，主要中间激活 (如 Attention scores, FFN intermediates) 峰值占用约 1.5-2.5 GB，取决于具体推理引擎 (vLLM/PyTorch) 的内存复用策略。

## Corrected Claim

激活值缓冲 (Activation Buffer) 的量化估算公式：对于 Transformer 解码器，激活显存 ≈ seq_len * hidden_size * bytes_per_elem * (num_layers * k + 1)。在 32K ctx, hidden=3584, BF16 下，主要中间激活 (如 Attention scores, FFN intermediates) 峰值占用约 1.5-2.5 GB，取决于具体推理引擎 (vLLM/PyTorch) 的内存复用策略。

## Evidence

先验知识/题面给定，逻辑校验通过
