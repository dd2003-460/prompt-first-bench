# N476: KV Cache 单 token 大小（BF16）的精确计算值为 128 KB/token，公式为 2 (K+V) * 64 (layers) * 8 (kv_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N197

## Claim

KV Cache 单 token 大小（BF16）的精确计算值为 128 KB/token，公式为 2 (K+V) * 64 (layers) * 8 (kv_heads) * 128 (head_dim) * 2 (bytes/BF16) = 131,072 bytes = 128 KB；N197 中声称的 256 KB/token 存在计算错误（可能误将 head_dim 或 kv_heads 加倍，或混淆了 Q/KV 维度），此错误会导致后续显存估算偏差 100%。

## Corrected Claim

KV Cache 单 token 大小（BF16）的精确计算值为 128 KB/token，公式为 2 (K+V) * 64 (layers) * 8 (kv_heads) * 128 (head_dim) * 2 (bytes/BF16) = 131,072 bytes = 128 KB；N197 中声称的 256 KB/token 存在计算错误（可能误将 head_dim 或 kv_heads 加倍，或混淆了 Q/KV 维度），此错误会导致后续显存估算偏差 100%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 64 * 8 * 128 * 2 = 131,072 bytes = 128 KB 计算正确，且符合 BF16 下 KV Cache 的标准计算逻辑。
