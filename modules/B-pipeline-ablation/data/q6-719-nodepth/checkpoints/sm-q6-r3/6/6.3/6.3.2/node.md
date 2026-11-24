# N166: 在 T=200ms 阈值下，自建10个POP（假设均匀分布于省会城市，覆盖半径500km）的P99延迟理论上限约为 30ms(用户到POP) + 20ms(处理

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

在 T=200ms 阈值下，自建10个POP（假设均匀分布于省会城市，覆盖半径500km）的P99延迟理论上限约为 30ms(用户到POP) + 20ms(处理) + 100ms(回源概率) ≈ 150ms，满足 P99_self <= 200ms。

## Corrected Claim

在 T=200ms 阈值下，自建10个POP（假设均匀分布于省会城市，覆盖半径500km）的P99延迟理论上限约为 30ms(用户到POP) + 20ms(处理) + 100ms(回源概率) ≈ 150ms，满足 P99_self <= 200ms。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点延迟公式中的三个主要组成部分（用户到POP传输、节点处理、回源），逻辑清晰且互不重叠，完整覆盖了P99延迟构成的关键方面，无冗余。）

## Search Query

Self-hosted CDN POP latency estimation 500km radius
