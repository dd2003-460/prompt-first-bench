# N581: 平均连接延迟计算中的 RTT 基准值：对于 C 端用户，国内主流运营商的 P50 RTT 约为 20-40ms，P99 RTT 约为 80-150ms，因此 2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N199

## Claim

平均连接延迟计算中的 RTT 基准值：对于 C 端用户，国内主流运营商的 P50 RTT 约为 20-40ms，P99 RTT 约为 80-150ms，因此 2.2 RTT 的平均连接延迟在 P50 下约为 44-88ms，在 P99 下约为 176-330ms

## Corrected Claim

平均连接延迟计算中的 RTT 基准值：对于 C 端用户，国内主流运营商的 P50 RTT 约为 20-40ms，P99 RTT 约为 80-150ms，因此 2.2 RTT 的平均连接延迟在 P50 下约为 44-88ms，在 P99 下约为 176-330ms

## Evidence

先验知识/题面给定，逻辑校验通过：2.2 RTT 的计算逻辑正确（2.2 * 20-40ms = 44-88ms; 2.2 * 80-150ms = 176-330ms），且国内主流运营商 P50/P99 RTT 数值符合工程经验常识。
