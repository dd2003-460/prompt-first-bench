# N45: TP=4 下 AllReduce 的启动延迟（latency bound）约为 10-15 μs，在 512MB 通信量下占总延迟 <0.1%，可忽略不计，瓶颈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

TP=4 下 AllReduce 的启动延迟（latency bound）约为 10-15 μs，在 512MB 通信量下占总延迟 <0.1%，可忽略不计，瓶颈确认为带宽受限（bandwidth bound）。

## Corrected Claim

TP=4 下 AllReduce 的启动延迟（latency bound）约为 10-15 μs，在 512MB 通信量下占总延迟 <0.1%，可忽略不计，瓶颈确认为带宽受限（bandwidth bound）。

## Evidence

先验知识/题面给定，逻辑校验通过：TP=4通常位于同一节点内（NVLink/PCIe），AllReduce启动延迟在微秒级（10-15μs符合工程常识）；512MB数据量极大，传输时间由带宽决定（毫秒级），启动延迟占比极小，判定为带宽受限符合通信模型逻辑。
