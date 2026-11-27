# N45: 在 TP=4 配置下，每卡权重 1.74 GB，剩余 14.26 GB 显存中扣除 0.5 GB 激活后，KV Cache 容量为 13.76 GB / 4 卡

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

在 TP=4 配置下，每卡权重 1.74 GB，剩余 14.26 GB 显存中扣除 0.5 GB 激活后，KV Cache 容量为 13.76 GB / 4 卡 ≈ 3.44 GB/卡，支持 3.44e9 / 65536 ≈ 52,488 tokens/卡，4 卡合计 209,952 tokens，接近 262k 需求但需严格监控碎片化。

## Corrected Claim

在 TP=4 配置下，每卡权重 1.74 GB，剩余 14.26 GB 显存中扣除 0.5 GB 激活后，KV Cache 容量为 13.76 GB / 4 卡 ≈ 3.44 GB/卡，支持 3.44e9 / 65536 ≈ 52,488 tokens/卡，4 卡合计 209,952 tokens，接近 262k 需求但需严格监控碎片化。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（14.26-0.5=13.76; 13.76/4=3.44; 3.44e9/65536≈52488; 52488*4=209952），量级符合大模型推理显存估算常识。
