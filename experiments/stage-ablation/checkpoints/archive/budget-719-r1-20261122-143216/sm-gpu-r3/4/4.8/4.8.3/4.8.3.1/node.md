# N356: 64K 上下文相比 32K 上下文，Decode 阶段每生成一个 token 需从显存读取的 KV Cache 数据量增加 100% (从 10.74GB 增至

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

64K 上下文相比 32K 上下文，Decode 阶段每生成一个 token 需从显存读取的 KV Cache 数据量增加 100% (从 10.74GB 增至 21.48GB 在 BF16 下)，导致每 token 的显存访问延迟翻倍。

## Corrected Claim

64K 上下文相比 32K 上下文，Decode 阶段每生成一个 token 需从显存读取的 KV Cache 数据量增加 100% (从 10.74GB 增至 21.48GB 在 BF16 下)，导致每 token 的显存访问延迟翻倍。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 大小与上下文长度成正比，64K 是 32K 的 2 倍，数据量从 10.74GB 增至 21.48GB 符合线性关系，且 Decode 阶段为内存带宽瓶颈，延迟随读取量线性增加，逻辑自洽。
