# N147: 在区域中心用户（如武汉用户访问武汉POP）场景下，物理距离 d ≈ 50-100 km，RTT 理论下限 ≈ 0.5-1ms，代表中等延迟/中等成本工作点，常用

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

在区域中心用户（如武汉用户访问武汉POP）场景下，物理距离 d ≈ 50-100 km，RTT 理论下限 ≈ 0.5-1ms，代表中等延迟/中等成本工作点，常用于验证 POP 覆盖密度对 P99 的影响。

## Corrected Claim

在区域中心用户（如武汉用户访问武汉POP）场景下，物理距离 d ≈ 50-100 km，RTT 理论下限 ≈ 0.5-1ms，代表中等延迟/中等成本工作点，常用于验证 POP 覆盖密度对 P99 的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：光速约300,000 km/s，50-100 km往返距离的理论延迟下限约为0.33-0.67 ms，加上处理开销后0.5-1 ms量级合理，符合物理直觉。

## Search Query

regional center user to local POP distance 50-100km RTT
