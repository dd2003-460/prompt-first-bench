# N148: 在单跳光纤链路（距离 d=100km）场景下，使用修正光速 c_fiber=2×10^8 m/s 计算单向延迟为 100km / (2×10^8 m/s) = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

在单跳光纤链路（距离 d=100km）场景下，使用修正光速 c_fiber=2×10^8 m/s 计算单向延迟为 100km / (2×10^8 m/s) = 0.5ms，若错误使用真空光速 3×10^8 m/s 则为 0.33ms，误差导致 RTT 低估 33%，影响 P99 延迟预算精度。

## Corrected Claim

在单跳光纤链路（距离 d=100km）场景下，使用修正光速 c_fiber=2×10^8 m/s 计算单向延迟为 100km / (2×10^8 m/s) = 0.5ms，若错误使用真空光速 3×10^8 m/s 则为 0.33ms，误差导致 RTT 低估 33%，影响 P99 延迟预算精度。

## Evidence

先验知识/题面给定，逻辑校验通过：100km/(2e8 m/s)=0.5ms，100km/(3e8 m/s)≈0.333ms，(0.5-0.333)/0.5≈33.3%，计算与物理常识一致。

## Search Query

fiber optic light speed 2e8 m/s vs vacuum speed latency error
