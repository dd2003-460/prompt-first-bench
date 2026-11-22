# N150: SGLang 对 Qwen3-27B 的 FP8 KV Cache 支持同样依赖 FP8 Tensor Core，RTX 4090 支持，RTX 3090 不支

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

SGLang 对 Qwen3-27B 的 FP8 KV Cache 支持同样依赖 FP8 Tensor Core，RTX 4090 支持，RTX 3090 不支持；SGLang 在长上下文 (32K) 下的 RadixAttention 优化可提升 KV Cache 复用率，减少实际占用 10%-20% [待核验: 具体复用率]。

## Corrected Claim

SGLang 对 Qwen3-27B 的 FP8 KV Cache 支持依赖 FP8 Tensor Core，RTX 4090 支持，RTX 3090 不支持；SGLang 在长上下文 (32K) 下的 RadixAttention 优化可提升 KV Cache 复用率，具体减少占用比例取决于工作负载的前缀共享特征。

## Evidence

[质询]具体数值（10%-20%）缺乏来源支持，且RadixAttention的复用率提升高度依赖工作负载特征（如前缀共享程度），并非固定常数，存在将特定场景数据泛化为通用指标的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

SGLang FP8 KV cache Qwen3 long context RadixAttention memory reduction
