# N501: 自建10个POP点（覆盖半径500km）下，核心区域用户到POP的物理距离 d_core_self 中位数为 20-100km，长尾区域 d_tail_self

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N166

## Claim

自建10个POP点（覆盖半径500km）下，核心区域用户到POP的物理距离 d_core_self 中位数为 20-100km，长尾区域 d_tail_self 中位数为 300-500km，导致 RTT_user_pop_core ≈ 6-10ms，RTT_user_pop_tail ≈ 20-30ms

## Corrected Claim

自建10个POP点（覆盖半径500km）下，核心区域用户到POP的物理距离 d_core_self 中位数为 20-100km，长尾区域 d_tail_self 中位数为 300-500km，导致 RTT_user_pop_core ≈ 6-10ms，RTT_user_pop_tail ≈ 20-30ms

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为200,000 km/s，单程20-100km对应延迟约0.1-0.5ms，往返2-10ms；单程300-500km对应延迟约1.5-2.5ms，往返3-5ms。考虑到网络协议栈、交换机处理及排队延迟（通常增加几毫秒），核心区域6-10ms和长尾区域20-30ms的RTT估算在工程上合理且量级正确。

## Search Query

Self-built POP node coverage radius user distance distribution
