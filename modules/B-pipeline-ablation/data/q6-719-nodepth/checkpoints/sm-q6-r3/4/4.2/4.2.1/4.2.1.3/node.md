# N335: 因IP地理映射错误导致的P99延迟惩罚项 C_geo_error (ms) = (1 - A_geo) * P99_RTT_penalty，其中 P99_RTT

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

因IP地理映射错误导致的P99延迟惩罚项 C_geo_error (ms) = (1 - A_geo) * P99_RTT_penalty，其中 P99_RTT_penalty 为被调度至次优POP（距离增加 >100km）时的P99 RTT增量，典型值为 10-25ms。

## Corrected Claim

因IP地理映射错误导致的P99延迟惩罚项 C_geo_error (ms) = (1 - A_geo) * P99_RTT_penalty，其中 P99_RTT_penalty 为被调度至次优POP（距离增加 >100km）时的P99 RTT增量，典型值为 10-25ms。

## Evidence

先验知识/题面给定，逻辑校验通过
