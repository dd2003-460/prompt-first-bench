# N256: Qwen3-27B 在 32K 上下文长度下，BF16 精度的 KV Cache 显存占用约为 14.4GB（计算式：27B参数 * 2bytes/param 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

Qwen3-27B 在 32K 上下文长度下，BF16 精度的 KV Cache 显存占用约为 14.4GB（计算式：27B参数 * 2bytes/param * 32K tokens * 2(K+V) * 注意力头占比修正），该数值是评估单卡/多卡显存可行性及与 INT8 方案（约 7.2GB）对比的基础量化指标。

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下，BF16 精度的 KV Cache 显存占用需根据具体层数、KV头数和头维度计算，通常远高于 14.4GB（例如若采用 GQA，可能在 20GB-40GB 区间），原计算式错误。

## Evidence

[质询]计算式存在严重的量纲和逻辑错误：KV Cache 的大小与模型总参数量（27B）无直接线性关系，而是取决于层数（L）、KV头数（H_kv）和头维度（D）。公式中直接乘以总参数量（27B）会导致数值量级错误（通常大几个数量级或完全不符），且 14.4GB 的数值对于 32K 上下文的 27B 模型而言通常偏小（实际往往在 20-40GB 之间，取决于具体架构如 GQA 的压缩比），该计算式本身在物理/工程逻辑上不成立。 | 逻辑校验失败：KV Cache 显存占用公式错误，不应直接乘以总参数量，且数值量级与常见 27B 模型在 32K 上下文下的实际占用不符。
