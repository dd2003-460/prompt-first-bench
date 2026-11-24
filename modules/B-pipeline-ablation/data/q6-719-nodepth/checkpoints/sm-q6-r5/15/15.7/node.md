# N415: 西部长尾延迟对 P99 合规性的影响量化：若 T = 100 ms，纯自建方案下 L_p99_self = max(L_p99_east, L_p99_tail

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

西部长尾延迟对 P99 合规性的影响量化：若 T = 100 ms，纯自建方案下 L_p99_self = max(L_p99_east, L_p99_tail)，其中 L_p99_tail ≈ 7.5 + 45 + 20*(1-0.75) = 58.75 ms（假设 L_backhaul_tail=20ms, H_tail=0.75），满足 T；但若 T = 50 ms，则不满足，需引入公有云兜底使 L_p99_tail 降至 35-40 ms。

## Corrected Claim

西部长尾延迟对 P99 合规性的影响量化：若 T = 100 ms，纯自建方案下 L_p99_self = max(L_p99_east, L_p99_tail)，其中 L_p99_tail ≈ 7.5 + 45 + 20*(1-0.75) = 58.75 ms（假设 L_backhaul_tail=20ms, H_tail=0.75），满足 T；但若 T = 50 ms，则不满足，需引入公有云兜底使 L_p99_tail 降至 35-40 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 7.5+45+20*(1-0.75)=58.75 正确，且 58.75 < 100 满足 T=100ms 条件，58.75 > 50 不满足 T=50ms 条件，逻辑自洽。
