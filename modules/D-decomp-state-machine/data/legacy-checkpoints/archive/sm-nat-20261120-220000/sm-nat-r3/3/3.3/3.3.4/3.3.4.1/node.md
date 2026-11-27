# N122: 工作点1（小对象/高失效）：当 s=1KB 时，p_invalid(s) = 0.01 * (1024/1024)^0.5 = 0.01 (1%)，且 cost

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

工作点1（小对象/高失效）：当 s=1KB 时，p_invalid(s) = 0.01 * (1024/1024)^0.5 = 0.01 (1%)，且 cost_refill(s) = 5ms + 1KB/100MB/s ≈ 5.01ms，单位失效成本 cost_per_invalid = 0.01 * 5.01ms = 0.0501 ms/req。

## Corrected Claim

工作点1（小对象/高失效）：当 s=1KB 时，p_invalid(s) = 0.01 * (1024/1024)^0.5 = 0.01 (1%)，且 cost_refill(s) = 5ms + 1KB/100MB/s ≈ 5.01ms，单位失效成本 cost_per_invalid = 0.01 * 5.01ms = 0.0501 ms/req。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（1KB/100MB/s ≈ 0.01ms，5+0.01=5.01ms，0.01*5.01=0.0501ms），量纲与逻辑自洽。
