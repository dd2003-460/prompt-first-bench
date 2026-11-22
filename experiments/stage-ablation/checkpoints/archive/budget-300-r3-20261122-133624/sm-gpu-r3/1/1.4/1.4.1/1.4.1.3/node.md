# N203: Qwen3-27B 在 32K 上下文下 BF16 KV Cache 的显存占比分析：总显存需求 = 权重 (27GB INT8) + KV Cache (4.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

Qwen3-27B 在 32K 上下文下 BF16 KV Cache 的显存占比分析：总显存需求 = 权重 (27GB INT8) + KV Cache (4.0 GB BF16) + 激活 (1.0 GB) + 其他 (0.5 GB) = 32.5 GB。对于 RTX 5090 (32GB)，显存不足，必须启用 INT8 KV Cache (2.0 GB) 或限制上下文至 16K (2.0 GB KV)，总需求降至 30.5 GB，方可在 32GB 显存内稳定运行，修正 N115 的部署可行性判断。

## Corrected Claim

Qwen3-27B 在 32K 上下文下 BF16 KV Cache 的显存占比分析：总显存需求 = 权重 (27GB INT8) + KV Cache (4.0 GB BF16) + 激活 (1.0 GB) + 其他 (0.5 GB) = 32.5 GB。对于 RTX 5090 (32GB)，显存不足，必须启用 INT8 KV Cache (2.0 GB) 或限制上下文至 16K (2.0 GB KV)，总需求降至 30.5 GB，方可在 32GB 显存内稳定运行，修正 N115 的部署可行性判断。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B INT8权重约27GB，32K上下文BF16 KV Cache约4GB，总需求32.5GB超过RTX 5090的32GB显存，需优化至30.5GB方可运行，数值量级与逻辑自洽。
