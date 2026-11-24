# N403: 长尾区域用户到POP的P99 RTT 计算值为 RTT_tail_P99 = 0.05 * 500 + 5 = 30ms（基于公式 RTT = 0.05*d +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

长尾区域用户到POP的P99 RTT 计算值为 RTT_tail_P99 = 0.05 * 500 + 5 = 30ms（基于公式 RTT = 0.05*d + 5）。

## Corrected Claim

长尾区域用户到POP的P99 RTT 计算值为 RTT_tail_P99 = 0.05 * 500 + 5 = 30ms（基于公式 RTT = 0.05*d + 5）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 RTT = 0.05*d + 5 代入 d=500 计算得 0.05*500 + 5 = 25 + 5 = 30ms，数值与量纲均正确。
