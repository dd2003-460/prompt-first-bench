# N155: 针对 27B 模型的长上下文科研任务，采用 Sliding Window Attention (SWA) 或 StreamingLLM 策略将 KV Cache

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

针对 27B 模型的长上下文科研任务，采用 Sliding Window Attention (SWA) 或 StreamingLLM 策略将 KV Cache 限制在最近 4k-8k tokens，可将单序列 KV 显存占用从 262k*64KB=16GB 降至 8k*64KB=512MB，使 TP=4 单卡剩余显存 (13.76GB) 支持并发序列数从 0.82 提升至 ~26，显著提升系统吞吐量。

## Corrected Claim

针对 27B 模型的长上下文科研任务，采用 Sliding Window Attention (SWA) 或 StreamingLLM 策略将 KV Cache 限制在最近 4k-8k tokens，可将单序列 KV 显存占用从 262k*64KB=16GB 降至 8k*64KB=512MB，使 TP=4 单卡剩余显存 (13.76GB) 支持并发序列数从 0.82 提升至 ~26，显著提升系统吞吐量。

## Evidence

检索失败: no sources from any channel (all 5 failed)
