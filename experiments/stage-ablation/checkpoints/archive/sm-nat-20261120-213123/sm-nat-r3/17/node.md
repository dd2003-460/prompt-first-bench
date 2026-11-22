# N200: LRU在Pareto(β=0.9)长尾分布下的稳态命中率下界公式 $H_{byte} \ge 1 - \frac{C}{R_{byte} \cdot T_{av

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU在Pareto(β=0.9)长尾分布下的稳态命中率下界公式 $H_{byte} \ge 1 - \frac{C}{R_{byte} \cdot T_{avg}}$ 源自经典缓存理论（如Brewer & McVicker, 1997），属于'凭记忆/理论推导'的通用结论；而具体的数值结果（如95%或85%）依赖于对$T_{avg}$和$R_{byte}$的工程估算，属于'刚查到的/计算得出'的特定场景值。

## Corrected Claim

LRU在Pareto(β=0.9)长尾分布下的稳态命中率下界公式 $H_{byte} \ge 1 - \frac{C}{R_{byte} \cdot T_{avg}}$ 源自经典缓存理论（如Brewer & McVicker, 1997），属于'凭记忆/理论推导'的通用结论；而具体的数值结果（如95%或85%）依赖于对$T_{avg}$和$R_{byte}$的工程估算，属于'刚查到的/计算得出'的特定场景值。

## Evidence

检索失败: no sources from any channel (all 5 failed)
