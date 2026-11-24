# N561: 电信-联通跨网 RTT 的 P99 值：在 2023-2024 年中国网络测量数据中，电信用户访问联通边缘节点的跨省 P99 RTT 典型值为 35-55ms，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N184

## Claim

电信-联通跨网 RTT 的 P99 值：在 2023-2024 年中国网络测量数据中，电信用户访问联通边缘节点的跨省 P99 RTT 典型值为 35-55ms，比同网电信跨省 RTT（20-50ms）高 10-25ms，主要源于跨网结算点（Peering Point）的额外跳数和拥塞。

## Corrected Claim

电信用户访问联通边缘节点的跨省P99 RTT通常高于同网电信跨省RTT，主要源于跨网结算点的额外跳数和拥塞，具体数值随测量环境和时间波动。

## Evidence

[质询]具体数值区间（35-55ms vs 20-50ms）及差值（10-25ms）属于经验性测量数据，缺乏公开权威基准支持，且受具体地理位置、运营商内部路由策略及时间窗口影响极大，不同测量报告间差异显著，该特定数值范围可能具有偶然性或特定样本偏差。 | 逻辑自洽：跨网通信通常需经过结算点或更复杂的路由路径，导致跳数增加和潜在拥塞，RTT高于同网符合网络工程直觉；但source为search且无可用外部来源支持具体数值，依据经验事实排除条款，降级为定性表述。

## Search Query

China Telecom to China Unicom cross-network P99 RTT peering point latency measurement 2023
