# N109: 自建POP点弹性不足导致的过载丢弃率 D_overload = max(0, (Actual_Traffic - Preprovisioned_Capacity

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

自建POP点弹性不足导致的过载丢弃率 D_overload = max(0, (Actual_Traffic - Preprovisioned_Capacity) / Preprovisioned_Capacity)，当流量突增超过 2x 峰值时 D_overload > 0，对应 P99 延迟无限大（请求失败），需计入成本惩罚项

## Corrected Claim

自建POP点弹性不足导致的过载丢弃率 D_overload = max(0, (Actual_Traffic - Preprovisioned_Capacity) / Preprovisioned_Capacity)，当流量突增超过 2x 峰值时 D_overload > 0，对应 P99 延迟无限大（请求失败），需计入成本惩罚项

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

edge node overload drop rate P99 latency infinite
