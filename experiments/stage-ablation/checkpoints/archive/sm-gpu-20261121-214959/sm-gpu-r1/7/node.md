# N32: RTX 4090 (24GB) 单卡在 32K 上下文下的最大可行精度验证：INT4 权重 (13.5GB) + BF16 KV Cache (12.58GB)

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

RTX 4090 (24GB) 单卡在 32K 上下文下的最大可行精度验证：INT4 权重 (13.5GB) + BF16 KV Cache (12.58GB) = 26.08GB > 24GB (溢出)；INT4 权重 (13.5GB) + FP8 KV Cache (6.29GB) = 19.79GB < 24GB (可行，剩余 ~4.2GB 用于激活值/临时缓冲)。结论：单卡 4090 必须同时使用 INT4 权重和 FP8 KV Cache 才能满足 32K 容量下限。

## Corrected Claim

RTX 4090 (24GB) 单卡在 32K 上下文下的最大可行精度验证：INT4 权重 (13.5GB) + BF16 KV Cache (12.58GB) = 26.08GB > 24GB (溢出)；INT4 权重 (13.5GB) + FP8 KV Cache (6.29GB) = 19.79GB < 24GB (可行，剩余 ~4.2GB 用于激活值/临时缓冲)。结论：单卡 4090 必须同时使用 INT4 权重和 FP8 KV Cache 才能满足 32K 容量下限。

## Evidence

检索失败: no sources from any channel (all 5 failed)
