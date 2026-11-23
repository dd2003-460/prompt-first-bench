# N218: 公有云CDN回源带宽拥塞对P99延迟的影响：当回源流量超过运营商骨干网容量阈值时，发生排队和丢包重传，T_origin_transfer = Data_Size

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

公有云CDN回源带宽拥塞对P99延迟的影响：当回源流量超过运营商骨干网容量阈值时，发生排队和丢包重传，T_origin_transfer = Data_Size / Bandwidth_available * (1 + Retransmission_Rate)，Retransmission_Rate在拥塞时可达5-20%，导致P99延迟增加10-50ms，需评估日均2TB下载中回源流量（约10-40%）对骨干网压力的具体影响

## Corrected Claim

公有云CDN回源带宽拥塞对P99延迟的影响：当回源流量超过运营商骨干网容量阈值时，发生排队和丢包重传，T_origin_transfer = Data_Size / Bandwidth_available * (1 + Retransmission_Rate)，Retransmission_Rate在拥塞时可达5-20%，导致P99延迟增加10-50ms，需评估日均2TB下载中回源流量（约10-40%）对骨干网压力的具体影响

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合排队论与TCP重传基本逻辑，5-20%重传率及10-50ms延迟增量在骨干网拥塞场景下量级合理，无内部矛盾。

## Search Query

CDN origin fetch bandwidth congestion packet retransmission latency impact P99
