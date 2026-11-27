# N775: H100 SXM 运行 Qwen3-27B BF16 时，HBM3 带宽利用率受 L2 Cache 命中率影响，在 Batch Size=1 时 L2 命中率低

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N241

## Claim

H100 SXM 运行 Qwen3-27B BF16 时，HBM3 带宽利用率受 L2 Cache 命中率影响，在 Batch Size=1 时 L2 命中率低于 10%，导致有效带宽降至理论值 3.35 TB/s 的 85-90%（约 2.8-3.0 TB/s），实际吞吐上限修正为 42-45 tokens/s 而非 50.9 tokens/s。

## Corrected Claim

H100 SXM 运行 Qwen3-27B BF16 时，HBM3 带宽利用率受 L2 Cache 命中率影响。在 Batch Size=1 时，由于 L2 命中率较低，有效带宽通常低于理论峰值 3.35 TB/s，实际吞吐上限可能低于基于理论带宽计算的 50.9 tokens/s，具体数值需实测确定。

## Evidence

[质询]该陈述包含具体的经验性数值（L2命中率<10%、带宽利用率85-90%、吞吐42-45 tokens/s），这些参数高度依赖于具体的硬件微架构、驱动版本、CUDA实现及Qwen3-27B的具体模型结构（如KV Cache大小、Attention实现方式），无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体性能指标无法仅凭逻辑推导得出精确数值）

## Search Query

H100 HBM3 bandwidth utilization L2 cache miss rate batch size 1 effective throughput
