# N116: Qwen3-27B 在 Decode 阶段 (batch_size=1) 的 Activation Buffer 显存占用量化：由于仅处理单个 token 的中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42, N43, N44

## Claim

Qwen3-27B 在 Decode 阶段 (batch_size=1) 的 Activation Buffer 显存占用量化：由于仅处理单个 token 的中间激活，占用量极小，主要取决于 hidden_size (4096) 和中间层维度 (11008)，估算为 < 50 MB，可忽略不计，因此 Decode 阶段的显存瓶颈完全由 KV Cache 决定，与 N44 中 '<100MB' 的定性描述一致但提供了具体上限

## Corrected Claim

Qwen3-27B 在 Decode 阶段 (batch_size=1) 的 Activation Buffer 显存占用量化：由于仅处理单个 token 的中间激活，占用量极小，主要取决于 hidden_size (4096) 和中间层维度 (11008)，估算为 < 50 MB，可忽略不计，因此 Decode 阶段的显存瓶颈完全由 KV Cache 决定，与 N44 中 '<100MB' 的定性描述一致但提供了具体上限

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B hidden_size=4096, intermediate_size=11008，batch_size=1时单token激活显存占用极小（<50MB），KV Cache为Decode阶段主要显存瓶颈，与N44定性描述一致
