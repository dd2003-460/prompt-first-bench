# N84: LRU平均驻留时间 λ 的估算公式：λ = C / (D * (1 - H_base))，其中 C 为缓存容量(128GB)，D 为每日总请求字节数(5000万

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

LRU平均驻留时间 λ 的估算公式：λ = C / (D * (1 - H_base))，其中 C 为缓存容量(128GB)，D 为每日总请求字节数(5000万 * 1MB = 50PB)，H_base 为稳态基础命中率(0.78)。

## Corrected Claim

LRU平均驻留时间 λ 的估算公式：λ = C / (D * (1 - H_base))，其中 C 为缓存容量(128GB)，D 为每日总请求字节数(5000万 * 1MB = 50PB)，H_base 为稳态基础命中率(0.78)。

## Evidence

先验知识/题面给定，逻辑校验通过
