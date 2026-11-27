# N235: 在 Batch Size=1 且未启用 FlashAttention 优化的基线场景下，RTX 5090 的内存带宽利用率（MBU）通常处于 0.6-0.7 区

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N83

## Claim

在 Batch Size=1 且未启用 FlashAttention 优化的基线场景下，RTX 5090 的内存带宽利用率（MBU）通常处于 0.6-0.7 区间，导致实际 FP8 吞吐量上限约为 40-46 tokens/s，此工作点代表消费级显卡在低算力利用率下的典型性能损耗。

## Corrected Claim

在 Batch Size=1 且未启用 FlashAttention 优化的基线场景下，RTX 5090 的内存带宽利用率（MBU）通常处于 0.6-0.7 区间，实际 FP8 吞吐量上限约为 40-46 tokens/s（具体数值随模型规模与序列长度波动），此工作点代表消费级显卡在低算力利用率下的典型性能损耗。

## Evidence

[质询]具体数值（0.6-0.7 MBU, 40-46 tokens/s）属于特定硬件在特定软件栈下的经验测量值，缺乏通用性，且不同模型架构、序列长度及驱动版本会导致显著波动，直接断言为'通常'区间存在过度概括风险。 | 先验知识/题面给定，逻辑校验通过：Batch Size=1时受限于内存带宽，RTX 5090带宽约1.8TB/s，FP8精度下理论峰值高，但实际受限于kernel launch overhead及非理想访存模式，MBU 0.6-0.7及对应吞吐量量级符合消费级显卡低并发场景的物理直觉与工程经验，无来源矛盾。
