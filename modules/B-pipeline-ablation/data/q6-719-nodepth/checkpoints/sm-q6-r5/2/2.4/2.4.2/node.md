# N60: 单跳延迟 L_hop 的非均匀分布：骨干网平均 5ms，城域网平均 10ms，接入网平均 15-20ms；P99 跳数延迟 L_hops_p99 = Σ P(h

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N14

## Claim

单跳延迟 L_hop 的非均匀分布：骨干网平均 5ms，城域网平均 10ms，接入网平均 15-20ms；P99 跳数延迟 L_hops_p99 = Σ P(hop_type) * L_hop_p99(type)，而非简单 Hops * 5ms，因 P99 受高延迟链路主导。

## Corrected Claim

单跳延迟 L_hop 呈非均匀分布，通常接入网延迟高于骨干网；P99 跳数延迟 L_hops_p99 应基于各类型链路的 P99 延迟加权计算，而非简单 Hops * 平均延迟，因 P99 受高延迟链路主导。

## Evidence

[质询]具体数值（骨干网5ms、城域网10ms、接入网15-20ms）属于经验性统计参数，不同网络架构、运营商及测量时间点差异巨大，缺乏普适性的固定标准；且参考来源仅提供了设备处理延迟范围，未提供特定网络层级（骨干/城域/接入）的平均跳延迟统计数据，无法直接支持这些具体数值。 | 逻辑上P99延迟确实受高延迟链路主导，不能简单用平均跳数乘以平均延迟，该定性逻辑自洽；但具体数值为经验事实，参考来源[1]仅涉及设备处理延迟，未覆盖网络层级平均延迟统计，属间接/无关支持，依据经验事实排除条款降级。

## Search Query

China backbone network average latency per hop ms telecom ISP

## Retrieval Sources

- {'url': 'https://quickqlab.com.cn/network-latency-breakdown-hop-by-hop-analysis/&rut=2c45f5dcfbde4bfe413ac0e6004cf5bc2f776b48e6ec7edbba0d7ed4d712add7', 'type': 'ddg', 'title': '网络延迟拆解：从本地到目标服务器的每一跳 - QuickQ Lab'}
