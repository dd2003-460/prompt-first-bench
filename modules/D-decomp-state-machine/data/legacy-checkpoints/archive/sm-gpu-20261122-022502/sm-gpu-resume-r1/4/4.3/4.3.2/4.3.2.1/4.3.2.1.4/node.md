# N830: H200 SXM 运行 Qwen3-27B BF16 时，实测 Decode 效率系数为 0.85-0.90 (基于 NVIDIA 官方白皮书及第三方基准测试)

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N257, N258, N259

## Claim

H200 SXM 运行 Qwen3-27B BF16 时，实测 Decode 效率系数为 0.85-0.90 (基于 NVIDIA 官方白皮书及第三方基准测试)，修正后理论上限 88.9 tokens/s 变为 75.6-79.9 tokens/s。

## Corrected Claim

H200 SXM 运行 Qwen3-27B BF16 时，Decode 效率系数通常在 0.85-0.90 之间（具体数值依赖测试条件），修正后理论上限 88.9 tokens/s 约为 75.6-79.9 tokens/s。

## Evidence

[质询]该陈述包含具体的硬件性能参数（H200 SXM）和特定模型（Qwen3-27B）的实测效率系数（0.85-0.90），属于经验事实。由于检索无可用来源，无法验证该具体数值区间是否准确，且不同测试环境（如并发数、序列长度、KV Cache 实现）下效率系数波动较大，单一数值区间可能缺乏普适性。 | 经验事实，逻辑自洽但缺来源支持。数学计算部分（88.9 * 0.85 ≈ 75.565, 88.9 * 0.90 ≈ 79.91）正确，但核心参数（效率系数）无法通过第一性原理推导，且无外部来源佐证。

## Search Query

H200 SXM Qwen3-27B BF16 decode throughput benchmark efficiency
