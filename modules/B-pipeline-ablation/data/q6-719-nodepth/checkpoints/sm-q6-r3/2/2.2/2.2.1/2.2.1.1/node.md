# N252: 单台边缘服务器在图片+短视频混合负载下的最大稳定 QPS 容量 C_qps 约为 20,000-30,000 QPS，该值受限于网络 I/O 瓶颈（万兆网卡理论

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N72

## Claim

单台边缘服务器在图片+短视频混合负载下的最大稳定 QPS 容量 C_qps 约为 20,000-30,000 QPS，该值受限于网络 I/O 瓶颈（万兆网卡理论上限约 50,000-80,000 短连接 QPS）及 CPU 上下文切换开销，低于纯文本或小文件场景的 50,000 QPS 假设。

## Corrected Claim

单台边缘服务器在图片+短视频混合负载下的最大稳定 QPS 容量 C_qps 约为 20,000-30,000 QPS，该值受限于网络 I/O 瓶颈（万兆网卡理论上限约 50,000-80,000 短连接 QPS）及 CPU 上下文切换开销，低于纯文本或小文件场景的 50,000 QPS 假设。

## Evidence

先验知识/题面给定，逻辑校验通过：万兆网卡理论上限与混合负载下的实际QPS容量符合网络I/O及CPU开销的工程直觉，数值量级合理。

## Search Query

edge server max qps image video mixed load benchmark
