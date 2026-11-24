# N636: 长尾区域 RTT 的修正值：基于修正后的距离 d_p99_tail = 400km，代入公式 RTT = 0.05*400 + 5 = 25ms，相比原估算 4

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N209

## Claim

长尾区域 RTT 的修正值：基于修正后的距离 d_p99_tail = 400km，代入公式 RTT = 0.05*400 + 5 = 25ms，相比原估算 40ms 降低 15ms，反映长尾区域虽节点稀疏但非极端偏远，P99 延迟更可控。

## Corrected Claim

长尾区域 RTT 的修正值：基于修正后的距离 d_p99_tail = 400km，代入公式 RTT = 0.05*400 + 5 = 25ms，相比原估算 40ms 降低 15ms，反映长尾区域虽节点稀疏但非极端偏远，P99 延迟更可控。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 RTT = 0.05*400 + 5 计算结果为 25ms，与陈述一致；25ms 相比 40ms 降低 15ms，数值逻辑自洽。

## Search Query

CDN RTT calculation 400km distance fiber latency
