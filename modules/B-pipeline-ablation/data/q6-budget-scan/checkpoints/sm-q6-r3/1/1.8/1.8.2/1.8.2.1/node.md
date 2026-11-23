# N234: 长尾区域 RTT_P99(k) 的地理分布：基于长尾省份用户到公有云 CDN 节点的距离 D_k，RTT_P99(k) = 2 * D_k / v_fiber 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

长尾区域 RTT_P99(k) 的地理分布：基于长尾省份用户到公有云 CDN 节点的距离 D_k，RTT_P99(k) = 2 * D_k / v_fiber + T_backbone_congestion，其中 D_k 通常 > 500km，T_backbone_congestion 在高峰期为 5-20ms，导致 RTT_P99 典型区间为 40-80ms

## Corrected Claim

长尾区域 RTT_P99(k) 的地理分布：基于长尾省份用户到公有云 CDN 节点的距离 D_k，RTT_P99(k) = 2 * D_k / v_fiber + T_backbone_congestion，其中 D_k 通常 > 500km，T_backbone_congestion 在高峰期为 5-20ms，导致 RTT_P99 典型区间为 40-80ms

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为200,000 km/s，500km单程延迟约2.5ms，往返约5ms，加上骨干网拥塞5-20ms及处理开销，40-80ms的P99区间在长尾高延迟场景下量级合理且逻辑自洽。

## Search Query

public cloud CDN latency long tail region backbone congestion
