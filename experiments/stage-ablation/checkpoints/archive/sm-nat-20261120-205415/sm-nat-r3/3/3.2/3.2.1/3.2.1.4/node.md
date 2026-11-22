# N138: 工作点 C（低频率/大对象）：假设 LFU 因更新率或异常负载缓存了较大对象，平均大小 E[S|H≥H_th] ≈ 2MB，则 K_LFU ≈ 131,072 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点 C（低频率/大对象）：假设 LFU 因更新率或异常负载缓存了较大对象，平均大小 E[S|H≥H_th] ≈ 2MB，则 K_LFU ≈ 131,072 MB / 2 MB ≈ 65,536。此工作点代表 LFU 在极端情况下的性能下限，用于评估最坏情况下的命中率。

## Corrected Claim

工作点 C（低频率/大对象）：假设 LFU 因更新率或异常负载缓存了较大对象，平均大小 E[S|H≥H_th] ≈ 2MB，则 K_LFU ≈ 131,072 MB / 2 MB ≈ 65,536。此工作点代表 LFU 在极端情况下的性能下限，用于评估最坏情况下的命中率。

## Evidence

先验知识/题面给定，逻辑校验通过：131,072 MB / 2 MB = 65,536，计算准确，量纲一致，符合缓存容量与对象大小决定最大缓存对象数量的基本逻辑。
