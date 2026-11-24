# N199: 策略选择的帕累托前沿临界点：当 P99 目标 T < 80ms 时，仅全自建 POP 策略能稳定达标（成本最高）；当 80ms <= T < 150ms 时，混

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

策略选择的帕累托前沿临界点：当 P99 目标 T < 80ms 时，仅全自建 POP 策略能稳定达标（成本最高）；当 80ms <= T < 150ms 时，混合策略在成本-延迟权衡上通常优于全公有云（因核心区域自建降低了长尾回源概率）；当 T >= 150ms 时，全公有云 CDN 因规模效应和免运维特性通常总成本最低。

## Corrected Claim

策略选择的帕累托前沿临界点：当 P99 目标 T < 80ms 时，仅全自建 POP 策略能稳定达标（成本最高）；当 80ms <= T < 150ms 时，混合策略在成本-延迟权衡上通常优于全公有云（因核心区域自建降低了长尾回源概率）；当 T >= 150ms 时，全公有云 CDN 因规模效应和免运维特性通常总成本最低。

## Evidence

检索失败: no sources from any channel (all 5 failed)
