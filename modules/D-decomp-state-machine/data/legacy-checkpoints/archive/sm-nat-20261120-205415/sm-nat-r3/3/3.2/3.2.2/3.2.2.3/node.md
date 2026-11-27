# N141: 工作点 B（中局部性/中对象）：假设 LRU 缓存对象平均大小接近全局平均 E[S]≈1MB，则 K_LRU ≈ 131,072 MB / 1 MB ≈ 131

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

工作点 B（中局部性/中对象）：假设 LRU 缓存对象平均大小接近全局平均 E[S]≈1MB，则 K_LRU ≈ 131,072 MB / 1 MB ≈ 131,072。此工作点代表无负相关修正时的基准性能。

## Corrected Claim

工作点 B（中局部性/中对象）：假设 LRU 缓存对象平均大小接近全局平均 E[S]≈1MB，则 K_LRU ≈ 131,072 MB / 1 MB ≈ 131,072。此工作点代表无负相关修正时的基准性能。

## Evidence

先验知识/题面给定，逻辑校验通过：131,072 MB / 1 MB = 131,072，计算正确且量纲一致。
