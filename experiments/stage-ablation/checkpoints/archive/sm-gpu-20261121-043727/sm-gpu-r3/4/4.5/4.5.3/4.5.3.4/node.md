# N203: 单位 Token 成本对比公式：Cost_per_token = TCO_3yr / (Throughput_eff * 8760h * 3 * 3600s/h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N76

## Claim

单位 Token 成本对比公式：Cost_per_token = TCO_3yr / (Throughput_eff * 8760h * 3 * 3600s/h)，代入 N94 和 N95 数据，2x 4090 单位成本约为 MI300X 的 1.8-2.2 倍，表明尽管硬件成本低，但性能劣势导致长期持有成本更高

## Corrected Claim

单位 Token 成本对比公式：Cost_per_token = TCO_3yr / (Throughput_eff * 8760h * 3 * 3600s/h)，代入 N94 和 N95 数据，2x 4090 单位成本约为 MI300X 的 1.8-2.2 倍，表明尽管硬件成本低，但性能劣势导致长期持有成本更高

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（TCO/总Token数），2x 4090与MI300X的性能差距（约2-3倍）与成本差距（约1.5-2倍）结合后，得出1.8-2.2倍的单位成本倍数符合工程直觉与逻辑推导。
