# N404: 自建POP节点CPU处理时间 T_cpu 的P99估算值为 3-5ms，基于单核处理能力 100M ops/s 及单请求平均处理逻辑 300k ops 的计算：

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

自建POP节点CPU处理时间 T_cpu 的P99估算值为 3-5ms，基于单核处理能力 100M ops/s 及单请求平均处理逻辑 300k ops 的计算：T_cpu = 300k / 100M * 1000ms。

## Corrected Claim

自建POP节点CPU处理时间 T_cpu 的P99估算值为 3-5ms，基于单核处理能力 100M ops/s 及单请求平均处理逻辑 300k ops 的计算：T_cpu = 300k / 100M * 1000ms。

## Evidence

先验知识/题面给定，逻辑校验通过：300,000 ops / 100,000,000 ops/s = 0.003s = 3ms，计算无误且量级合理。
