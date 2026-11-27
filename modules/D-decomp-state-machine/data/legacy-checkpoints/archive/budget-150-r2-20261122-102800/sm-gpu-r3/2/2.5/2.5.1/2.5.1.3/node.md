# N235: N85 的‘不可行性’边界未包含激活内存动态波动：在 32K 上下文下，激活内存峰值可能高于 3.5GB 估算值（实际约 4.2-5.0GB），导致 INT8 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85

## Claim

N85 的‘不可行性’边界未包含激活内存动态波动：在 32K 上下文下，激活内存峰值可能高于 3.5GB 估算值（实际约 4.2-5.0GB），导致 INT8 方案（N86）的剩余余量从 5.925GB 降至 5.1-5.9GB，影响 batch 扩展能力。

## Corrected Claim

N85 的‘不可行性’边界未包含激活内存动态波动：在 32K 上下文下，激活内存峰值可能高于 3.5GB 估算值，导致 INT8 方案（N86）的剩余余量减少，影响 batch 扩展能力。

## Evidence

[质询]具体数值（4.2-5.0GB, 5.1-5.9GB）缺乏来源支持，且不同模型架构下激活内存波动范围差异巨大，直接断言具体区间可能不准确。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B 32K context activation memory peak GB vLLM
