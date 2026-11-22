# N255: 工作点2（高吞吐/中等利用率）：在 H100 上运行 Qwen3-27B BF16 时，采用 Continuous Batching 且 Batch Size=

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86, N87, N88

## Claim

工作点2（高吞吐/中等利用率）：在 H100 上运行 Qwen3-27B BF16 时，采用 Continuous Batching 且 Batch Size=64 的 Prefill+Decode 混合负载，有效显存带宽利用率提升至 0.92 [待核验]，此时计算瓶颈（Tensor Core）开始显现，带宽不再是唯一限制。

## Corrected Claim

工作点2（高吞吐/中等利用率）：在 H100 上运行 Qwen3-27B BF16 时，采用 Continuous Batching 且 Batch Size=64 的 Prefill+Decode 混合负载，有效显存带宽利用率显著提升（接近饱和），此时计算瓶颈（Tensor Core）开始显现，带宽不再是唯一限制。

## Evidence

[质询]具体数值 0.92 缺乏来源支持，且该数值高度依赖于具体的硬件配置（HBM3 vs HBM3e）、软件栈版本及负载分布，属于经验事实而非第一性原理可推导结论。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

H100 BF16 LLM continuous batching high throughput bandwidth utilization
