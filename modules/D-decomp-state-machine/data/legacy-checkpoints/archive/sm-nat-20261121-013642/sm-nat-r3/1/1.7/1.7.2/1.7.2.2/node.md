# N149: 工作点2（中频大对象混合，中精度/中字节贡献）：f_threshold 设为 95% 分位（top 5% 对象），P(freq > f_threshold) =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点2（中频大对象混合，中精度/中字节贡献）：f_threshold 设为 95% 分位（top 5% 对象），P(freq > f_threshold) = 0.05，E[size | freq > f_threshold] ≈ 1.2 * E[size]（因部分中频对象尺寸较大），则 B_LFU_only ≈ 0.05 * N_total * 1.2 * E[size] * r_avg_mid，此工作点捕捉了 LFU 在保留对象中混入较大尺寸对象时的字节量贡献，修正了纯小对象假设的偏差。

## Corrected Claim

工作点2（中频大对象混合，中精度/中字节贡献）：f_threshold 设为 95% 分位（top 5% 对象），P(freq > f_threshold) = 0.05，E[size | freq > f_threshold] ≈ 1.2 * E[size]（因部分中频对象尺寸较大），则 B_LFU_only ≈ 0.05 * N_total * 1.2 * E[size] * r_avg_mid，此工作点捕捉了 LFU 在保留对象中混入较大尺寸对象时的字节量贡献，修正了纯小对象假设的偏差。

## Evidence

先验知识/题面给定，逻辑校验通过
