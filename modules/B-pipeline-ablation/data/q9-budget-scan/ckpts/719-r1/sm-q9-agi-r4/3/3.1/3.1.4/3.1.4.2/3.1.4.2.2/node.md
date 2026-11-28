# N500: 工作点B（Pipeline Parallel混合）：若改用PP=2+TP=2，T_comm ≈ 0.32ms/step，但引入Pipeline Bubble O

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N179

## Claim

工作点B（Pipeline Parallel混合）：若改用PP=2+TP=2，T_comm ≈ 0.32ms/step，但引入Pipeline Bubble Overhead (~15% latency)；综合延迟可能高于纯TP=4，揭示TP/PP trade-off边界

## Corrected Claim

工作点B（Pipeline Parallel混合）：若改用PP=2+TP=2，T_comm ≈ 0.32ms/step，但引入Pipeline Bubble Overhead (~15% latency)；综合延迟可能高于纯TP=4，揭示TP/PP trade-off边界

## Evidence

先验知识/题面给定，逻辑校验通过：PP引入Bubble Overhead是已知特性，TP通信量随规模增加，两者权衡符合分布式训练基本原理。
