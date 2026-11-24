# N290: 云对象存储扩容的网络出口带宽边际成本：若扩容导致月度出口流量增加 ΔTraffic_TB，成本 = ΔTraffic_TB * 1024 * price_per

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N135

## Claim

云对象存储扩容的网络出口带宽边际成本：若扩容导致月度出口流量增加 ΔTraffic_TB，成本 = ΔTraffic_TB * 1024 * price_per_GB_out，阿里云 OSS 标准外网流出价格约为 ¥0.5/GB，故每增加 1TB 出口流量成本为 ¥512，此为 N135 声称‘隐性运维成本为 0’的反例。

## Corrected Claim

云对象存储扩容的网络出口带宽边际成本：若扩容导致月度出口流量增加 ΔTraffic_TB，成本 = ΔTraffic_TB * 1024 * price_per_GB_out，阿里云 OSS 标准外网流出价格约为 ¥0.5/GB，故每增加 1TB 出口流量成本为 ¥512，此为 N135 声称‘隐性运维成本为 0’的反例。

## Evidence

先验知识/题面给定，逻辑校验通过：1TB=1024GB，1024*0.5=512元，计算无误且符合阿里云OSS标准存储外网流出计费常识。

## Search Query

Alibaba Cloud OSS egress traffic pricing per GB
