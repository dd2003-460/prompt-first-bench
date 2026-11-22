# N81: T_throughput (吞吐量) 的标准化定义：T_throughput 为单请求 (batch_size=1) 在目标上下文长度 (32K) 下的解码速度

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

T_throughput (吞吐量) 的标准化定义：T_throughput 为单请求 (batch_size=1) 在目标上下文长度 (32K) 下的解码速度 (tokens/s)，而非预填充速度，因为本地工作站推理主要瓶颈在解码阶段。

## Corrected Claim

T_throughput (吞吐量) 的标准化定义：T_throughput 为单请求 (batch_size=1) 在目标上下文长度 (32K) 下的解码速度 (tokens/s)，而非预填充速度，因为本地工作站推理主要瓶颈在解码阶段。

## Evidence

先验知识/题面给定，逻辑校验通过：在本地工作站（非数据中心集群）场景下，单请求（batch_size=1）的解码阶段受限于内存带宽（Memory-Bound），确实是主要瓶颈；将吞吐量定义为解码速度符合LLM推理性能评估的常规工程实践。

## Search Query

LLM inference throughput definition decode vs prefill batch size 1
