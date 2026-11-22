# N124: 工作点3（平均大小/基准失效）：当 s=E[s]≈11.1KB 时，p_invalid(s) = 0.01 * (1024/11340)^0.5 ≈ 0.003

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

工作点3（平均大小/基准失效）：当 s=E[s]≈11.1KB 时，p_invalid(s) = 0.01 * (1024/11340)^0.5 ≈ 0.0030 (0.3%)，且 cost_refill(s) = 5ms + 11.1KB/100MB/s ≈ 5.11ms，单位失效成本 cost_per_invalid = 0.0030 * 5.11ms ≈ 0.0153 ms/req，为全局最低成本工作点。

## Corrected Claim

工作点3（平均大小/基准失效）：当 s=E[s]≈11.1KB 时，p_invalid(s) = 0.01 * (1024/11340)^0.5 ≈ 0.0030 (0.3%)，且 cost_refill(s) = 5ms + 11.1KB/100MB/s ≈ 5.11ms，单位失效成本 cost_per_invalid = 0.0030 * 5.11ms ≈ 0.0153 ms/req，为全局最低成本工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（(1024/11340)^0.5 ≈ 0.3005, 0.01*0.3005=0.0030; 5+0.111=5.111ms; 0.0030*5.111≈0.0153ms），量纲与逻辑自洽。
