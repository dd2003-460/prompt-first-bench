# N131: 文献检索工具执行延迟的分布参数修正：Google Scholar 非官方接口或 Semantic Scholar API 的 P99 延迟并非严格 3μ，受网络

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

文献检索工具执行延迟的分布参数修正：Google Scholar 非官方接口或 Semantic Scholar API 的 P99 延迟并非严格 3μ，受网络抖动和反爬限流影响，实测 P99 通常在 1.5s-3s 之间（μ=200ms 仅适用于本地缓存命中或轻量 API）；若采用 Semantic Scholar，μ≈500ms, P99≈2s，此时 Hook 触发的阻塞时间从 2% 升至 ~5%（基于 50 tok/s, 1 trigger/500 tokens 计算：2s / (500/50 s) = 20% per trigger? No, 1 trigger per 10s, 2s block -> 20% delay per trigger event, but triggers are sparse. Correct calc: Average delay per token = (P99_delay * Trigger_Freq) = 2s * (1/10s) = 0.2s/s = 20% overhead if always hitting P99. Realistic avg overhead = μ * Freq = 0.5s * 0.1/s = 5%.

## Corrected Claim

文献检索工具执行延迟受网络抖动和反爬限流影响，通常高于本地缓存场景。以 Semantic Scholar API 为例，典型平均延迟可能在数百毫秒级别，P99 延迟可能在秒级，导致 Hook 触发的阻塞时间占比显著高于轻量级本地操作（具体数值需根据实时网络状况和 API 负载动态评估，不宜固定为单一数值）。

## Evidence

[质询]该陈述包含具体的经验性能数据（如 Semantic Scholar API 的 μ≈500ms, P99≈2s 以及 Google Scholar 的 P99 范围），这些属于特定网络环境和 API 版本下的实测经验值，无法从第一性原理或数学公理中严格推导出来。此外，'非官方接口'的行为具有高度不确定性，断言其 P99 在 1.5s-3s 之间缺乏普适性保证。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体 API 延迟参数属经验数据，不可由第一性原理推出）

## Search Query

semantic scholar api p99 latency benchmark millisecond distribution academic search
