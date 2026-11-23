# N166: 回源链路总延迟的 P99 分布受长尾影响：P99(t_origin) = t_base + t_queue(P99) + t_server(P99) + t_n

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

回源链路总延迟的 P99 分布受长尾影响：P99(t_origin) = t_base + t_queue(P99) + t_server(P99) + t_net(P99)，其中各分位数的 P99 通常比均值高 2-5 倍，需分别测量各组件的 P99 而非仅用均值相加

## Corrected Claim

回源链路总延迟的 P99 分布受长尾影响：P99(t_origin) = t_base + t_queue(P99) + t_server(P99) + t_net(P99)，其中各分位数的 P99 通常比均值高 2-5 倍，需分别测量各组件的 P99 而非仅用均值相加

## Evidence

先验知识/题面给定，逻辑校验通过：延迟分布通常呈重尾分布（如帕累托或指数分布），P99 显著高于均值是统计学常识；各组件延迟独立叠加时，总延迟的 P99 近似等于各组件 P99 之和（在强相关或独立同分布假设下为保守估计），且分别测量各组件 P99 是性能分析的标准最佳实践，逻辑自洽且符合工程直觉。

## Search Query

P99 latency tail decomposition network components
