# N20: 在max-num-seqs=8的并发设置下，理论最大吞吐量 Throughput_max = num_gpus * gpu_flops / (ops_per_t

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

在max-num-seqs=8的并发设置下，理论最大吞吐量 Throughput_max = num_gpus * gpu_flops / (ops_per_token * latency_per_token)，其中 gpu_flops 为V100-SXM2-16GB的FP16峰值算力 15.7 TFLOPS

## Corrected Claim

在max-num-seqs=8的并发设置下，理论最大吞吐量 Throughput_max = num_gpus * gpu_flops / (ops_per_token * latency_per_token)，其中 gpu_flops 为V100-SXM2-16GB的FP16峰值算力 15.7 TFLOPS

## Evidence

先验知识/题面给定，逻辑校验通过：V100-SXM2-16GB FP16峰值算力确为15.7 TFLOPS，公式量纲正确（FLOPS / (FLOPs/token * s/token) = tokens/s），符合基本物理/计算直觉。
