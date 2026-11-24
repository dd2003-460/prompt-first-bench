# N641: 公有云 CDN 长尾区域（用户距节点 100-300km）的 P99 RTT 基础值为 40ms，由光纤传播延迟 (0.05ms/km * 300km = 15

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N211

## Claim

公有云 CDN 长尾区域（用户距节点 100-300km）的 P99 RTT 基础值为 40ms，由光纤传播延迟 (0.05ms/km * 300km = 15ms) 和跨运营商骨干网路由延迟 (25ms) 组成。

## Corrected Claim

公有云 CDN 长尾区域（用户距节点 100-300km）的 P99 RTT 基础值为 40ms，由光纤传播延迟 (0.05ms/km * 300km = 15ms) 和跨运营商骨干网路由延迟 (25ms) 组成。

## Evidence

先验知识/题面给定，逻辑校验通过：光纤传播延迟计算正确（0.05ms/km * 300km = 15ms），总延迟15ms+25ms=40ms符合长尾区域P99 RTT的工程经验量级

## Search Query

long tail user CDN RTT backbone network delay breakdown
