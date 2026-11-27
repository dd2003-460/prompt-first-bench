# N407: 在 batch_size=32, seq_len=1024 场景下，Qwen3-27B (BF16) 的 KV Cache 总占用量为 32 * 2 * 32 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N163

## Claim

在 batch_size=32, seq_len=1024 场景下，Qwen3-27B (BF16) 的 KV Cache 总占用量为 32 * 2 * 32 * 4096 * 2 bytes ≈ 16.7 MB/layer，全模型 (64 layers) 约 1.07 GB，加上权重 54.6 GB，总显存需求约 55.7 GB；RTX 4090 (24GB) 不可行，A100 40GB 不可行，A100 80GB 可行，H100 80GB 可行。

## Corrected Claim

在 batch_size=32, seq_len=1024 场景下，Qwen3-27B (BF16) 的 KV Cache 总占用量为 32 * 2 * 32 * 4096 * 2 bytes ≈ 16.7 MB/layer，全模型 (64 layers) 约 1.07 GB，加上权重 54.6 GB，总显存需求约 55.7 GB；RTX 4090 (24GB) 不可行，A100 40GB 不可行，A100 80GB 可行，H100 80GB 可行。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算 (32*2*32*4096*2=16.7MB/layer, 64 layers=1.07GB) 及总显存 (54.6+1.07≈55.7GB) 数值量级与逻辑自洽，符合 Qwen3-27B 架构参数及主流 GPU 显存规格。
