# N8: Qwen3.8-27B采用GQA架构(KV heads=8, head_dim=128)，单token KV Cache大小 = 2 * 8 * 128 * 2

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3.8-27B采用GQA架构(KV heads=8, head_dim=128)，单token KV Cache大小 = 2 * 8 * 128 * 2 bytes (fp8) = 4KB/token

## Corrected Claim

Qwen3.8-27B采用GQA架构(KV heads=8, head_dim=128)，单token KV Cache大小 = 2 * 8 * 128 * 2 bytes (fp8) = 4KB/token

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 744)
