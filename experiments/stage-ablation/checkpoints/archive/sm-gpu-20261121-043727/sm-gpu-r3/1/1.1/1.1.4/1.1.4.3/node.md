# N114: 修正 N43 中的公式参数代入错误：N43 假设 num_key_value_heads=8 导致高估 KV Cache 为 8.0 GB；根据 N107 确认

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42, N43, N44

## Claim

修正 N43 中的公式参数代入错误：N43 假设 num_key_value_heads=8 导致高估 KV Cache 为 8.0 GB；根据 N107 确认的 Qwen3-27B 实际配置 (num_kv_heads=4)，正确计算值应为 4.0 GB，该修正项使 RTX 4090 (24GB) 在 W4 量化下剩余可用显存从 8GB 增加至 12GB，显著改变最大并发 Batch Size 的估算上限

## Corrected Claim

修正 N43 中的公式参数代入错误：N43 假设 num_key_value_heads=8 导致高估 KV Cache 为 8.0 GB；根据 N107 确认的 Qwen3-27B 实际配置 (num_kv_heads=4)，正确计算值应为 4.0 GB，该修正项使 RTX 4090 (24GB) 在 W4 量化下剩余可用显存从 8GB 增加至 12GB，显著改变最大并发 Batch Size 的估算上限

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 大小与 num_kv_heads 成正比，从 8 头修正为 4 头，显存占用从 8.0GB 减半至 4.0GB，剩余显存从 8GB 增至 12GB，数学推导自洽。
