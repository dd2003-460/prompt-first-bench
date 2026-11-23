# N75: RTX 4090 (24GB) 运行 Qwen3-27B BF16 所需的总显存占用（权重+KV Cache+激活值），计算公式：Weight_Size = 2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

RTX 4090 (24GB) 运行 Qwen3-27B BF16 所需的总显存占用（权重+KV Cache+激活值），计算公式：Weight_Size = 27B * 2 bytes, KV_Cache_Size = 2 * n_layers * n_heads * head_dim * seq_len * 2 bytes, 需验证是否溢出 24GB

## Corrected Claim

RTX 4090 (24GB) 运行 Qwen3-27B BF16 所需的总显存占用（权重+KV Cache+激活值），计算公式：Weight_Size = 27B * 2 bytes, KV_Cache_Size = 2 * n_layers * n_heads * head_dim * seq_len * 2 bytes, 需验证是否溢出 24GB

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存为 24GB，Qwen3-27B BF16 权重约 54GB，远超显存容量，必然溢出，公式量纲与数值量级合理。
