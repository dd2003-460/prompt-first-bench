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

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数（H_byte_LRU）下的数值实例，属于参数扫描而非正交分解；此外，'完备性'不足，因为缺少对 T_cold 估算逻辑（如 500 GB/s 吞吐假设、命中率与驻留时间的反比关系推导）的独立解释节点，仅给出结果而未覆盖模型假设的关键方面。）
