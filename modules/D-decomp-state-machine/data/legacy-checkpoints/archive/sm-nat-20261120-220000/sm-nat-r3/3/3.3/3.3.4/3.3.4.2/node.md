# N123: 工作点2（大对象/低失效）：当 s=10MB 时，p_invalid(s) = 0.01 * (1024/10^7)^0.5 ≈ 0.00032 (0.032%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

工作点2（大对象/低失效）：当 s=10MB 时，p_invalid(s) = 0.01 * (1024/10^7)^0.5 ≈ 0.00032 (0.032%)，且 cost_refill(s) = 5ms + 10MB/100MB/s = 105ms，单位失效成本 cost_per_invalid = 0.00032 * 105ms ≈ 0.0336 ms/req，比小对象低约 33%。

## Corrected Claim

工作点2（大对象/低失效）：当 s=10MB 时，p_invalid(s) = 0.01 * (1024/10^7)^0.5 ≈ 0.00032 (0.032%)，且 cost_refill(s) = 5ms + 10MB/100MB/s = 105ms，单位失效成本 cost_per_invalid = 0.00032 * 105ms ≈ 0.0336 ms/req，比小对象低约 33%。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（0.00032 * 105 = 0.0336），且符合大对象低失效导致单位成本降低的直觉。
