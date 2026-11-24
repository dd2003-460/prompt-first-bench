# N42: 敏感性分析中，P99 目标值 T 的变动对策略选择的影响：当 T 从 200ms 降至 150ms 时，公有云CDN的 P99_public 可能超标，而自建P

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

敏感性分析中，P99 目标值 T 的变动对策略选择的影响：当 T 从 200ms 降至 150ms 时，公有云CDN的 P99_public 可能超标，而自建POP的 P99_self 因 RTT 更低而更可能达标，导致策略从公有云转向自建或混合。

## Corrected Claim

敏感性分析中，P99 目标值 T 的变动对策略选择的影响：当 T 从 200ms 降至 150ms 时，公有云CDN的 P99_public 可能超标，而自建POP的 P99_self 因 RTT 更低而更可能达标，导致策略从公有云转向自建或混合。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 705)
