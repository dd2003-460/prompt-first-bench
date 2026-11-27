# N55: LRU有效命中率折扣因子 D_eff 的量化计算：D_eff = 1 - M_invalidation。若 M_invalidation ≈ 0.005（来自 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

LRU有效命中率折扣因子 D_eff 的量化计算：D_eff = 1 - M_invalidation。若 M_invalidation ≈ 0.005（来自 N30），则 D_eff ≈ 0.995，即命中率打 99.5 折。

## Corrected Claim

LRU有效命中率折扣因子 D_eff 的量化计算：D_eff = 1 - M_invalidation。若 M_invalidation ≈ 0.005（来自 N30），则 D_eff ≈ 0.995，即命中率打 99.5 折。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数（T_res）下的数值实例，存在严重冗余；且父节点强调基于N30的M_invalidation≈0.005，但子节点1和2引入了不同的M_invalidation值，未明确说明这些是假设场景而非N30的具体数据，导致与父节点的特定上下文（N30）缺乏严格对应，完备性不足。）
