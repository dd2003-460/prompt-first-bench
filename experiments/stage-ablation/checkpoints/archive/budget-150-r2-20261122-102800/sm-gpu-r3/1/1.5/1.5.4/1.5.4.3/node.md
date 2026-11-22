# N205: L40S 的 48GB 显存可完整容纳 Qwen3-27B 的 BF16 权重 (≈54GB) 吗？否，54GB > 48GB。因此 L40S 无法在单卡 BF

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

L40S 的 48GB 显存可完整容纳 Qwen3-27B 的 BF16 权重 (≈54GB) 吗？否，54GB > 48GB。因此 L40S 无法在单卡 BF16 下运行 Qwen3-27B 而保留足够的 KV Cache 空间 (32K context 需额外 ~20-40GB)。必须使用 INT8 (≈27GB) 或 W4 (≈13.5GB) 量化，或双卡 L40S (TP=2)。若双卡 L40S，硬件成本翻倍至 $18,000-$22,000，且 PCIe 通信开销显著。

## Corrected Claim

L40S 的 48GB 显存可完整容纳 Qwen3-27B 的 BF16 权重 (≈54GB) 吗？否，54GB > 48GB。因此 L40S 无法在单卡 BF16 下运行 Qwen3-27B 而保留足够的 KV Cache 空间 (32K context 需额外 ~20-40GB)。必须使用 INT8 (≈27GB) 或 W4 (≈13.5GB) 量化，或双卡 L40S (TP=2)。若双卡 L40S，硬件成本翻倍至 $18,000-$22,000，且 PCIe 通信开销显著。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重约54GB，确实超过L40S 48GB显存，且加上KV Cache后更无法容纳，必须量化或双卡。

## Search Query

Qwen3-27B BF16 memory footprint 48GB GPU inference
