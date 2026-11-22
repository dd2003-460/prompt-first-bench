# N15: 稳态陈旧对象占比 C_steady = 1 - exp(-λ_u * T_cold)，其中 λ_u=0.01/day，T_cold 为 LRU 缓存中对象的平均

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

稳态陈旧对象占比 C_steady = 1 - exp(-λ_u * T_cold)，其中 λ_u=0.01/day，T_cold 为 LRU 缓存中对象的平均驻留时间（由缓存容量 128GB 和访问频率决定）

## Corrected Claim

稳态陈旧对象占比 C_steady = 1 - exp(-λ_u * T_cold)，其中 λ_u=0.01/day，T_cold 为 LRU 缓存中对象的平均驻留时间（由缓存容量 128GB 和访问频率决定）

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上是正交的（分别对应高、中、低命中率三个不同场景），且覆盖了父节点公式在不同参数下的应用，具备完备性。然而，这三个子节点本质上是同一个数学公式在三个不同参数值下的具体计算实例，属于典型的“参数扫描”或“案例枚举”，而非结构性分解。它们共享相同的计算逻辑和变量定义，仅数值不同，因此存在高度冗余。）
