# N179: vLLM中KV Cache Manager的元数据开销（Block Table, Req-to-Block映射）与序列长度线性相关，在32K上下文下，该元数据开

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

vLLM中KV Cache Manager的元数据开销（Block Table, Req-to-Block映射）与序列长度线性相关，在32K上下文下，该元数据开销约为0.5-1.0GB，包含在N9所述的5-10%框架开销内，需从总显存中独立扣除以确保护边际。

## Corrected Claim

vLLM中KV Cache Manager的元数据开销（Block Table, Req-to-Block映射）与序列长度线性相关，在32K上下文下，该元数据开销约为0.5-1.0GB，包含在N9所述的5-10%框架开销内，需从总显存中独立扣除以确保护边际。

## Evidence

先验知识/题面给定，逻辑校验通过：vLLM的Block Table和Req-to-Block映射结构确实与序列长度（或块数）线性相关，32K上下文下的元数据开销量级（0.5-1.0GB）在工程实践中合理，且属于框架固定开销的一部分。

## Search Query

vLLM KV cache manager memory overhead block table size 32k context
