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

先验知识/题面给定，逻辑校验通过
