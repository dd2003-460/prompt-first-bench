# N56: 重新计算稳态命中率下界：H_byte_LRU_eff ≥ 1 - (C_eff / W_eff_eff)，其中 W_eff_eff 是有效工作集大小，需根据 C

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

重新计算稳态命中率下界：H_byte_LRU_eff ≥ 1 - (C_eff / W_eff_eff)，其中 W_eff_eff 是有效工作集大小，需根据 C_eff 重新求解 ∫_{k=1}^{K_eff} S(k) dk = C_eff，得到新的 K_eff，然后计算 H_byte_LRU_eff = ∫_{k=1}^{K_eff} R(k) dk / ∫_{k=1}^{N} R(k) dk。

## Corrected Claim

重新计算稳态命中率下界：H_byte_LRU_eff ≥ 1 - (C_eff / W_eff_eff)，其中 W_eff_eff 是有效工作集大小，需根据 C_eff 重新求解 ∫_{k=1}^{K_eff} S(k) dk = C_eff，得到新的 K_eff，然后计算 H_byte_LRU_eff = ∫_{k=1}^{K_eff} R(k) dk / ∫_{k=1}^{N} R(k) dk。

## Evidence

父节点级核验未通过：非正交（子节点1（Stale_bytes积分）和子节点2（C_eff数值）存在逻辑依赖而非正交关系，且子节点2直接给出了子节点1计算的结果，导致信息重叠。更严重的是，父节点定义的公式中分母是 ∫S(k)dk（工作集大小），而子节点4使用的公式分母是 ∫R(k)S(k)dk（总请求量），分子也是 ∫R(k)S(k)dk，这与父节点定义的 H_byte_LRU_eff = ∫R(k)dk / ∫R(k)dk 不一致，存在公式矛盾。）

## Search Query

LRU hit rate recalculation with reduced cache capacity
