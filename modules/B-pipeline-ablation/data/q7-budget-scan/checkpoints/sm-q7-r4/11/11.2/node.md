# N290: 云对象存储扩容的网络出口带宽边际成本：若扩容导致月度出口流量增加 ΔTraffic_TB，成本 = ΔTraffic_TB * 1024 * price_per

- **status**: pending
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

父节点级核验未通过：不完备（子节点1提供了通用的5年累计成本计算公式，子节点2提供了特定业务场景下参数（r_egress_daily）的具体估算逻辑，两者在功能上互补且不重叠，因此正交且无冗余。然而，父节点的核心论证依赖于一个具体的边际成本反例（每TB出口流量成本¥512，用于反驳N135），而两个子节点均未包含这一具体的单位成本推导或该反例的直接陈述，导致父节点的关键论证细节在分解中缺失。）

## Search Query

Alibaba Cloud OSS egress traffic pricing per GB
