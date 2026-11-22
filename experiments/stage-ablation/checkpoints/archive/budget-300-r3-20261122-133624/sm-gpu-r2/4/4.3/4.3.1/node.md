# N102: vLLM 0.6.x 版本对 Qwen3-27B 架构的官方支持状态：需确认是否已合并 Qwen3 的 config.json 解析逻辑及专用算子（如 GQA 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

vLLM 0.6.x 版本对 Qwen3-27B 架构的官方支持状态：需确认是否已合并 Qwen3 的 config.json 解析逻辑及专用算子（如 GQA 优化），若未支持则需回退至 SGLang 或 llama.cpp，导致吞吐量下降约 15-20%。

## Corrected Claim

vLLM 0.6.x 版本对 Qwen3-27B 架构的官方支持状态需确认，若未支持则需回退至其他框架，可能导致吞吐量下降。

## Evidence

[质询]该陈述包含具体的经验性数值（吞吐量下降15-20%）和特定的版本支持状态（vLLM 0.6.x对Qwen3的支持），这些属于经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM 0.6 Qwen3 support github issue
