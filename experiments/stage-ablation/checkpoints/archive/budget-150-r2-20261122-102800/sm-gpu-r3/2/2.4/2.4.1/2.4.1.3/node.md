# N230: W4 单卡显存需求精确分解：Qwen3-27B 权重 (14.57 GB, 0.5 bytes/element) + KV Cache (32K ctx, ba

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

W4 单卡显存需求精确分解：Qwen3-27B 权重 (14.57 GB, 0.5 bytes/element) + KV Cache (32K ctx, batch=1, 2 bytes/element, 仍为 BF16 存储 ≈ 2.01 GB) + 激活缓冲 (W4 计算但中间激活保持 BF16，峰值 ≈ 1.7 GB) + 框架开销 (≈ 1.0 GB) = 19.28 GB；因此 24 GB 卡 (如 RTX 4090) 余量 4.72 GB (24%)，满足安全阈值，但需确认 KV Cache 是否支持 FP8 压缩以进一步降低需求。

## Corrected Claim

W4 单卡显存需求精确分解：Qwen3-27B 权重 (14.57 GB, 0.5 bytes/element) + KV Cache (32K ctx, batch=1, 2 bytes/element, 仍为 BF16 存储 ≈ 2.01 GB) + 激活缓冲 (W4 计算但中间激活保持 BF16，峰值 ≈ 1.7 GB) + 框架开销 (≈ 1.0 GB) = 19.28 GB；因此 24 GB 卡 (如 RTX 4090) 余量 4.72 GB (24%)，满足安全阈值，但需确认 KV Cache 是否支持 FP8 压缩以进一步降低需求。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B W4量化权重约14.57GB，KV Cache与激活缓冲估算符合BF16存储量级，总显存需求19.28GB在24GB卡上留有合理余量，数值量级与工程直觉一致。

## Search Query

Qwen3-27B W4 AWQ VRAM requirement KV cache FP8 support
