# N646: 工作点B（混合存储）的P99读取延迟 L_read_p99_C 取决于热点数据在SSD层的命中率 H_ssd_layer；若 H_ssd_layer ≥ 95%

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N216

## Claim

工作点B（混合存储）的P99读取延迟 L_read_p99_C 取决于热点数据在SSD层的命中率 H_ssd_layer；若 H_ssd_layer ≥ 95%，则 L_read_p99_C ≈ L_ssd_read (0.5ms)；若 H_ssd_layer < 95%，则 L_read_p99_C ≈ L_hdd_seek (5-10ms) + L_hdd_read (0.5ms)，需确保 H_ssd_layer 足够高以维持 <15ms 目标。

## Corrected Claim

工作点B（混合存储）的P99读取延迟 L_read_p99_C 取决于热点数据在SSD层的命中率 H_ssd_layer；若 H_ssd_layer ≥ 95%，则 L_read_p99_C ≈ L_ssd_read (0.5ms)；若 H_ssd_layer < 95%，则 L_read_p99_C ≈ L_hdd_seek (5-10ms) + L_hdd_read (0.5ms)，需确保 H_ssd_layer 足够高以维持 <15ms 目标。

## Evidence

先验知识/题面给定，逻辑校验通过
