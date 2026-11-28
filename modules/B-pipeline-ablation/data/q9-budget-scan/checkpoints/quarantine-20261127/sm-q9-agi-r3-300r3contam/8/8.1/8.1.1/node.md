# N237: V100 互联带宽约束：NVLink 双向带宽 300 GB/s (单链路) 或 600 GB/s (双向聚合)，在 TP=4 张量并行中，AllReduce 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

V100 互联带宽约束：NVLink 双向带宽 300 GB/s (单链路) 或 600 GB/s (双向聚合)，在 TP=4 张量并行中，AllReduce 通信流量占总通信量的比例约为 2*(n-1)/n，当 Batch Size 较小时，通信延迟 (Latency-bound) 而非带宽 (Bandwidth-bound) 成为瓶颈，导致有效聚合带宽远低于 4 卡线性叠加值 3600 GB/s。

## Corrected Claim

V100 互联带宽约束：NVLink 双向带宽 300 GB/s (单链路) 或 600 GB/s (双向聚合)，在 TP=4 张量并行中，AllReduce 通信流量占总通信量的比例约为 2*(n-1)/n，当 Batch Size 较小时，通信延迟 (Latency-bound) 而非带宽 (Bandwidth-bound) 成为瓶颈，导致有效聚合带宽远低于 4 卡线性叠加值 3600 GB/s。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 NVLink 3.0 单链路双向带宽确为 300GB/s，TP=4 下 AllReduce 流量占比公式 2(n-1)/n 符合 Ring AllReduce 算法原理，小 Batch 下 Latency-bound 导致有效带宽低于理论峰值符合分布式训练常识。

## Search Query

V100 NVLink allreduce latency tensor parallelism overhead vllm small batch
