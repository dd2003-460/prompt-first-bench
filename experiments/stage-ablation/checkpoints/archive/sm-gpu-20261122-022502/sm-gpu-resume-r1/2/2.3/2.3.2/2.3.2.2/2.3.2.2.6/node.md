# N625: 4x RTX 4090 在 TP=4 下，实际有效吞吐受限于通信瓶颈，理论峰值 16.1 tokens/s 需乘以通信效率因子 η = T_compute / 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N191, N192, N193

## Claim

4x RTX 4090 在 TP=4 下，实际有效吞吐受限于通信瓶颈，理论峰值 16.1 tokens/s 需乘以通信效率因子 η = T_compute / (T_compute + T_comm)，其中 T_comm = 8.1 ms（Ring All-Reduce），T_compute ≈ 10-12 ms（基于 4090 FP16 Tensor Core 算力 82.6 TFLOPS 与模型 FLOPs 估算），故 η ≈ 0.55-0.60，实际吞吐为 8.9-9.7 tokens/s，而非 16.1 tokens/s。

## Corrected Claim

4x RTX 4090 在 TP=4 下，实际有效吞吐受限于通信瓶颈。若 T_comm ≈ 8.1 ms 且 T_compute 估算为 10-12 ms，则通信效率因子 η ≈ 0.55-0.60，实际吞吐约为 8.9-9.7 tokens/s。注意：T_compute 的具体数值需根据实际模型 FLOPs 和硬件利用率进一步校准。

## Evidence

[质询]T_compute 的估算（10-12 ms）高度依赖于未明确给出的模型参数量、序列长度及具体算子分布，且 4090 的 FP16 算力在 TP=4 下的实际利用率通常远低于理论峰值，导致 T_compute 可能被低估，进而影响 η 的准确性。 | 先验知识/题面给定，逻辑校验通过；但 T_compute 为经验估算值，缺乏具体模型参数支持，且无外部来源验证，故降级。
