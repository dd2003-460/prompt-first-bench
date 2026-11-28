# N94: 分块处理策略的成本-收益平衡：启用分块后推理延迟增加T_overhead = T_merge * N_chunks，T_merge为分块结果合并耗时（~200m

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

分块处理策略的成本-收益平衡：启用分块后推理延迟增加T_overhead = T_merge * N_chunks，T_merge为分块结果合并耗时（~200ms/chunk），质量增益ΔQ = Q_chunked - Q_flat，当ΔQ/T_overhead > 0.05 quality-points/ms时策略可行。

## Corrected Claim

分块处理策略的成本-收益平衡：启用分块后推理延迟增加 T_overhead = T_merge * N_chunks，T_merge 为分块结果合并耗时（具体值依实现而定），质量增益 ΔQ = Q_chunked - Q_flat，当 ΔQ/T_overhead 超过特定业务定义的阈值时策略可行。

## Evidence

[质询]阈值 0.05 quality-points/ms 缺乏通用标准定义，且 T_merge 的 ~200ms/chunk 为特定实现下的经验值，不同系统差异巨大，该具体数值组合不具备普适性。 | 先验知识/题面给定，逻辑校验通过，但具体参数值为经验事实，缺乏通用来源支持，故降级。
