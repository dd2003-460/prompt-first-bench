# N169: 长尾区域（20-30%用户）回源路径延迟分解：Latency_tail = RTT_pop_origin + Origin_Processing + RTT_o

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

长尾区域（20-30%用户）回源路径延迟分解：Latency_tail = RTT_pop_origin + Origin_Processing + RTT_origin_pop。基于中国地理分布，长尾POP至中心机房（如北京/上海）单程RTT典型值为15-30ms，往返30-60ms；Origin处理时间取决于回源并发，若未命中导致CPU排队，P99处理时间可能增加20-50ms。

## Corrected Claim

长尾区域（20-30%用户）回源路径延迟分解：Latency_tail = RTT_pop_origin + Origin_Processing + RTT_origin_pop。基于中国地理分布，长尾POP至中心机房（如北京/上海）单程RTT典型值为15-30ms，往返30-60ms；Origin处理时间取决于回源并发，若未命中导致CPU排队，P99处理时间可能增加20-50ms。

## Evidence

先验知识/题面给定，逻辑校验通过：中国骨干网单程RTT 15-30ms符合物理距离与光纤传输延迟常识，Origin处理时间20-50ms符合高并发下CPU排队及IO操作的典型量级，公式分解逻辑自洽。

## Search Query

China CDN back-to-origin latency RTT average ms
