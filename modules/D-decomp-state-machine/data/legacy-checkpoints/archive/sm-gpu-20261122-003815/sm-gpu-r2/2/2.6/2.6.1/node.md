# N102: 2x RTX 4090 (48GB) 运行 FP8 Qwen3-27B 的显存分布：总显存 48 GB。FP8 权重 27 GB。若采用 Tensor Para

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

2x RTX 4090 (48GB) 运行 FP8 Qwen3-27B 的显存分布：总显存 48 GB。FP8 权重 27 GB。若采用 Tensor Parallelism (TP=2)，每卡承载 13.5 GB 权重。KV Cache 需分片或复制。若 KV Cache 总量 8.6 GB (BF16, 32K)，每卡 4.3 GB。每卡总占用 ≈ 13.5 + 4.3 + 1 (Act) + 1 (Runtime) = 19.8 GB < 24 GB，可行。

## Corrected Claim

2x RTX 4090 (48GB) 运行 FP8 Qwen3-27B 的显存分布：总显存 48 GB。FP8 权重 27 GB。若采用 Tensor Parallelism (TP=2)，每卡承载 13.5 GB 权重。KV Cache 需分片或复制。若 KV Cache 总量 8.6 GB (BF16, 32K)，每卡 4.3 GB。每卡总占用 ≈ 13.5 + 4.3 + 1 (Act) + 1 (Runtime) = 19.8 GB < 24 GB，可行。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数FP8权重约27GB，TP=2分片后每卡13.5GB；32K上下文BF16 KV Cache约8.6GB，分片后每卡4.3GB；加上激活和运行时开销，每卡总占用约19.8GB，小于24GB显存限制，计算逻辑自洽且量级合理。
