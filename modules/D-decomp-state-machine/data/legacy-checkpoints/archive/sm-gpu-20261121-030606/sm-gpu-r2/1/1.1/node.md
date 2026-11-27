# N7: 消费级GPU显存容量下限为24GB，基于Qwen3-27B在FP8精度下权重占用约13.5GB，需预留KV Cache空间，低于24GB的显存（如RTX 406

- **status**: pending
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

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 736)
