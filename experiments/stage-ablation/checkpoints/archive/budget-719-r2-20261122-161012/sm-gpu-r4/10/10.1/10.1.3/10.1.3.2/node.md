# N718: A100 80GB 在 Qwen3-27B FP8 32K 上下文下的理论峰值吞吐量估算：A100 80GB带宽为2039 GB/s，FP8权重27GB，KV 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N294

## Claim

A100 80GB 在 Qwen3-27B FP8 32K 上下文下的理论峰值吞吐量估算：A100 80GB带宽为2039 GB/s，FP8权重27GB，KV Cache约4GB（32K BF16 KV），总访存约31GB，理论Decode速度 ≈ 2039/31 ≈ 65.7 tokens/s（假设100%带宽利用率，实际MFU取0.7则≈46 tokens/s），小时吞吐约165,600 tokens/hour，单位成本（假设$4.88/hour）≈ $0.0000295/token。

## Corrected Claim

A100 80GB 在 Qwen3-27B FP8 32K 上下文下的理论峰值吞吐量估算：A100 80GB带宽为2039 GB/s，FP8权重27GB，KV Cache约4GB（32K BF16 KV），总访存约31GB，理论Decode速度 ≈ 2039/31 ≈ 65.7 tokens/s（假设100%带宽利用率，实际MFU取0.7则≈46 tokens/s），小时吞吐约165,600 tokens/hour，单位成本（假设$4.88/hour）≈ $0.0000295/token。

## Evidence

[质询]KV Cache 估算可能偏低（若考虑 GQA 或具体层数/头数配置，32K 上下文的 KV 占用可能高于 4GB，从而降低理论峰值），但作为量级估算逻辑自洽。 | 先验知识/题面给定，逻辑校验通过：A100 80GB 带宽 2039 GB/s 为已知规格，FP8 权重 27GB 与模型参数量匹配，访存计算与吞吐量推导符合内存带宽瓶颈模型的基本逻辑。
