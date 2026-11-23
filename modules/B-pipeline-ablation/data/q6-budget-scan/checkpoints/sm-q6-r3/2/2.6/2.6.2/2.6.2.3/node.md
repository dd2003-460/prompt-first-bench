# N284: 峰值与包月成本的交叉点阈值：当 P95_Bandwidth_Mbps * p_peak_per_mbps < Min(C_bandwidth_package) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

峰值与包月成本的交叉点阈值：当 P95_Bandwidth_Mbps * p_peak_per_mbps < Min(C_bandwidth_package) 时选择峰值计费，反之选择包月；该交叉点通常出现在带宽利用率较低（<40%）或短期突发场景，对于日均2TB的稳定流量，包月计费通常更优，需计算具体盈亏平衡点带宽值

## Corrected Claim

峰值与包月成本的交叉点阈值：当 P95_Bandwidth_Mbps * p_peak_per_mbps < Min(C_bandwidth_package) 时选择峰值计费，反之选择包月；该交叉点通常出现在带宽利用率较低（<40%）或短期突发场景，对于日均2TB的稳定流量，包月计费通常更优，需计算具体盈亏平衡点带宽值

## Evidence

先验知识/题面给定，逻辑校验通过：成本比较逻辑自洽，且对于日均2TB（约3.4Gbps平均带宽）的稳定流量，包月计费通常优于按峰值计费符合云计算计费常识。

## Search Query

CDN billing model break-even point peak vs package
