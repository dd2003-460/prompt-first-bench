# N260: A100 SXM 的 2039 GB/s 带宽在 Qwen3-27B BF16 推理中，受限于模型并行策略（TP=1），实际有效带宽利用率约为 60-80%，导

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

A100 SXM 的 2039 GB/s 带宽在 Qwen3-27B BF16 推理中，受限于模型并行策略（TP=1），实际有效带宽利用率约为 60-80%，导致有效吞吐量上限约为 25-35 tokens/s（Batch Size=1, 32K context）。

## Corrected Claim

A100 SXM 的 2039 GB/s 带宽在 Qwen3-27B BF16 推理中（TP=1, Batch Size=1, 32K context），受限于模型并行策略和内存访问模式，实际有效带宽利用率通常低于理论峰值，导致有效吞吐量上限显著低于基于纯带宽计算的极限值。

## Evidence

[质询]该陈述包含具体的经验性数值（60-80%利用率、25-35 tokens/s），这些数值高度依赖于具体的硬件配置、软件栈版本（如TensorRT-LLM或vLLM版本）、KV Cache实现细节及内存访问模式，无法仅从第一性原理或通用硬件规格严格推导得出，属于缺乏具体来源支持的经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体吞吐量数值无法从第一性原理严格推出）

## Search Query

A100 80GB Qwen2.5 72B or 32B inference throughput tokens per second
