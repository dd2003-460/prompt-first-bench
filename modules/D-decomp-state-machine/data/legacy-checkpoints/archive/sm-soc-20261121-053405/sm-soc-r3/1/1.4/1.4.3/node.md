# N32: 共享随机源（N9）：买家搜索行为的时间依赖函数 λ_new(t, ΔP)，其核心随机源是买家在降价事件发生后的“重新检索触发概率” P(trigger | ΔP

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N8, N9, N10

## Claim

共享随机源（N9）：买家搜索行为的时间依赖函数 λ_new(t, ΔP)，其核心随机源是买家在降价事件发生后的“重新检索触发概率” P(trigger | ΔP, t)，该概率受搜索耐心阈值 δ_patience 约束。

## Corrected Claim

共享随机源（N9）：买家搜索行为的时间依赖函数 λ_new(t, ΔP)，其核心随机源是买家在降价事件发生后的“重新检索触发概率” P(trigger | ΔP, t)，该概率受搜索耐心阈值 δ_patience 约束。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了噪声分布、核心概率模型、关键参数约束以及最终的聚合函数表达式，逻辑层次清晰（从底层噪声/参数到中间模型再到顶层函数），各部分职责明确且相互独立，无重复或矛盾。）
