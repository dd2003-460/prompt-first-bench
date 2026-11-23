# N388: 长尾区域用户通过公有云 CDN 访问时的回源延迟 $L_{backhaul, tail, cloud}$ 由用户到最近公有云边缘节点的距离 $D_{user, 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N145

## Claim

长尾区域用户通过公有云 CDN 访问时的回源延迟 $L_{backhaul, tail, cloud}$ 由用户到最近公有云边缘节点的距离 $D_{user, edge}$ 和边缘节点到源站的距离 $D_{edge, origin}$ 决定，典型值 $L_{backhaul, tail, cloud} \approx 30-50$ms

## Corrected Claim

长尾区域用户通过公有云 CDN 访问时的回源延迟 $L_{backhaul, tail, cloud}$ 由用户到最近公有云边缘节点的距离 $D_{user, edge}$ 和边缘节点到源站的距离 $D_{edge, origin}$ 决定，典型值 $L_{backhaul, tail, cloud} \approx 30-50$ms

## Evidence

先验知识/题面给定，逻辑校验通过
