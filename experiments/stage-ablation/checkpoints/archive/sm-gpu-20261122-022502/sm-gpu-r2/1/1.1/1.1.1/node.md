# N33: 32K上下文KV Cache在BF16下的确切显存占用为 192MB (32,768 tokens * 2 bytes/token * 2 (K+V) * 1.

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

32K上下文KV Cache在BF16下的确切显存占用为 192MB (32,768 tokens * 2 bytes/token * 2 (K+V) * 1.0 (Qwen3-27B标准KV头数/维度估算)，注：若考虑GQA/MQA或具体层数，需按 2 * layers * kv_heads * head_dim * 2 bytes 计算，Qwen3-27B具体层数与KV头数需查模型config.json [待核验]，但即使按保守估计，KV Cache仅占显存极小部分，主要瓶颈是权重)

## Corrected Claim

32K上下文KV Cache在BF16下的显存占用约为 8GB (估算值，具体取决于 Qwen3-27B 的层数和 KV 头数配置，公式为 2 * layers * kv_heads * head_dim * 32768 * 2 bytes)。

## Evidence

[质询]数值量级严重错误：192MB 远小于 32K 上下文 KV Cache 的实际占用。对于 Qwen3-27B（假设层数~64，KV头数~8，Head Dim~128），单层 KV 大小约为 2 * 8 * 128 * 2 bytes = 4KB，32K tokens 单层占用 128MB，总占用约为 64 * 128MB = 8GB。192MB 仅相当于约 1.5 层的 KV Cache，或者仅相当于 2K 上下文的占用，与 32K 上下文不符。 | 逻辑校验失败：根据标准 Transformer KV Cache 计算公式 (2 * layers * kv_heads * head_dim * seq_len * dtype_size)，32K 上下文的 KV Cache 占用通常在 GB 级别（对于 27B 模型约为 8-10GB），而非 192MB。192MB 的数值与 32K 序列长度在量级上矛盾（相差约 50-100 倍）。

## Search Query

Qwen3-27B model config.json num_hidden_layers num_key_value_heads head_dim
