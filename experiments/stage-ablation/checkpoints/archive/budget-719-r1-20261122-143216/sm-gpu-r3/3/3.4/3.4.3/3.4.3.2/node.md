# N259: A100 80GB 在 BF16 精度、Batch=1 场景下的性价比指标上限，计算公式为 35.9 tokens/s / ($12000 + $885 + $

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N91

## Claim

A100 80GB 在 BF16 精度、Batch=1 场景下的性价比指标上限，计算公式为 35.9 tokens/s / ($12000 + $885 + $2400) ≈ 0.00235 tokens/s/$，代表低电价、高带宽利用率的最佳情况，用于与 RTX 5090 等消费卡进行最优情况下的对比

## Corrected Claim

A100 80GB 在 BF16 精度、Batch=1 场景下的性价比指标上限，计算公式为 35.9 tokens/s / ($12000 + $885 + $2400) ≈ 0.00235 tokens/s/$，代表低电价、高带宽利用率的最佳情况，用于与 RTX 5090 等消费卡进行最优情况下的对比

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB 在 BF16 下 Batch=1 的推理速度受限于内存带宽，35.9 tokens/s 符合其 2TB/s 带宽及模型权重大小的量级估算；成本构成（硬件+电力+其他）及除法运算逻辑自洽，数值量级合理。
