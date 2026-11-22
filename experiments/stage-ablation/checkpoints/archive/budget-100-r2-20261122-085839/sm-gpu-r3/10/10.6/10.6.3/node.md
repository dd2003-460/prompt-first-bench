# N324: RTX 4090 24GB 在 BF16 下无法运行 Qwen3-27B (需 54.2GB 权重)，故在 BF16 分支中，消费级卡不可行；若对比 W4 量化

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

RTX 4090 24GB 在 BF16 下无法运行 Qwen3-27B (需 54.2GB 权重)，故在 BF16 分支中，消费级卡不可行；若对比 W4 量化，4090 带宽 1008GB/s，Bytes_per_token = 13.55GB，理论吞吐 = (1008 * 0.6~0.85) / 13.55 * 1000 ≈ 44,600 - 62,700 tokens/s，高于 A100 BF16 下限但低于 H100 BF16 上限

## Corrected Claim

RTX 4090 24GB 在 BF16 下无法运行 Qwen3-27B (需 54.2GB 权重)，故在 BF16 分支中，消费级卡不可行；若对比 W4 量化，4090 带宽 1008GB/s，Bytes_per_token = 13.55GB，理论吞吐 = (1008 * 0.6~0.85) / 13.55 * 1000 ≈ 44,600 - 62,700 tokens/s，高于 A100 BF16 下限但低于 H100 BF16 上限

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存24GB确实无法容纳54.2GB的BF16权重；带宽1008GB/s与量化后13.55GB/token的吞吐量计算逻辑自洽且量级合理。
