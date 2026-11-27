# N252: A100 80GB 在 BF16 精度、Batch=1、32K 上下文下的实际 Decode 吞吐量下限，计算公式为 (2039 GB/s × 0.7) / 5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

A100 80GB 在 BF16 精度、Batch=1、32K 上下文下的实际 Decode 吞吐量下限，计算公式为 (2039 GB/s × 0.7) / 54 GB ≈ 26.3 tokens/s，代表内存带宽利用率低（70%）且计算/访存重叠效率差时的保守工作点

## Corrected Claim

A100 80GB 在 BF16 精度、Batch=1、32K 上下文下的实际 Decode 吞吐量下限，计算公式为 (2039 GB/s × 0.7) / 54 GB ≈ 26.3 tokens/s，代表内存带宽利用率低（70%）且计算/访存重叠效率差时的保守工作点

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB HBM2e 带宽约 2039 GB/s，BF16 下 54GB 模型权重读取耗时约 0.0265s，对应理论上限约 37.7 tokens/s；按 70% 带宽利用率计算得 26.3 tokens/s，量级与逻辑自洽。
