# N108: 显存带宽瓶颈公式的修正项：实际Tokens/s = (显存带宽 * 带宽利用率) / (权重字节数 + KV Cache每Token增量字节数)；其中带宽利用率

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

显存带宽瓶颈公式的修正项：实际Tokens/s = (显存带宽 * 带宽利用率) / (权重字节数 + KV Cache每Token增量字节数)；其中带宽利用率在消费级GPU上通常为0.8-0.9，KV Cache每Token增量 = 2 * 层数 * KV头数 * 头维度 * 2 bytes。

## Corrected Claim

显存带宽瓶颈公式的修正项：实际Tokens/s = (显存带宽 * 带宽利用率) / (权重字节数 + KV Cache每Token增量字节数)；其中带宽利用率在消费级GPU上通常为0.8-0.9，KV Cache每Token增量 = 2 * 层数 * KV头数 * 头维度 * 2 bytes。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合LLM推理显存带宽瓶颈的第一性原理（Roofline模型），KV Cache增量计算（2*层数*头数*维度*2bytes）符合标准Transformer架构（K/V各一份，FP16精度），消费级GPU带宽利用率0.8-0.9符合工程经验。

## Search Query

GPU inference throughput formula memory bandwidth utilization kv cache overhead token generation
