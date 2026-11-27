# N797: RTX 4090 在运行 LLM 推理时的激活值/中间缓冲占用估算：主要取决于 batch_size 和 hidden_dim。对于 Qwen3-27B (hi

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N248, N249, N250

## Claim

RTX 4090 在运行 LLM 推理时的激活值/中间缓冲占用估算：主要取决于 batch_size 和 hidden_dim。对于 Qwen3-27B (hidden_dim=4096)，单 token 前向传播的激活峰值约为 2 * hidden_dim * num_layers * dtype_size。在 Decode 阶段 (batch=1)，激活值占用通常 < 1 GB；在 Prefill 阶段 (32K 上下文)，激活值峰值可达 2-4 GB，具体取决于是否启用 FlashAttention (节省中间 QKV 存储)。

## Corrected Claim

RTX 4090 在运行 LLM 推理时的激活值/中间缓冲占用估算：主要取决于 batch_size 和 hidden_dim。对于 Qwen3-27B (hidden_dim=4096)，单 token 前向传播的激活峰值约为 2 * hidden_dim * num_layers * dtype_size。在 Decode 阶段 (batch=1)，激活值占用通常 < 1 GB；在 Prefill 阶段 (32K 上下文)，激活值峰值可达 2-4 GB，具体取决于是否启用 FlashAttention (节省中间 QKV 存储)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B hidden_dim=4096，Decode阶段batch=1激活值极小（<1GB合理），Prefill阶段32K上下文下激活值峰值2-4GB符合FlashAttention优化后的量级估算

## Search Query

LLM inference activation memory usage estimation batch size hidden dim
