# N253: A100 80GB 在 BF16 精度、Batch=1、32K 上下文下的实际 Decode 吞吐量上限，计算公式为 (2039 GB/s × 0.95) / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

A100 80GB 在 BF16 精度、Batch=1、32K 上下文下的实际 Decode 吞吐量上限，计算公式为 (2039 GB/s × 0.95) / 54 GB ≈ 35.9 tokens/s，代表内存带宽利用率极高（95%）且 Kernel Fusion 优化完美时的理论最优工作点

## Corrected Claim

A100 80GB 在 BF16 精度、Batch=1、32K 上下文下的实际 Decode 吞吐量上限，计算公式为 (2039 GB/s × 0.95) / 54 GB ≈ 35.9 tokens/s，代表内存带宽利用率极高（95%）且 Kernel Fusion 优化完美时的理论最优工作点

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB HBM2e 带宽约 2039 GB/s，BF16 下 54GB 模型权重读取一次耗时约 26.5ms，理论上限约 37.7 tokens/s，95% 利用率下 35.9 tokens/s 符合内存带宽瓶颈下的 Decode 吞吐计算逻辑。
