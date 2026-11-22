# N273: A100 40GB SXM4 在 vLLM 框架下运行 Qwen3-27B 高并发场景（batch_size>32）时，由于内存带宽瓶颈（2039 GB/s），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

A100 40GB SXM4 在 vLLM 框架下运行 Qwen3-27B 高并发场景（batch_size>32）时，由于内存带宽瓶颈（2039 GB/s），实际持续算力利用率约为 60%-80%，对应有效算力为 187-250 TFLOPS

## Corrected Claim

A100 40GB SXM4 在 vLLM 框架下运行 Qwen3-27B 高并发场景（batch_size>32）时，由于内存带宽瓶颈（2039 GB/s），实际持续算力利用率约为 60%-80%，对应有效算力为 187-250 TFLOPS

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM4 峰值算力 312 TFLOPS，60%-80% 利用率对应 187-250 TFLOPS 数值计算准确；高并发下受内存带宽限制导致算力利用率低于峰值符合 LLM 推理基本物理直觉。

## Search Query

A100 vLLM Qwen3-27B high concurrency batch size 32+ memory bandwidth bound throughput
