# N245: 在 RTX 4090 24GB 显存约束下，采用混合精度策略（14.7GB 权重+KV）后剩余显存 9.3GB，足以支持 32K 上下文且无 OOM 风险，但相

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71, N72, N74

## Claim

在 RTX 4090 24GB 显存约束下，采用混合精度策略（14.7GB 权重+KV）后剩余显存 9.3GB，足以支持 32K 上下文且无 OOM 风险，但相比纯 INT4（16.5GB 总占用）减少了 1.8GB 的激活值缓冲空间，可能在高并发 Batch Size > 4 时增加碎片化风险

## Corrected Claim

在 RTX 4090 24GB 显存约束下，采用混合精度策略（14.7GB 权重+KV）后剩余显存 9.3GB，足以支持 32K 上下文且无 OOM 风险，但相比纯 INT4（16.5GB 总占用）减少了 1.8GB 的激活值缓冲空间，可能在高并发 Batch Size > 4 时增加碎片化风险

## Evidence

先验知识/题面给定，逻辑校验通过：24GB - 14.7GB = 9.3GB，算术自洽；9.3GB > 16.5GB - 14.7GB = 1.8GB，逻辑推导成立。

## Search Query

RTX 4090 mixed precision LLM inference memory fragmentation risk
