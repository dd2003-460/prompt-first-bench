# N7: 消费级GPU显存容量下限为24GB，基于Qwen3-27B在FP8精度下权重占用约13.5GB，需预留KV Cache空间，低于24GB的显存（如RTX 406

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

消费级GPU显存容量下限为24GB，基于Qwen3-27B在FP8精度下权重占用约13.5GB，需预留KV Cache空间，低于24GB的显存（如RTX 4060/4070）在32K上下文下必然溢出，故排除显存<24GB的消费级显卡。

## Corrected Claim

消费级GPU显存容量下限为24GB，基于Qwen3-27B在FP8精度下权重占用约13.5GB，需预留KV Cache空间，低于24GB的显存（如RTX 4060/4070）在32K上下文下必然溢出，故排除显存<24GB的消费级显卡。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B FP8权重约13.5GB，加上32K上下文KV Cache及激活值开销，总显存需求远超16GB，24GB为合理下限。
