# N121: RTX 4090 在 W4 量化下运行 Qwen3-27B 32K 上下文时，理论解码吞吐上限为 1008 GB/s / 13.5 GB = 74.6 toke

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28, N29, N30

## Claim

RTX 4090 在 W4 量化下运行 Qwen3-27B 32K 上下文时，理论解码吞吐上限为 1008 GB/s / 13.5 GB = 74.6 tokens/s，实际需乘以框架效率系数 0.7-0.8 得到 52-60 tokens/s

## Corrected Claim

RTX 4090 在 W4 量化下运行 Qwen3-27B 32K 上下文时，理论解码吞吐上限为 1008 GB/s / 13.5 GB = 74.6 tokens/s，实际需乘以框架效率系数 0.7-0.8 得到 52-60 tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽约 1008 GB/s，Qwen3-27B W4 量化模型权重约 13.5 GB，理论上限 1008/13.5 ≈ 74.6 tokens/s，乘以 0.7-0.8 效率系数得 52-60 tokens/s，数值量级与逻辑自洽。

## Search Query

RTX 4090 W4 inference throughput tokens per second
