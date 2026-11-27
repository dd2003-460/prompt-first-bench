# N16: 有效命中率 H_eff 与静态命中率 H_static 的关系为 H_eff = H_static * (1 - P_invalid) + H_dynamic_

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

有效命中率 H_eff 与静态命中率 H_static 的关系为 H_eff = H_static * (1 - P_invalid) + H_dynamic_hit，其中 H_dynamic_hit 是更新后重新缓存并再次命中的概率，通常远小于 P_invalid，因此近似为 H_eff ≈ H_static * (1 - P_invalid)，'打折'系数即为 (1 - P_invalid)。

## Corrected Claim

有效命中率 H_eff 与静态命中率 H_static 的关系为 H_eff = H_static * (1 - P_invalid) + H_dynamic_hit，其中 H_dynamic_hit 是更新后重新缓存并再次命中的概率，通常远小于 P_invalid，因此近似为 H_eff ≈ H_static * (1 - P_invalid)，'打折'系数即为 (1 - P_invalid)。

## Evidence

父节点级核验未通过：不完备（子节点分别处理了公式中的两个不同项（P_invalid 和 H_dynamic_hit），逻辑上正且不冗余。但父节点的核心结论是近似关系 H_eff ≈ H_static * (1 - P_invalid)，其成立的依据是 'H_dynamic_hit 通常远小于 P_invalid'。子节点仅给出了 H_dynamic_hit 的定义/边界，却缺失了关于 '为何 H_dynamic_hit 可忽略' 或 'P_invalid 与 H_dynamic_hit 量级比较' 的关键论证/条件节点，导致对父节点近似逻辑的支撑不完备。）
