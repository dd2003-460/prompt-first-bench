# N142: 工作点 C（低局部性/大对象）：假设 LRU 缓存对象平均大小 E[S|T≥T_th] ≈ 1.5MB（因时间局部性可能包含较大对象），则 K_LRU ≈ 13

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

工作点 C（低局部性/大对象）：假设 LRU 缓存对象平均大小 E[S|T≥T_th] ≈ 1.5MB（因时间局部性可能包含较大对象），则 K_LRU ≈ 131,072 MB / 1.5 MB ≈ 87,381。此工作点代表 LRU 在极端情况下的性能下限。

## Corrected Claim

工作点 C（低局部性/大对象）：假设 LRU 缓存对象平均大小 E[S|T≥T_th] ≈ 1.5MB（因时间局部性可能包含较大对象），则 K_LRU ≈ 131,072 MB / 1.5 MB ≈ 87,381。此工作点代表 LRU 在极端情况下的性能下限。

## Evidence

先验知识/题面给定，逻辑校验通过：131,072 / 1.5 ≈ 87,381.33，数值计算正确，量级合理，符合LRU缓存容量与对象大小关系的定义。
