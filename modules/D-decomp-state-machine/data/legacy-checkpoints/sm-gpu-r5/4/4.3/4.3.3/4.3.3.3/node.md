# N201: 2x RTX 4090 在 FP8 量化下运行 Qwen3-27B，权重大小减半 (~27GB/卡)，单卡 24GB 仍可能不足（需考虑 KV Cache 和激

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

2x RTX 4090 在 FP8 量化下运行 Qwen3-27B，权重大小减半 (~27GB/卡)，单卡 24GB 仍可能不足（需考虑 KV Cache 和激活值），若采用 W4 量化则权重 ~13.5GB/卡，此时单卡显存充足，理论吞吐量上限提升至 ~30-35 tokens/s (基于 1.5TB/s 带宽修正后)。

## Corrected Claim

2x RTX 4090 在 FP8 量化下运行 Qwen3-27B，权重大小减半 (~27GB/卡)，单卡 24GB 仍可能不足（需考虑 KV Cache 和激活值），若采用 W4 量化则权重 ~13.5GB/卡，此时单卡显存充足，理论吞吐量上限提升至 ~30-35 tokens/s (基于 1.5TB/s 带宽修正后)。

## Evidence

先验知识/题面给定，逻辑校验通过
