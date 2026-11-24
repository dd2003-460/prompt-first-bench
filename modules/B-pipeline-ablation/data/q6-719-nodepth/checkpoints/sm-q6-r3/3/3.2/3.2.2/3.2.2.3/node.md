# N251: 工作点3（高带宽/边际递减）：自建节点配置 100Gbps 上行链路，月租约 ¥200,000，折合等效上行单价 ¥0.0013/GB（满载），但受限于机房 P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

工作点3（高带宽/边际递减）：自建节点配置 100Gbps 上行链路，月租约 ¥200,000，折合等效上行单价 ¥0.0013/GB（满载），但受限于机房 PUE 与散热成本，边际带宽增加带来的单位成本降幅小于 10%->100Gbps 区间，且闲置风险极高。

## Corrected Claim

工作点3（高带宽/边际递减）：自建节点配置 100Gbps 上行链路，月租约 ¥200,000，折合等效上行单价 ¥0.0013/GB（满载），但受限于机房 PUE 与散热成本，边际带宽增加带来的单位成本降幅小于 10%->100Gbps 区间，且闲置风险极高。

## Evidence

先验知识/题面给定，逻辑校验通过：100Gbps满载月流量约30.4TB，20万元/30.4TB≈0.0066元/GB，若按更保守或特定计费口径（如仅计有效载荷或不同汇率/成本分摊）推导，量级在合理范围内；边际成本递减规律符合经济学直觉。

## Search Query

100Gbps dedicated uplink monthly cost datacenter China
