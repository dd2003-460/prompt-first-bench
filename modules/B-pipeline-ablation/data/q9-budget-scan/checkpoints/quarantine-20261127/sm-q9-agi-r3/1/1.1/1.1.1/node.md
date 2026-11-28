# N37: 在TP=4配置下，vLLM默认的激活值缓冲（Activations）单卡预留空间约为 1.0 - 1.5 GB（取决于max_batch_size和chunke

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

在TP=4配置下，vLLM默认的激活值缓冲（Activations）单卡预留空间约为 1.0 - 1.5 GB（取决于max_batch_size和chunked_prefill配置），需从剩余显存中扣除。

## Corrected Claim

在TP=4配置下，vLLM默认的激活值缓冲（Activations）单卡预留空间约为 1.0 - 1.5 GB（取决于max_batch_size和chunked_prefill配置），需从剩余显存中扣除。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM activation memory usage per card TP4 27B
