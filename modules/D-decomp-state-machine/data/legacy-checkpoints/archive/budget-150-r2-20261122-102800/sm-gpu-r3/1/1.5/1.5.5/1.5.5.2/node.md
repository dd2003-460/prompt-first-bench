# N207: RTX 3090 24GB 在 BF16 精度下的理论 Decode 吞吐 ≈ 936 GB/s / (27B * 2 bytes) ≈ 17.3 tokens

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

RTX 3090 24GB 在 BF16 精度下的理论 Decode 吞吐 ≈ 936 GB/s / (27B * 2 bytes) ≈ 17.3 tokens/s，与 RTX 4090 相当，但显存仅 24GB。Qwen3-27B BF16 权重需 ~54GB，远超 24GB 显存，因此 RTX 3090 单卡无法运行 BF16 Qwen3-27B。必须使用 W4 量化 (≈13.5GB 权重 + KV Cache)，或双卡 3090 (TP=2, 48GB 总显存)。双卡 3090 硬件成本 ≈ $1,800-$2,200，是极低成本的 BF16/INT8 可行方案 (若双卡显存足够容纳权重+KV)。

## Corrected Claim

RTX 3090 24GB 在 BF16 精度下的理论 Decode 吞吐 ≈ 936 GB/s / (27B * 2 bytes) ≈ 17.3 tokens/s，与 RTX 4090 相当，但显存仅 24GB。Qwen3-27B BF16 权重需 ~54GB，远超 24GB 显存，因此 RTX 3090 单卡无法运行 BF16 Qwen3-27B。必须使用 W4 量化 (≈13.5GB 权重 + KV Cache)，或双卡 3090 (TP=2, 48GB 总显存)。双卡 3090 硬件成本 ≈ $1,800-$2,200，是极低成本的 BF16/INT8 可行方案 (若双卡显存足够容纳权重+KV)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090显存带宽936GB/s与24GB容量、Qwen3-27B BF16权重约54GB、W4量化约13.5GB及双卡成本估算均符合硬件规格与算术逻辑。

## Search Query

RTX 3090 24GB Qwen3-27B inference quantization requirement
