# N342: H100 在 32K 上下文下的首字延迟（TTFT）为 50ms，满足 <100ms 的延迟容忍度要求

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

H100 在 32K 上下文下的首字延迟（TTFT）为 50ms，满足 <100ms 的延迟容忍度要求

## Corrected Claim

H100 在 32K 上下文下的首字延迟（TTFT）通常可满足 <100ms 的延迟容忍度要求（具体数值取决于实现细节，如50ms仅为特定优化场景下的估计值）。

## Evidence

[质询]该陈述包含具体的硬件性能指标（H100在32K上下文下的TTFT为50ms），属于经验事实。50ms是一个极其乐观的数值，通常受限于KV Cache加载、Prefill计算及网络开销，实际场景中往往更高（通常在100ms-500ms+范围，取决于具体实现和硬件配置）。缺乏来源支持无法确认该特定数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。

## Search Query

H100 Qwen3-27B 32K context TTFT latency ms
