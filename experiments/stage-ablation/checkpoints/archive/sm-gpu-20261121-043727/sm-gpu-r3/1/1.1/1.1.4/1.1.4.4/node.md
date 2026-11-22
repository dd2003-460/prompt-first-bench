# N115: Qwen3-27B 在 Prefill 阶段 (seq_len=32K, batch_size=1) 的 Activation Buffer 峰值显存占用量化：

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42, N43, N44

## Claim

Qwen3-27B 在 Prefill 阶段 (seq_len=32K, batch_size=1) 的 Activation Buffer 峰值显存占用量化：基于 Transformer 中间层激活值公式 (hidden_size * seq_len * num_intermediate_dims * precision_bytes)，结合 FlashAttention-2 优化后仅存储注意力分数块而非完整矩阵，估算峰值激活值占用约为 1.5 - 2.5 GB，该数值需从总显存中扣除以计算最大 KV Cache 容量

## Corrected Claim

Qwen3-27B 在 Prefill 阶段 (seq_len=32K, batch_size=1) 的 Activation Buffer 峰值显存占用受 FlashAttention-2 及 FFN 中间层优化策略影响显著，具体数值需根据实际推理框架（如 vLLM, Ollama）的内存管理策略确定，简单公式估算可能低估 FFN 中间激活值占用。

## Evidence

[质询]数值估算缺乏严谨推导且可能低估：Qwen3-27B 的 hidden_size 约为 5120，intermediate_size 约为 27648。在 seq_len=32K 时，仅 FFN 层（SwiGLU 结构，通常有 3 个投影矩阵）的激活值峰值（若未完全融合或中间层未优化）可能远超 2.5GB（例如 5120 * 32768 * 27648 * 2 bytes * 3 ≈ 27GB，即使 FlashAttention 优化了 Attention 部分，FFN 的中间激活值仍是主要瓶颈，除非使用了极端的 offloading 或分块计算，否则 1.5-2.5GB 的峰值估计过于乐观，且未明确说明是否包含 FFN 中间层激活）。 | 来源 [1] 仅提供了 Qwen3-27B 在 4090 24GB 显卡上运行 256K 上下文的实测背景，未提供具体的 Activation Buffer 峰值显存数值或计算公式，无法直接支持 1.5-2.5GB 的具体量化结论；该数值属于经验事实/工程估算，逻辑上虽自洽（作为估算值），但缺乏来源直接支持且存在低估风险，故降级。

## Search Query

Qwen3-27B prefill activation memory usage flash attention 32k context

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2077357481093763492&rut=8cceee022cc23b803b3799e1d54d538f8ecc6d81494ca0e0961c57ebc3a3c19f', 'type': 'ddg', 'title': '我用自测工具把本地 27B 大模型榨了一遍：prefill、decode、前缀缓存，答案都在表里'}
