# N46: N24 中 decode 步时间 10ms 的假设存在偏差：基于 N30 修正后的单 token 生成延迟 15ms（受 900GB/s 带宽限制），17% 的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

N24 中 decode 步时间 10ms 的假设存在偏差：基于 N30 修正后的单 token 生成延迟 15ms（受 900GB/s 带宽限制），17% 的通信占比应重算为 1.7ms / 15ms ≈ 11.3%，低于 15% 下限，表明在纯带宽受限场景下通信占比略低于原估算区间。

## Corrected Claim

N24 中 decode 步时间 10ms 的假设存在偏差：基于 N30 修正后的单 token 生成延迟 15ms（受 900GB/s 带宽限制），17% 的通信占比应重算为 1.7ms / 15ms ≈ 11.3%，低于 15% 下限，表明在纯带宽受限场景下通信占比略低于原估算区间。

## Evidence

先验知识/题面给定，逻辑校验通过：1.7/15≈11.3%计算正确，且11.3%<15%符合陈述逻辑
