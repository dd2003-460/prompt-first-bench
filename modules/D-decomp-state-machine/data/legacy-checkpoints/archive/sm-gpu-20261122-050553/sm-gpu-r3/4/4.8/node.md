# N27: 延迟特性 (Latency) = Time_to_First_Token (TTFT) + Time_per_Subsequent_Token (TSTT)；虽

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

延迟特性 (Latency) = Time_to_First_Token (TTFT) + Time_per_Subsequent_Token (TSTT)；虽非硬约束，但 TSTT 影响用户感知流畅度，需在 TCO 相近时作为次级排序键（如 TTFT < 1s, TSTT < 50ms 为良好）。

## Corrected Claim

延迟特性 (Latency) = Time_to_First_Token (TTFT) + Time_per_Subsequent_Token (TSTT)；虽非硬约束，但 TSTT 影响用户感知流畅度，需在 TCO 相近时作为次级排序键（如 TTFT < 1s, TSTT < 50ms 为良好）。

## Evidence

先验知识/题面给定，逻辑校验通过
