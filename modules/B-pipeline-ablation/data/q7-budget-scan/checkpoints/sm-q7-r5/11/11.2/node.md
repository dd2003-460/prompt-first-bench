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

父节点级核验未通过：不完备（子节点1定义了通用的5年TCO计算公式框架，子节点2提供了该公式中关键参数（r_egress_daily）的具体推导和取值逻辑，两者分别对应'模型结构'与'参数校准'，逻辑上正交且不冗余。然而，父节点的核心论点是针对'扩容导致的边际成本'以及反驳'隐性运维成本为0'这一特定断言（强调单TB出口成本为¥512），而子节点仅关注长期的累计TCO和混合比例估算，未明确涵盖父节点中提到的'边际增量'视角或具体的单位成本反例论证，因此完备性不足。）

## Search Query

Alibaba Cloud OSS egress traffic pricing per GB
