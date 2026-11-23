# N212: M/M/K模型中P99等待时间的精确解析公式：W_q(P99) = (P(W_q > t_p99))^{-1} * ... 或基于Erlang C公式推导的尾延

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

M/M/K模型中P99等待时间的精确解析公式：W_q(P99) = (P(W_q > t_p99))^{-1} * ... 或基于Erlang C公式推导的尾延迟近似，需代入具体的K（并发连接数）和ρ（利用率）计算毫秒级数值，而非仅定性描述'急剧上升'

## Corrected Claim

M/M/K模型中P99等待时间的精确解析公式：W_q(P99) = (P(W_q > t_p99))^{-1} * ... 或基于Erlang C公式推导的尾延迟近似，需代入具体的K（并发连接数）和ρ（利用率）计算毫秒级数值，而非仅定性描述'急剧上升'

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/K排队论中等待时间服从混合分布（含原子质量在0处和指数尾部），P99等待时间确实可通过Erlang C公式推导出的尾概率分布函数反解或数值积分获得精确解析/数值解，且依赖于K和ρ，逻辑自洽。

## Search Query

M/M/K queue P99 latency formula Erlang C tail latency calculation
