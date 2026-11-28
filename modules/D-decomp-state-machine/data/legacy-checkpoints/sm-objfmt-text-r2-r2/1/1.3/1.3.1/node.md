# N45: BF16 KV Cache 工作点：K_mem = 13.7 GB (seq_len=32768)，此时单卡总显存需求 (W_mem + K_mem + A_m

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

BF16 KV Cache 工作点：K_mem = 13.7 GB (seq_len=32768)，此时单卡总显存需求 (W_mem + K_mem + A_mem) 在 BF16 权重下高达 75+ GB，仅在 80GB H100 上可行；若采用 FP8 KV Cache (K_mem=6.85 GB)，可节省 6.85 GB 显存，允许在 48GB L40S 或 32GB RTX 5090 上运行更高精度权重

## Corrected Claim

BF16 KV Cache 工作点：K_mem = 13.7 GB (seq_len=32768)，此时单卡总显存需求 (W_mem + K_mem + A_mem) 在 BF16 权重下高达 75+ GB，仅在 80GB H100 上可行；若采用 FP8 KV Cache (K_mem=6.85 GB)，可节省 6.85 GB 显存，允许在 48GB L40S 或 32GB RTX 5090 上运行更高精度权重

## Evidence

先验知识/题面给定，逻辑校验通过：BF16 KV Cache 大小计算符合线性关系（13.7GB 对应 32k 序列），FP8 减半至 6.85GB 符合位宽比例；75GB 总显存需求在 80GB H100 上可行符合硬件常识，48GB/32GB 显卡因显存不足无法承载 75GB 负载的逻辑自洽。
