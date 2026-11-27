# N133: P99 延迟 < 2s 对推理吞吐的约束：假设 Qwen3-27B 在 RTX 4090 上的平均生成速度为 50 tokens/s，生成 100 tokens

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

P99 延迟 < 2s 对推理吞吐的约束：假设 Qwen3-27B 在 RTX 4090 上的平均生成速度为 50 tokens/s，生成 100 tokens 输出需 2s；若输入上下文为 32K tokens，Prefill 阶段计算量巨大，RTX 4090 (1008 GB/s) 的 Prefill 延迟可能超过 2s，而 H100 (3350 GB/s) 可将 Prefill 延迟降低至约 0.6s，满足 P99 要求。

## Corrected Claim

P99 延迟 < 2s 对推理吞吐的约束：假设 Qwen3-27B 在 RTX 4090 上的平均生成速度为 50 tokens/s，生成 100 tokens 输出需 2s；若输入上下文为 32K tokens，Prefill 阶段计算量巨大，RTX 4090 的 Prefill 延迟可能超过 2s，而 H100 凭借更高的算力和带宽可将 Prefill 延迟显著降低，更有可能满足 P99 要求。

## Evidence

[质询]Prefill 延迟并非单纯由显存带宽（GB/s）决定，而是受计算能力（FLOPS）和内存带宽共同制约（Compute-Bound vs Memory-Bound）。对于 32K 长上下文，Prefill 通常是计算密集型任务，仅用带宽比值（3350/1008 ≈ 3.3x）推导延迟降低至 0.6s 缺乏严谨的物理/工程依据，且 RTX 4090 的 FP16/BF16 算力远低于 H100，实际延迟差距可能更大或受其他瓶颈影响，该线性估算过于简化。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，且 Prefill 延迟估算模型过于简化，未考虑算力瓶颈，故降级。

## Search Query

Qwen3-27B 32k context prefill latency RTX 4090 vs H100
