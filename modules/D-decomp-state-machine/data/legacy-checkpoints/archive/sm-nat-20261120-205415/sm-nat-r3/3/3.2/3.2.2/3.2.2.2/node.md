# N140: 工作点 A（高局部性/小对象）：假设 LRU 缓存对象平均大小 E[S|T≥T_th] ≈ 0.8MB（因负相关，近期访问对象偏小），则 K_LRU ≈ 131

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

工作点 A（高局部性/小对象）：假设 LRU 缓存对象平均大小 E[S|T≥T_th] ≈ 0.8MB（因负相关，近期访问对象偏小），则 K_LRU ≈ 131,072 MB / 0.8 MB ≈ 163,840。此工作点代表 LRU 在负相关下的最优性能边界。

## Corrected Claim

工作点 A（高局部性/小对象）：假设 LRU 缓存对象平均大小 E[S|T≥T_th] ≈ 0.8MB（因负相关，近期访问对象偏小），则 K_LRU ≈ 131,072 MB / 0.8 MB ≈ 163,840。此工作点代表 LRU 在负相关下的最优性能边界。

## Evidence

先验知识/题面给定，逻辑校验通过：131,072 / 0.8 = 163,840，计算准确，量级合理。
