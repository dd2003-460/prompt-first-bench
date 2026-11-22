# N133: P99 延迟 < 2s 对推理吞吐的约束：假设 Qwen3-27B 在 RTX 4090 上的平均生成速度为 50 tokens/s，生成 100 tokens

- **status**: pending
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

父节点级核验未通过：有冗余（子节点分别对应不同硬件平台（RTX 4090, H100, A100），彼此独立且无矛盾，覆盖了父节点中提到的关键硬件对比，因此正交性和完备性满足。然而，三个子节点本质上是同一计算模型（T_total = T_prefill + T_decode）在不同硬件带宽参数下的实例化，存在结构上的高度冗余。）

## Search Query

Qwen3-27B 32k context prefill latency RTX 4090 vs H100
