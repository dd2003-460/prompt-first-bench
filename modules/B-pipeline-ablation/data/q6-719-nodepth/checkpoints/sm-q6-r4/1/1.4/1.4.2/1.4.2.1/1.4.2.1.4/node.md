# N707: 工作点1下公有云CDN的P99延迟敏感性分析：若 RTT_user_edge_tail_p99 从 40ms 增至 50ms（长尾区域距离增加），P99_tai

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N233

## Claim

工作点1下公有云CDN的P99延迟敏感性分析：若 RTT_user_edge_tail_p99 从 40ms 增至 50ms（长尾区域距离增加），P99_tail 从 46ms 增至 56ms，仍满足 T=100ms，无额外成本影响。

## Corrected Claim

工作点1下公有云CDN的P99延迟敏感性分析：若 RTT_user_edge_tail_p99 从 40ms 增至 50ms（长尾区域距离增加），P99_tail 从 46ms 增至 56ms，仍满足 T=100ms，无额外成本影响。

## Evidence

先验知识/题面给定，逻辑校验通过：P99延迟增加10ms后为56ms，仍小于100ms阈值，且未提及成本变化，逻辑自洽。
