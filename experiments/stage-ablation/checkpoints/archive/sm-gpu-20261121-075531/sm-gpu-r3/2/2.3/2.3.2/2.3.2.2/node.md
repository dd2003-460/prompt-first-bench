# N191: H100 80GB 运行 Qwen3-27B INT8 时的理论峰值 TPS，基于 HBM3 带宽 3.35 TB/s 和权重加载瓶颈计算，约为 100-120

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

H100 80GB 运行 Qwen3-27B INT8 时的理论峰值 TPS，基于 HBM3 带宽 3.35 TB/s 和权重加载瓶颈计算，约为 100-120 tokens/s，远高于消费级卡，但需扣除 32K 上下文下 KV Cache 计算开销后的实际值。

## Corrected Claim

H100 80GB 运行 Qwen3-27B INT8 时的理论峰值 TPS，基于 HBM3 带宽 3.35 TB/s 和权重加载瓶颈计算，约为 100-120 tokens/s，远高于消费级卡，但需扣除 32K 上下文下 KV Cache 计算开销后的实际值。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 80GB HBM3 带宽约 3.35 TB/s，Qwen3-27B INT8 权重约 27GB，理论峰值 TPS ≈ 3350/27 ≈ 124 tokens/s，与陈述的 100-120 tokens/s 量级一致，且符合大模型推理带宽瓶颈的基本物理直觉。
