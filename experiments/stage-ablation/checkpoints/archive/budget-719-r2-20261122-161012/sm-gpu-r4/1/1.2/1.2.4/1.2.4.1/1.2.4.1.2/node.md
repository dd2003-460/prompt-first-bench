# N359: 32K 上下文下 KV Cache 占用的敏感性分析：若上下文长度从 32K 增加至 64K，KV Cache 占用从 8.59GB 线性增加至 17.18GB

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N149

## Claim

32K 上下文下 KV Cache 占用的敏感性分析：若上下文长度从 32K 增加至 64K，KV Cache 占用从 8.59GB 线性增加至 17.18GB；在 24GB 卡 (INT4 权重) 上，64K 上下文将直接导致 OOM (17.18GB > 9.5GB 可用)，因此 24GB 卡仅适用于严格限制在 32K 以内的场景，不具备扩展性。

## Corrected Claim

32K 上下文下 KV Cache 占用的敏感性分析：若上下文长度从 32K 增加至 64K，KV Cache 占用从 8.59GB 线性增加至 17.18GB；在 24GB 卡 (INT4 权重) 上，64K 上下文将直接导致 OOM (17.18GB > 9.5GB 可用)，因此 24GB 卡仅适用于严格限制在 32K 以内的场景，不具备扩展性。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 大小与上下文长度呈线性关系，8.59GB * 2 = 17.18GB，且 17.18GB 超过 9.5GB 可用显存，推导自洽。

## Search Query

KV cache size linear scaling context length LLM inference
