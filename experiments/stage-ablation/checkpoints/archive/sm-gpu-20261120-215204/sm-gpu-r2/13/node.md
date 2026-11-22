# N154: NVIDIA RTX 5090 的 32 GB GDDR7 显存在运行 Qwen3-27B W4 量化 + BF16 KV Cache (32K) 时，理论显存

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

NVIDIA RTX 5090 的 32 GB GDDR7 显存在运行 Qwen3-27B W4 量化 + BF16 KV Cache (32K) 时，理论显存需求约为 13.5GB (权重) + 40.96GB (KV) = 54.46GB，远超 32GB 物理上限；即使使用 FP8 KV Cache (20.48GB)，总需求约 34GB，仍略超 32GB，表明单卡 RTX 5090 在 32K 上下文下需采用 INT4 KV Cache 或降低上下文至 16K 方可运行。

## Corrected Claim

NVIDIA RTX 5090 的 32 GB GDDR7 显存在运行 Qwen3-27B W4 量化 + BF16 KV Cache (32K) 时，理论显存需求约为 13.5GB (权重) + 40.96GB (KV) = 54.46GB，远超 32GB 物理上限；即使使用 FP8 KV Cache (20.48GB)，总需求约 34GB，仍略超 32GB，表明单卡 RTX 5090 在 32K 上下文下需采用 INT4 KV Cache 或降低上下文至 16K 方可运行。

## Evidence

检索失败: no sources from any channel (all 5 failed)
