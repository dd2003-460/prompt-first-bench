# N19: LRU 稳态缓存驻留对象的大小阈值 S_threshold：由缓存容量 C=128GB 和对象访问频率决定，S_threshold = C / (Σ_{i in

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

LRU 稳态缓存驻留对象的大小阈值 S_threshold：由缓存容量 C=128GB 和对象访问频率决定，S_threshold = C / (Σ_{i in cache} f_i)，需通过求解 ∫_{x_min}^{S_threshold} f(x) * S(x) dx = C 得到具体数值。

## Corrected Claim

LRU 稳态缓存驻留对象的大小阈值 S_threshold：由缓存容量 C=128GB 和对象访问频率决定，S_threshold = C / (Σ_{i in cache} f_i)，需通过求解 ∫_{x_min}^{S_threshold} f(x) * S(x) dx = C 得到具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过
