# N68: t_embedding 的硬件依赖分析：若嵌入模型为本地部署的小模型（如 BGE-small，<100M params），在 MacBook M1 Max 上推

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

t_embedding 的硬件依赖分析：若嵌入模型为本地部署的小模型（如 BGE-small，<100M params），在 MacBook M1 Max 上推理 500 tokens 的延迟约为 50-200ms；若调用云端 API（如 OpenAI text-embedding-3-small），延迟主要受网络 RTT 限制，通常为 200-500ms。

## Corrected Claim

t_embedding 的硬件依赖分析：若嵌入模型为本地部署的小模型（如 BGE-small，<100M params），在 MacBook M1 Max 上推理 500 tokens 的延迟约为 50-200ms；若调用云端 API（如 OpenAI text-embedding-3-small），延迟主要受网络 RTT 限制，通常为 200-500ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

BGE-small inference latency Apple M1 Max
