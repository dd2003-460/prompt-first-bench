# N420: 在Batch=1, ctx=32K, INT8精度下，2x RTX 4090 (PCIe互联) 的KV Cache分片同步开销导致有效吞吐率降至18-20 to

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N152

## Claim

在Batch=1, ctx=32K, INT8精度下，2x RTX 4090 (PCIe互联) 的KV Cache分片同步开销导致有效吞吐率降至18-20 tokens/s，具体数值取决于KV Cache在双卡间的切分策略（如按Head切分或按Layer切分）及PCIe 4.0 x16双向带宽利用率（通常<50%）。

## Corrected Claim

在Batch=1, ctx=32K, INT8精度下，2x RTX 4090 (PCIe互联) 的KV Cache分片同步开销会显著降低有效吞吐率，具体数值取决于KV Cache切分策略及PCIe 4.0 x16双向带宽利用率。

## Evidence

[质询]该陈述包含具体的经验性性能数值（18-20 tokens/s）和硬件带宽利用率假设（<50%），属于硬件规格与实测性能范畴，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM tensor parallelism 2x RTX 4090 Qwen3-27B INT8 throughput benchmark 32k context
