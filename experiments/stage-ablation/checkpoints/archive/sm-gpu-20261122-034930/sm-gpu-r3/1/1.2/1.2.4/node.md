# N51: Batch Size 对 KV Cache 显存的影响线性关系：KV_cache_total = 8 GB (per token batch=1) * Batc

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

Batch Size 对 KV Cache 显存的影响线性关系：KV_cache_total = 8 GB (per token batch=1) * Batch_Size。例如 Batch=4 时，KV Cache 占用 32 GB，这将显著改变单卡可行性边界（例如使 RTX 4090 24GB 在 Batch>2 时无法运行 INT8 模型）。

## Corrected Claim

KV Cache 显存占用与 Batch Size 呈线性关系（KV_cache_total = KV_cache_per_token * Batch_Size）。具体每 Token 占用量取决于模型架构与精度，例如在某些大模型配置下可能达到数 GB/Token，这将显著改变单卡可行性边界。

## Evidence

[质询]数值量级与具体硬件/模型配置强相关，'8 GB per token' 这一具体数值缺乏通用性，且未指明具体的模型架构（如层数、头数、维度）和精度，不同模型下该系数差异巨大，直接断言线性关系的具体系数存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过（KV Cache 随 Batch Size 线性增长是基本事实），但具体数值 8GB/token 为经验参数，缺乏来源支持且依赖特定模型配置，故降级。
