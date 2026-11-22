# N14: 更新率对 LRU 的额外折损：当对象更新时，LRU 需重新加载，命中率折损 = λ_update * S_obj / (S_obj + S_miss_penal

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

更新率对 LRU 的额外折损：当对象更新时，LRU 需重新加载，命中率折损 = λ_update * S_obj / (S_obj + S_miss_penalty)，S_obj 为对象大小，S_miss_penalty 为未命中惩罚（如回源延迟折算的字节数）；λ_update = 0.01/天，S_obj ≈ 11.1KB，S_miss_penalty ≈ 100KB，折损 ≈ 0.01 * 11.1 / 111.1 ≈ 0.01%

## Corrected Claim

更新率对 LRU 的额外折损：当对象更新时，LRU 需重新加载，命中率折损 = λ_update * S_obj / (S_obj + S_miss_penalty)，S_obj 为对象大小，S_miss_penalty 为未命中惩罚（如回源延迟折算的字节数）；λ_update = 0.01/天，S_obj ≈ 11.1KB，S_miss_penalty ≈ 100KB，折损 ≈ 0.01 * 11.1 / 111.1 ≈ 0.01%

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合LRU更新导致缓存失效的直觉（更新率乘以对象占比），数值计算 0.01 * 11.1 / (11.1 + 100) ≈ 0.000999 ≈ 0.01% 准确无误，量纲与量级合理。
