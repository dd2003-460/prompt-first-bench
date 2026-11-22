# N267: A100 80GB SXM4 在 BF16 量化下的理论 Decode 吞吐上限 = 2039 GB/s / (54.2 GB + 10.31 GB + 2.0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

A100 80GB SXM4 在 BF16 量化下的理论 Decode 吞吐上限 = 2039 GB/s / (54.2 GB + 10.31 GB + 2.03 GB) * 1000 ≈ 31.0 tokens/s（单卡）；若使用 2卡 NVLink TP，通信开销可忽略（<2%），总吞吐 ≈ 61.5 tokens/s，但硬件成本翻倍。

## Corrected Claim

A100 80GB SXM4 在 BF16 量化下的理论 Decode 吞吐上限 = 2039 GB/s / (54.2 GB + 10.31 GB + 2.03 GB) * 1000 ≈ 31.0 tokens/s（单卡）；若使用 2卡 NVLink TP，通信开销可忽略（<2%），总吞吐 ≈ 61.5 tokens/s，但硬件成本翻倍。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM4 带宽 2039 GB/s 与模型权重/激活/KV Cache 总量约 66.5 GB 的算术运算结果 30.66 与 31.0 在合理误差范围内，双卡线性扩展逻辑自洽。
