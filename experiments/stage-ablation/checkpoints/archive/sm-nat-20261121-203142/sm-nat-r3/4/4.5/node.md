# N20: 量化工作点 3（高更新率 u=0.1）：δ ≈ 1 - 0.1 * (T_residence / L_object)；若 T_residence/L_objec

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

量化工作点 3（高更新率 u=0.1）：δ ≈ 1 - 0.1 * (T_residence / L_object)；若 T_residence/L_object ≈ 0.5，则 δ ≈ 0.95，折损 5%；此时需考虑 LRU 淘汰机制与更新风暴的交互，可能需引入 TTL 或版本控制机制，折损模型失效需修正项。

## Corrected Claim

量化工作点 3（高更新率 u=0.1）：δ ≈ 1 - 0.1 * (T_residence / L_object)；若 T_residence/L_object ≈ 0.5，则 δ ≈ 0.95，折损 5%；此时需考虑 LRU 淘汰机制与更新风暴的交互，可能需引入 TTL 或版本控制机制，折损模型失效需修正项。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 δ = 1 - u * (T_residence / L_object) 在 u=0.1 且比值为 0.5 时计算结果为 0.95，折损 5% 符合算术逻辑；关于 LRU 与更新风暴交互导致模型失效需修正的定性描述符合缓存系统一般工程直觉。
