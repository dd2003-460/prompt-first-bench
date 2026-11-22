# N319: RTX 4090 在 INT8 量化下运行 Qwen3-27B 的显存不可行证明：权重 27GB > 24GB 单卡显存上限，即使 KV Cache 为 0 且

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

RTX 4090 在 INT8 量化下运行 Qwen3-27B 的显存不可行证明：权重 27GB > 24GB 单卡显存上限，即使 KV Cache 为 0 且无框架开销，权重本身已超出 3GB，因此单卡 RTX 4090 在 INT8 下物理不可行，必须双卡或换卡。

## Corrected Claim

RTX 4090 在 INT8 量化下运行 Qwen3-27B 的显存不可行证明：权重 27GB > 24GB 单卡显存上限，即使 KV Cache 为 0 且无框架开销，权重本身已超出 3GB，因此单卡 RTX 4090 在 INT8 下物理不可行，必须双卡或换卡。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，INT8量化下权重体积约为27GB，超过RTX 4090的24GB显存上限，物理上不可行。
