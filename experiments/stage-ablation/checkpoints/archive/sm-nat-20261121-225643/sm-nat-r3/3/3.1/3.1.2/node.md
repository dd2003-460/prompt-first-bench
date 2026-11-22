# N31: P_stale 的下界修正：由于 T_resident ≈ 1e-8 天，P_stale = min(1, u * T_resident) ≈ 1e-10，远小

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

P_stale 的下界修正：由于 T_resident ≈ 1e-8 天，P_stale = min(1, u * T_resident) ≈ 1e-10，远小于 N11 假设的 0.01，因此新鲜度失效对命中率的直接折损可忽略不计，主要影响来自对象更新导致的缓存内容失效而非驻留过期

## Corrected Claim

P_stale 的下界修正：由于 T_resident ≈ 1e-8 天，P_stale = min(1, u * T_resident) ≈ 1e-10，远小于 N11 假设的 0.01，因此新鲜度失效对命中率的直接折损可忽略不计，主要影响来自对象更新导致的缓存内容失效而非驻留过期

## Evidence

父节点级核验未通过：有冗余（子节点本质上是对同一公式 P_stale ≈ u * T_resident 在不同参数组合下的数值验证，属于同一逻辑维度的不同样本点，而非结构上正交的独立方面。虽然覆盖了不同量级以证明结论的鲁棒性，但结构上存在参数化冗余。）
