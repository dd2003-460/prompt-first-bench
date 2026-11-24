# N143: P99 延迟对命中率 H 的非线性修正：N34 的线性公式 P99 = H*T_local + (1-H)*T_origin 仅在请求延迟分布为双峰且无重叠时成

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

P99 延迟对命中率 H 的非线性修正：N34 的线性公式 P99 = H*T_local + (1-H)*T_origin 仅在请求延迟分布为双峰且无重叠时成立。实际 P99 受长尾影响，若 T_local 的 P99 为 20ms，T_origin 的 P99 为 150ms，则混合 P99 并非简单加权平均，而是取第 99 百分位的实际观测值。当 H=90% 时，10% 的请求进入 T_origin 分布，若 T_origin 的 P99.9 为 500ms，则整体 P99 可能接近 T_origin 的 P90 值，而非平均值。需引入分布函数 F(t) 进行积分计算。

## Corrected Claim

P99 延迟对命中率 H 的非线性修正：N34 的线性公式 P99 = H*T_local + (1-H)*T_origin 仅在请求延迟分布为双峰且无重叠时成立。实际 P99 受长尾影响，若 T_local 的 P99 为 20ms，T_origin 的 P99 为 150ms，则混合 P99 并非简单加权平均，而是取第 99 百分位的实际观测值。当 H=90% 时，10% 的请求进入 T_origin 分布，若 T_origin 的 P99.9 为 500ms，则整体 P99 可能接近 T_origin 的 P90 值，而非平均值。需引入分布函数 F(t) 进行积分计算。

## Evidence

先验知识/题面给定，逻辑校验通过：P99是统计分位数，不满足线性叠加性质，混合分布的分位数确实取决于具体分布形态而非均值加权，该陈述符合统计学基本原理。

## Search Query

percentile latency calculation bimodal distribution cache hit miss
