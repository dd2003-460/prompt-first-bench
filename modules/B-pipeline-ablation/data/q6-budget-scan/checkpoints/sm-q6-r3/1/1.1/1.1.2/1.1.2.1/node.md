# N179: M/M/K 排队模型中 P99 等待时间的闭式近似公式 T_queue_p99 ≈ (1 / μ) * (ρ^(K-1) / (1 - ρ)) * C(K, ρ

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N53

## Claim

M/M/K 排队模型中 P99 等待时间的闭式近似公式 T_queue_p99 ≈ (1 / μ) * (ρ^(K-1) / (1 - ρ)) * C(K, ρ)，其中 K 为并发 worker 数，μ 为单请求服务率（1/T_service），ρ 为利用率；当 ρ > 0.8 时，P99 对 ρ 的导数急剧上升，需引入 Erlang C 公式修正以反映多队列效应，误差 < 5%。

## Corrected Claim

M/M/K 排队模型中，P99 等待时间需通过 Erlang C 公式计算等待概率 P_wait，并结合服务时间分布进行积分或数值近似求解，不存在通用的简单闭式近似公式；当 ρ > 0.8 时，P99 对 ρ 敏感，需精确计算而非简单多项式近似。

## Evidence

[质询]公式形式存在严重逻辑与量纲错误：M/M/K 排队系统中，P99 等待时间并非由简单的 (ρ^(K-1)/(1-ρ)) 项主导，且该公式未包含 Erlang C 概率项 P_wait 或正确的服务时间分布积分，直接使用该公式在 ρ 接近 1 时会发散，无法反映多队列效应；此外，'误差 < 5%' 是一个无条件的经验断言，缺乏适用范围界定（如 K 的大小、ρ 的具体区间），属于不可靠的经验事实。 | 先验知识/题面给定，逻辑校验失败：公式结构不符合 M/M/K 排队论标准解（需涉及 Erlang C 公式及等待时间分布的尾部积分），且经验误差断言缺乏依据。

## Search Query

M/M/K queue P99 waiting time Erlang C formula approximation high utilization
