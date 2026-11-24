# N134: 长尾区域回源链路的光纤传输延迟计算：距离 1500km，RTT_min = 2 * 1500 / 200,000 = 15ms。考虑路由系数 1.3，实际 RT

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31, N32, N33

## Claim

长尾区域回源链路的光纤传输延迟计算：距离 1500km，RTT_min = 2 * 1500 / 200,000 = 15ms。考虑路由系数 1.3，实际 RTT ≈ 19.5ms。此值仅包含物理传输，不含 TCP/TLS 握手。

## Corrected Claim

长尾区域回源链路的光纤传输延迟计算：距离 1500km，RTT_min = 2 * 1500 / 200,000 = 15ms。考虑路由系数 1.3，实际 RTT ≈ 19.5ms。此值仅包含物理传输，不含 TCP/TLS 握手。

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为200,000 km/s，1500km单程延迟7.5ms，RTT 15ms，乘以路由系数1.3得19.5ms，计算无误且符合物理直觉。
