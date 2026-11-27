# N195: 修正自矛盾检测：基于 N121 的准确计算（K=12.88GB, V=12.88GB），32K 上下文下单个请求的 KV Cache 总占用应为 25.76GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

修正自矛盾检测：基于 N121 的准确计算（K=12.88GB, V=12.88GB），32K 上下文下单个请求的 KV Cache 总占用应为 25.76GB（BF16），而非 N60 原述的 4GB 或 N88 的 8GB；这意味着每生成一个 token 需读取整个 25.76GB 的 KV Cache（若无 PagedAttention 优化），这将导致 RTX 5090 的 TPOT 高达 14.4ms（25.76GB/1792GB/s），远超可接受范围，因此必须启用 PagedAttention 或 KV Cache 量化。

## Corrected Claim

修正自矛盾检测：基于 N121 的准确计算（K=12.88GB, V=12.88GB），32K 上下文下单个请求的 KV Cache 总占用应为 25.76GB（BF16），而非 N60 原述的 4GB 或 N88 的 8GB；这意味着每生成一个 token 需读取整个 25.76GB 的 KV Cache（若无 PagedAttention 优化），这将导致 RTX 5090 的 TPOT 高达 14.4ms（25.76GB/1792GB/s），远超可接受范围，因此必须启用 PagedAttention 或 KV Cache 量化。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 大小计算（25.76GB）与带宽延迟推导（14.4ms）在数学和物理量纲上自洽，符合 LLM 推理的基本原理。
