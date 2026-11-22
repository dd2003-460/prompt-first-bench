# N62: P_hit_cold (陈旧对象命中概率) 的边界情形 1：完全替换场景，P_hit_cold = 0。此时 δ = 1 - C_steady，意味着所有陈旧对

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

P_hit_cold (陈旧对象命中概率) 的边界情形 1：完全替换场景，P_hit_cold = 0。此时 δ = 1 - C_steady，意味着所有陈旧对象请求均导致 Miss，惩罚最大。

## Corrected Claim

P_hit_cold (陈旧对象命中概率) 的边界情形 1：完全替换场景，P_hit_cold = 0。此时 δ = 1 - C_steady，意味着所有陈旧对象请求均导致 Miss，惩罚最大。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了低驻留、高驻留和过渡区三个互斥的时间范围，逻辑上正交且无重复。它们共同构成了对 T_cold 全值域的覆盖，满足完备性。虽然本质上是同一公式在不同区间的取值，但作为'边界情形'的分析，展示不同区间的行为差异（如线性近似失效、饱和、切换阈值）具有独立的学术分析价值，因此不视为冗余，而是必要的参数敏感性分析。）
