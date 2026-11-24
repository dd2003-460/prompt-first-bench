# N186: 无 BGP 接入时的跨网延迟惩罚 ΔT_cross (ms)：当用户运营商与 POP 接入运营商不一致时，P99 延迟增加 ΔT_cross ≈ 15-25ms

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

无 BGP 接入时的跨网延迟惩罚 ΔT_cross (ms)：当用户运营商与 POP 接入运营商不一致时，P99 延迟增加 ΔT_cross ≈ 15-25ms，需纳入 P99_self 的计算。

## Corrected Claim

无 BGP 接入时的跨网延迟惩罚 ΔT_cross (ms)：当用户运营商与 POP 接入运营商不一致时，P99 延迟增加 ΔT_cross ≈ 15-25ms，需纳入 P99_self 的计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN POP cross-ISP latency penalty ms
