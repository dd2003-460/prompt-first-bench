# N16: LRU 平均驻留时间 T_cold 的近似表达式：T_cold ≈ (C_cache / R_bytes) * (1 / (1 - H_byte_LRU))，其

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LRU 平均驻留时间 T_cold 的近似表达式：T_cold ≈ (C_cache / R_bytes) * (1 / (1 - H_byte_LRU))，其中 C_cache=128GB，R_bytes 为总字节请求率，H_byte_LRU 为字节命中率

## Corrected Claim

LRU 平均驻留时间 T_cold 的近似表达式：T_cold ≈ (C_cache / R_bytes) * (1 / (1 - H_byte_LRU))，其中 C_cache=128GB，R_bytes 为总字节请求率，H_byte_LRU 为字节命中率

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的两个独立变量 R_bytes 和 H_byte_LRU，两者定义域不同（流量 vs 命中率），无重叠或矛盾。公式中第三个参数 C_cache 已在父节点中明确为固定值 128GB，无需作为独立子节点分解。因此分解覆盖了公式的所有动态/可变组成部分，且无冗余。）
