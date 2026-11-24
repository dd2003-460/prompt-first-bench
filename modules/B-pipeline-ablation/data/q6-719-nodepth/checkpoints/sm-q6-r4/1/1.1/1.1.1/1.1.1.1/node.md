# N145: 在典型城市用户（如上海用户访问上海POP）场景下，物理距离 d ≈ 0 km，Haversine 公式计算结果为 0，此时 RTT 瓶颈转为交换机/网卡处理延迟

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

在典型城市用户（如上海用户访问上海POP）场景下，物理距离 d ≈ 0 km，Haversine 公式计算结果为 0，此时 RTT 瓶颈转为交换机/网卡处理延迟（通常 <1ms），代表低延迟/低成本工作点。

## Corrected Claim

在典型城市用户（如上海用户访问上海POP）场景下，物理距离 d ≈ 0 km，Haversine 公式计算结果为 0，此时 RTT 瓶颈转为交换机/网卡处理延迟（通常 <1ms），代表低延迟/低成本工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：同城访问物理距离趋近于0，Haversine公式结果趋近于0，此时网络延迟主要受限于本地交换/网卡处理（通常<1ms），符合低延迟/低成本工作点的定义。

## Search Query

typical city user to local CDN POP distance latency
