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

父节点级核验通过：正交+完备+无冗余（子节点1负责推导误差公式并计算相对比例（无量纲），子节点2负责引入基准参数并计算绝对数值，两者逻辑上为“公式推导”与“参数实例化”的关系，互不重复且共同覆盖了父节点中“量化具体百分比值”的要求。）

## Search Query

LRU cache warm-up time steady state convergence rate
