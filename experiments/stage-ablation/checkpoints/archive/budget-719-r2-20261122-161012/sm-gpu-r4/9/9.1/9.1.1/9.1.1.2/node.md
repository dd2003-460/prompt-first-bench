# N680: RTX 5090 在 BF16 精度下的理论 Decode 上限：权重 54GB 超出 32GB 显存，无法单卡运行 BF16；若使用 FP8 (27GB)，理

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N281

## Claim

RTX 5090 在 BF16 精度下的理论 Decode 上限：权重 54GB 超出 32GB 显存，无法单卡运行 BF16；若使用 FP8 (27GB)，理论上限 1792/27 ≈ 66.4 tokens/s (15ms/token)，实际利用率 70-80% 时为 46-53 tokens/s (19-22ms/token)；若使用 INT4 (13.5GB)，理论上限 1792/13.5 ≈ 132.7 tokens/s (7.5ms/token)，实际利用率 70-80% 时为 93-106 tokens/s (9.4-10.7ms/token)。

## Corrected Claim

RTX 5090 在 BF16 精度下的理论 Decode 上限：权重 54GB 超出 32GB 显存，无法单卡运行 BF16；若使用 FP8 (27GB)，理论上限 1792/27 ≈ 66.4 tokens/s (15ms/token)，实际利用率 70-80% 时为 46-53 tokens/s (19-22ms/token)；若使用 INT4 (13.5GB)，理论上限 1792/13.5 ≈ 132.7 tokens/s (7.5ms/token)，实际利用率 70-80% 时为 93-106 tokens/s (9.4-10.7ms/token)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 显存 32GB，BF16 权重 54GB 确实超出；FP8 27GB 和 INT4 13.5GB 在显存范围内；理论 Decode 上限计算基于 1792 tokens/s 的基准吞吐量除以权重大小，数值量级合理，实际利用率 70-80% 的估算符合工程经验。

## Search Query

RTX 5090 LLM inference FP8 INT4 tokens per second benchmark
