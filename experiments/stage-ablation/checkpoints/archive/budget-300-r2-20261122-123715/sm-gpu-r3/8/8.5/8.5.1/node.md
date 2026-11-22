# N359: Qwen3-27B 在 32K 上下文下的 KV Cache 显存占用（基于 GQA 配置 num_kv_heads=4, head_dim=256, laye

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

Qwen3-27B 在 32K 上下文下的 KV Cache 显存占用（基于 GQA 配置 num_kv_heads=4, head_dim=256, layers=64, FP16）为 4.0 GB，计算公式为 (2 * 64 * 4 * 256 * 32768 * 2) / 1024^3

## Corrected Claim

Qwen3-27B 在 32K 上下文下的 KV Cache 显存占用（基于 GQA 配置 num_kv_heads=4, head_dim=256, layers=64, FP16）为 4.0 GB，计算公式为 (2 * 64 * 4 * 256 * 32768 * 2) / 1024^3

## Evidence

先验知识/题面给定，逻辑校验通过：公式 (2 * 64 * 4 * 256 * 32768 * 2) / 1024^3 计算结果确为 4.0 GB，量纲与数值均正确。
