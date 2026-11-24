# N494: 对象存储数据块读取（Read Block）的延迟 T_data_read 受 IOPS 限制，在 10k IOPS 源站负载下，单请求排队等待时间 T_queu

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N166

## Claim

对象存储数据块读取（Read Block）的延迟 T_data_read 受 IOPS 限制，在 10k IOPS 源站负载下，单请求排队等待时间 T_queue ≈ 1/(10000 * (1-ρ))，若利用率 ρ=0.5，则 T_queue ≈ 0.1ms，加上 SSD 随机读物理延迟 0.1-0.5ms，总数据读取时间约 0.2-0.6ms

## Corrected Claim

对象存储数据块读取（Read Block）的延迟 T_data_read 受 IOPS 限制，在 10k IOPS 源站负载下，单请求排队等待时间 T_queue ≈ 1/(10000 * (1-ρ))，若利用率 ρ=0.5，则 T_queue ≈ 0.1ms，加上 SSD 随机读物理延迟 0.1-0.5ms，总数据读取时间约 0.2-0.6ms

## Evidence

先验知识/题面给定，逻辑校验通过：基于M/M/1排队模型，10k IOPS下ρ=0.5时排队延迟0.1ms及SSD随机读延迟0.1-0.5ms的量级符合工程常识与物理直觉。

## Search Query

SSD random read latency IOPS queueing theory M/M/1
