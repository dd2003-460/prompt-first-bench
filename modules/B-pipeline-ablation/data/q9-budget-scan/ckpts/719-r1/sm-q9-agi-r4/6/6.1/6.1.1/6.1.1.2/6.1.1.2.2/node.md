# N688: FP16 下 Qwen3.8-27B 在 4x V100 TP=4 配置的实际 Decode 吞吐量 (tokens/s) 需通过 nsight-systems

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N250

## Claim

FP16 下 Qwen3.8-27B 在 4x V100 TP=4 配置的实际 Decode 吞吐量 (tokens/s) 需通过 nsight-systems 实测，以校正 T_compute 估算值 10ms/token 的误差范围

## Corrected Claim

FP16 下 Qwen3.8-27B 在 4x V100 TP=4 配置的实际 Decode 吞吐量需通过 nsight-systems 实测以确定，当前 T_compute 估算值 10ms/token 仅为待验证的理论估计，可能存在显著误差。

## Evidence

[质询]该陈述包含具体的经验性性能指标（10ms/token）和特定的硬件/软件配置（Qwen3.8-27B, 4x V100, FP16），这些属于经验事实，无法从第一性原理推导，且缺乏实测数据支持其准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen 27B V100 Tensor Parallel 4 decode throughput tokens per second benchmark
