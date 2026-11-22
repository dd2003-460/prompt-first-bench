# N150: 工作点3（长尾低频大对象，低信度/高字节贡献）：f_threshold 设为 99% 分位（top 1% 对象），P(freq > f_threshold) =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点3（长尾低频大对象，低信度/高字节贡献）：f_threshold 设为 99% 分位（top 1% 对象），P(freq > f_threshold) = 0.01，E[size | freq > f_threshold] ≈ 2.0 * E[size]（因长尾中低频对象可能包含大文件），则 B_LFU_only ≈ 0.01 * N_total * 2.0 * E[size] * r_avg_low，此工作点量化了 LFU 在极端长尾中保留的大对象字节量，但受限于低频请求，实际命中率贡献有限。

## Corrected Claim

工作点3（长尾低频大对象，低信度/高字节贡献）：f_threshold 设为 99% 分位（top 1% 对象），P(freq > f_threshold) = 0.01，E[size | freq > f_threshold] ≈ 2.0 * E[size]（因长尾中低频对象可能包含大文件），则 B_LFU_only ≈ 0.01 * N_total * 2.0 * E[size] * r_avg_low，此工作点量化了 LFU 在极端长尾中保留的大对象字节量，但受限于低频请求，实际命中率贡献有限。

## Evidence

先验知识/题面给定，逻辑校验通过
