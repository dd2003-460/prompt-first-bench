# N349: 次日留存率 L2 对 P99 延迟 ΔP99 的边际敏感度具体数值：根据行业 A/B 测试数据，每增加 100ms P99 延迟，次日留存率下降约 0.5%-1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N110

## Claim

次日留存率 L2 对 P99 延迟 ΔP99 的边际敏感度具体数值：根据行业 A/B 测试数据，每增加 100ms P99 延迟，次日留存率下降约 0.5%-1.5%，即 dL2/dP99 ≈ -0.00005 ~ -0.00015 /ms（原 N110 的 0.1%-0.3%/ms 高估了敏感度 10 倍）

## Corrected Claim

延迟增加通常会对用户留存产生负面影响，具体敏感度因产品类型而异。例如，亚马逊内部测试显示每增加100ms延迟会导致销售额下降约1%（来源[2]），但次日留存率的具体边际敏感度缺乏通用的行业统一数据支持。

## Evidence

[质询]该陈述声称基于“行业A/B测试数据”得出次日留存率对P99延迟的具体敏感度（-0.5%~-1.5%/100ms），但这是一个非常具体的经验性统计结论，且不同产品（游戏、电商、社交）对延迟的敏感度差异巨大，不存在通用的“行业”标准数值。此外，参考来源中仅提供了亚马逊销售额对延迟的敏感度（1%/100ms），并未提供次日留存率（L2）的相关数据，无法直接支持该具体数值。 | 逻辑上量纲和量级合理（延迟增加导致留存下降符合直觉），但属于经验事实，参考来源[2]仅支持销售额敏感度，未覆盖次日留存率，且无其他来源直接支持该具体数值，故降级。

## Search Query

A/B test latency impact next day retention rate drop per 100ms mobile app

## Retrieval Sources

- {'url': 'https://speedtest.im/en/guide/is-100-ms-ping-bad.html&rut=2a29f4f4c776e775cccf159a5eebd4973beedcebc9d292c2c45800e77fc60f2c', 'type': 'ddg', 'title': 'Is 100 ms Ping Bad? Understand Latency and Fix It - 一键测速网'}
- {'url': 'https://latencycost.com/&rut=875253c8014e636070919ef2aa0f1edbaf3429fef51605bd04cc009295322e47', 'type': 'ddg', 'title': 'Latency Cost: Amazon Loses 1% Sales Per 100ms (and It Gets Worse)'}
- {'url': 'https://www.broadbandsearch.net/blog/signs-of-high-internet-latency&rut=8cdf5fb944c07a2a74daa9130e276c7fb28a32a5fc0892c2c7910c455d93a566', 'type': 'ddg', 'title': 'High Latency: Causes & Fixes | BroadbandSearch'}
