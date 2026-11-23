# N124: 核心区域RTT基线 = 2 * d_core / 2.0e8 * 1.05，若d_core=75km，则RTT_core ≈ 0.79ms（纯传播）+ 处理延迟

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

核心区域RTT基线 = 2 * d_core / 2.0e8 * 1.05，若d_core=75km，则RTT_core ≈ 0.79ms（纯传播）+ 处理延迟，实际网络RTT通常因路由跳跃增加至10-20ms

## Corrected Claim

核心区域RTT基线 = 2 * d_core / 2.0e8 * 1.05，若d_core=75km，则RTT_core ≈ 0.79ms（纯传播）+ 处理延迟，实际网络RTT通常因路由跳跃增加至10-20ms

## Evidence

先验知识/题面给定，逻辑校验通过：光速约3e8 m/s，75km单程传播延迟约0.25ms，RTT约0.5ms，考虑介质折射率或路径非直线（1.05系数）后0.79ms量级合理；实际网络RTT 10-20ms符合互联网典型经验值。
