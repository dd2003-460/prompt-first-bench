# N43: 冷启动过渡期内 LRU 命中率 H_transit(t) 随时间 t 的演化模型：H_transit(t) ≈ H_steady × (1 - e^{-t/T_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

冷启动过渡期内 LRU 命中率 H_transit(t) 随时间 t 的演化模型：H_transit(t) ≈ H_steady × (1 - e^{-t/T_steady})，误差 ε(t) = H_steady - H_transit(t) 需量化在 t=1天 时的具体百分比值

## Corrected Claim

冷启动过渡期内 LRU 命中率 H_transit(t) 随时间 t 的演化模型：H_transit(t) ≈ H_steady × (1 - e^{-t/T_steady})，误差 ε(t) = H_steady - H_transit(t) 需量化在 t=1天 时的具体百分比值

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache warm-up time steady state convergence rate
