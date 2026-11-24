# N146: 在跨省用户（如北京用户访问广州POP，假设无更近POP）场景下，物理距离 d ≈ 1900 km，RTT 理论下限 = 2×1900km / (2×10^8 m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

在跨省用户（如北京用户访问广州POP，假设无更近POP）场景下，物理距离 d ≈ 1900 km，RTT 理论下限 = 2×1900km / (2×10^8 m/s) ≈ 19ms，代表高延迟/高带宽成本工作点。

## Corrected Claim

在跨省用户（如北京用户访问广州POP，假设无更近POP）场景下，物理距离 d ≈ 1900 km，RTT 理论下限 = 2×1900km / (2×10^8 m/s) ≈ 19ms，代表高延迟/高带宽成本工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：光速约3×10^8 m/s，光纤中光速约为2×10^8 m/s，1900km往返距离对应延迟约19ms，计算无误。

## Search Query

Beijing to Guangzhou distance km RTT calculation
