# N469: 预热状态对 P99 延迟的非线性影响函数：L_p99(W_cache) = L_edge + L_backhaul * (1 - W_cache)^1.5 * 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N150

## Claim

预热状态对 P99 延迟的非线性影响函数：L_p99(W_cache) = L_edge + L_backhaul * (1 - W_cache)^1.5 * (1 - H_base) + L_processing，其中指数 1.5 反映长尾对象预热滞后效应，当 W_cache = 0.5 时，L_p99 ≈ 50 + 100 * 0.354 * 0.1 + 5 ≈ 60.5 ms，比线性模型高 12%。

## Corrected Claim

预热状态对 P99 延迟的影响可用非线性模型近似描述：L_p99(W_cache) = L_edge + L_backhaul * (1 - W_cache)^1.5 * (1 - H_base) + L_processing。在特定参数设定下（如 L_edge=50ms, L_backhaul=100ms, H_base=0.1, L_processing=5ms），当 W_cache = 0.5 时，L_p99 ≈ 60.5 ms。

## Evidence

[质询]该公式为特定场景下的经验拟合模型，指数1.5及各项系数（L_edge=50, L_backhaul=100, H_base=0.1, L_processing=5）缺乏通用物理或数学公理支持，属于特定系统调优的经验参数，无法从第一性原理严格推导。 | source=knowledge，逻辑校验通过（数值计算 50 + 100*0.35355*0.1 + 5 ≈ 60.54 与陈述一致，量纲合理），但作为经验事实模型，缺乏外部来源直接支持其普适性或具体参数值的准确性，故降级。
