# N124: H100 SXM5 的 BF16 原生推理吞吐量基准：在 32K 上下文下，单用户 tokens/s 约为 60-80 tokens/s，TTFT 约 1.0-

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30, N31, N32

## Claim

H100 SXM5 的 BF16 原生推理吞吐量基准：在 32K 上下文下，单用户 tokens/s 约为 60-80 tokens/s，TTFT 约 1.0-1.5s [待核验]。用于对比 FP8 加速比及与消费级卡 BF16 性能的差距。

## Corrected Claim

H100 SXM5 的 BF16 原生推理吞吐量基准：在 32K 上下文下，单用户 tokens/s 约为 60-80 tokens/s，TTFT 约 1.0-1.5s（注：具体数值依赖模型大小、批处理策略及软件栈优化，此处为典型估算值，缺乏特定基准测试来源直接证实）。

## Evidence

[质询]参考来源仅包含硬件规格（制程、架构、发布时间），完全未涉及任何推理吞吐量（tokens/s）或首字延迟（TTFT）的性能基准数据，无法提供外部证据支持具体的数值范围。 | 经验事实，逻辑自洽但缺来源支持（来源[1]仅含硬件规格，无性能数据）

## Search Query

H100 SXM5 Qwen3 27B BF16 inference throughput tokens per second 32k context

## Retrieval Sources

- {'url': 'https://www.techpowerup.com/gpu-specs/h100-sxm5-80-gb.c3900&rut=7f09b993aaca417c6d41aa8399b54260e9db367c890d472157a2dd44b4964b15', 'type': 'ddg', 'title': 'NVIDIA H100 SXM5 80 GB Specs | TechPowerUp GPU Database'}
