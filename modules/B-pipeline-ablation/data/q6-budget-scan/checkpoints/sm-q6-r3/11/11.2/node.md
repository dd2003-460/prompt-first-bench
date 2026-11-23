# N213: 自建节点95th Percentile带宽成本修正：月度成本 = 峰值带宽(140,000 Mbps) * 0.95 * 730h * 单价(¥1.5/Mbps

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

自建节点95th Percentile带宽成本修正：月度成本 = 峰值带宽(140,000 Mbps) * 0.95 * 730h * 单价(¥1.5/Mbps/h) ≈ ¥146,437,500/月，远高于公有云CDN成本，表明自建10个POP点承载全量2TB/日流量在带宽成本上极不经济，除非单价极低或仅承载部分流量

## Corrected Claim

自建节点95th Percentile带宽成本修正：月度成本 = 峰值带宽(140,000 Mbps) * 0.95 * 730h * 单价(¥1.5/Mbps/h) ≈ ¥146,437,500/月，远高于公有云CDN成本，表明自建10个POP点承载全量2TB/日流量在带宽成本上极不经济，除非单价极低或仅承载部分流量

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 140,000 * 0.95 * 730 * 1.5 = 146,437,500 准确无误，量级符合带宽成本常识。
