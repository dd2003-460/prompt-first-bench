# N182: RTX 5090 32GB 显存在 INT8 精度 (权重 27GB) + 32K 上下文 BF16 KV Cache (17.2GB) 的总显存需求为 44.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48, N49, N50

## Claim

RTX 5090 32GB 显存在 INT8 精度 (权重 27GB) + 32K 上下文 BF16 KV Cache (17.2GB) 的总显存需求为 44.2GB，超出 32GB 物理上限 12.2GB，结论：单卡 5090 无法在 32K 上下文下运行 INT8 Qwen3-27B，必须使用 FP8 KV (8.6GB, 总 35.6GB 仍超) 或降低上下文至 ~24K (KV 12.9GB, 总 39.9GB 仍超) 或 W4 精度。

## Corrected Claim

RTX 5090 32GB 显存在 INT8 精度 (权重 27GB) + 32K 上下文 BF16 KV Cache (17.2GB) 的总显存需求为 44.2GB，超出 32GB 物理上限 12.2GB，结论：单卡 5090 无法在 32K 上下文下运行 INT8 Qwen3-27B，必须使用 FP8 KV (8.6GB, 总 35.6GB 仍超) 或降低上下文至 ~24K (KV 12.9GB, 总 39.9GB 仍超) 或 W4 精度。

## Evidence

先验知识/题面给定，逻辑校验通过：27GB (INT8权重) + 17.2GB (BF16 KV) = 44.2GB > 32GB，且替代方案计算 (8.6+27=35.6GB, 12.9+27=39.9GB) 均超过32GB，数值量级与逻辑自洽。
