# N22: Qwen3-27B模型在BF16精度下的理论推理吞吐量（tokens/s）与硬件显存带宽成正比，公式为：吞吐量 = 显存带宽 / (权重大小 + 激活值大小 +

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B模型在BF16精度下的理论推理吞吐量（tokens/s）与硬件显存带宽成正比，公式为：吞吐量 = 显存带宽 / (权重大小 + 激活值大小 + KV Cache大小)

## Corrected Claim

Qwen3-27B模型在BF16精度下的理论推理吞吐量（tokens/s）与硬件显存带宽成正比，公式为：吞吐量 = 显存带宽 / (权重大小 + 激活值大小 + KV Cache大小)

## Evidence

先验知识/题面给定，逻辑校验通过：在大模型推理的Decode阶段，计算密度低，主要瓶颈为显存带宽，吞吐量近似等于带宽除以每次生成token需读取的总数据量（权重+激活+KV Cache），符合Roofline模型基本原理。
