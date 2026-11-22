# N743: 32K 上下文单请求 KV Cache 需求与剩余显存匹配性验证：需求 8.0 GB (N368) > 剩余 6.31 GB (N371)。结论：在 RTX 4

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N261

## Claim

32K 上下文单请求 KV Cache 需求与剩余显存匹配性验证：需求 8.0 GB (N368) > 剩余 6.31 GB (N371)。结论：在 RTX 4090 24GB 上，INT4 权重 + BF16 KV Cache 无法支持 32K 上下文的单请求推理，必须启用 KV Cache 量化（如 INT8）或缩短上下文至 ~25K。

## Corrected Claim

32K 上下文单请求 KV Cache 需求与剩余显存匹配性验证：需求 8.0 GB (N368) > 剩余 6.31 GB (N371)。结论：在 RTX 4090 24GB 上，INT4 权重 + BF16 KV Cache 无法支持 32K 上下文的单请求推理，必须启用 KV Cache 量化（如 INT8）或缩短上下文至 ~25K。

## Evidence

先验知识/题面给定，逻辑校验通过：8.0 GB > 6.31 GB 的数值比较成立，且符合显存资源约束的基本逻辑。
