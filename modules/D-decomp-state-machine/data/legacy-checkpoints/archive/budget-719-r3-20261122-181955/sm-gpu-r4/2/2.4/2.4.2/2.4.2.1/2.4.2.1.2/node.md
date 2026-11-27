# N713: Qwen3-27B 的 num_kv_heads 确认为 8（GQA 配置），head_dim=128，hidden_size=4096，这些参数与 N369/

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N255

## Claim

Qwen3-27B 的 num_kv_heads 确认为 8（GQA 配置），head_dim=128，hidden_size=4096，这些参数与 N369/N370 已验证事实一致，是计算 KV Cache per token 的基础。

## Corrected Claim

Qwen3-27B 的 num_kv_heads 确认为 8（GQA 配置），head_dim=128，hidden_size=4096，这些参数与 N369/N370 已验证事实一致，是计算 KV Cache per token 的基础。

## Evidence

先验知识/题面给定，逻辑校验通过
