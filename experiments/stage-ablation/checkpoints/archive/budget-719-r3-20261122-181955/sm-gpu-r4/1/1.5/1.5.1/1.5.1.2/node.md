# N198: Apple M2 Ultra (192GB) 在 Qwen3-27B BF16 下的理论 Decode 上限计算：Throughput_decode = (Ef

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N61

## Claim

Apple M2 Ultra (192GB) 在 Qwen3-27B BF16 下的理论 Decode 上限计算：Throughput_decode = (Effective_Bandwidth * Efficiency_Factor) / (Weights_Size + KV_Cache_Size_per_token * Batch_Size)。假设 Effective_Bandwidth = 800 * 0.85 = 680 GB/s，Weights = 54 GB，KV_Cache per token (BF16, 32K ctx) 需基于 N114 确认的架构参数计算。

## Corrected Claim

Apple M2 Ultra (192GB) 在 Qwen3-27B BF16 下的理论 Decode 上限计算：Throughput_decode = (Effective_Bandwidth * Efficiency_Factor) / (Weights_Size + KV_Cache_Size_per_token * Batch_Size)。假设 Effective_Bandwidth = 800 * 0.85 = 680 GB/s，Weights = 54 GB，KV_Cache per token (BF16, 32K ctx) 需基于 N114 确认的架构参数计算。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 758)
