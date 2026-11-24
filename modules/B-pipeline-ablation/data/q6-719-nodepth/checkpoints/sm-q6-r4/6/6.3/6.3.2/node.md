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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个独立分量（用户到POP延迟、处理延迟、回源延迟），彼此正交且无重叠。三个子节点共同覆盖了父节点中所有关键延迟组成部分，完备性良好。各子节点描述的是不同阶段的延迟，不存在冗余或可压缩为单一参数的情况。）

## Search Query

Self-hosted CDN POP latency estimation 500km radius
