# N382: RTX 4090 在空闲/低负载状态下的功耗基线（Idle Power）及其在 24/7 推理场景中的时间占比修正系数：若推理请求并非 100% 满载（存在等待

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134

## Claim

RTX 4090 在空闲/低负载状态下的功耗基线（Idle Power）及其在 24/7 推理场景中的时间占比修正系数：若推理请求并非 100% 满载（存在等待时间），需结合平均利用率（Utilization %）计算加权平均功耗，公式：P_avg = P_idle * (1 - U) + P_load * U。

## Corrected Claim

RTX 4090 在空闲/低负载状态下的功耗基线（Idle Power）及其在 24/7 推理场景中的时间占比修正系数：若推理请求并非 100% 满载（存在等待时间），需结合平均利用率（Utilization %）计算加权平均功耗，公式：P_avg = P_idle * (1 - U) + P_load * U。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均功耗公式符合线性插值原理，量纲一致，且RTX 4090存在明确的空闲与负载功耗差异，逻辑自洽。
