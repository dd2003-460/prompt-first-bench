# N137: 工作点 B（中频率/中对象）：假设 LFU 缓存对象平均大小接近全局平均 E[S]≈1MB，则 K_LFU ≈ 131,072 MB / 1 MB ≈ 131,

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点 B（中频率/中对象）：假设 LFU 缓存对象平均大小接近全局平均 E[S]≈1MB，则 K_LFU ≈ 131,072 MB / 1 MB ≈ 131,072。此工作点代表无负相关修正时的基准性能，用于对比 ρ=-0.3 带来的增益。

## Corrected Claim

工作点 B（中频率/中对象）：假设 LFU 缓存对象平均大小接近全局平均 E[S]≈1MB，则 K_LFU ≈ 131,072 MB / 1 MB ≈ 131,072。此工作点代表无负相关修正时的基准性能，用于对比 ρ=-0.3 带来的增益。

## Evidence

先验知识/题面给定，逻辑校验通过：131,072 MB / 1 MB = 131,072，计算无误，量纲一致，符合LFU缓存容量估算的基本逻辑。
