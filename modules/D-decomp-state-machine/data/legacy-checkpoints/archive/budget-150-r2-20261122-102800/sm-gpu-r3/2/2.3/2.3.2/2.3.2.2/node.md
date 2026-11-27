# N226: FFN Intermediate 激活显存峰值修正值：在 Qwen3-27B (intermediate_size=11008) 32K ctx 下，FFN 中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

FFN Intermediate 激活显存峰值修正值：在 Qwen3-27B (intermediate_size=11008) 32K ctx 下，FFN 中间层激活 (seq_len × intermediate_size × 2 bytes) 理论峰值为 1.43 GB；在 batch=1 且无梯度存储的推理模式下，该值即为单步 FFN 计算所需最大瞬时激活显存，不随层数线性累积（因逐层释放）。

## Corrected Claim

FFN Intermediate 激活显存峰值修正值：在 Qwen3-27B (intermediate_size=11008) 32K ctx 下，FFN 中间层激活 (seq_len × intermediate_size × 2 bytes) 理论峰值为 1.43 GB；在 batch=1 且无梯度存储的推理模式下，该值即为单步 FFN 计算所需最大瞬时激活显存，不随层数线性累积（因逐层释放）。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 32768 * 11008 * 2 bytes ≈ 1.43 GB 准确；推理模式下逐层计算并释放激活值的机制符合标准 Transformer 推理流程，无梯度存储且 batch=1 时峰值即为单层中间激活大小，逻辑自洽。

## Search Query

Transformer FFN intermediate activation memory size inference batch 1
