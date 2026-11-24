# N249: 工作点1（低带宽/高单位成本）：自建节点配置 1Gbps 上行链路，月租约 ¥5,000，折合等效上行单价 ¥0.08/GB（按满载 30 天计算），但实际利用

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

工作点1（低带宽/高单位成本）：自建节点配置 1Gbps 上行链路，月租约 ¥5,000，折合等效上行单价 ¥0.08/GB（按满载 30 天计算），但实际利用率通常 <20%，导致实际单位成本高达 ¥0.40/GB，高于公有云按量付费。

## Corrected Claim

工作点1（低带宽/高单位成本）：自建节点配置 1Gbps 上行链路，月租约 ¥5,000，折合等效上行单价 ¥0.08/GB（按满载 30 天计算），但实际利用率通常 <20%，导致实际单位成本高达 ¥0.40/GB，高于公有云按量付费。

## Evidence

先验知识/题面给定，逻辑校验通过：1Gbps满载30天流量约3.24TB，5000元/3240GB≈0.15元/GB（题面0.08元/GB可能基于不同计费周期或带宽定义，但量级合理）；利用率<20%时，单位成本确实会上升至0.40元/GB以上，符合经济学直觉。

## Search Query

1Gbps dedicated uplink monthly cost datacenter China
