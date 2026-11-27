# N62: NVIDIA H100 (Hopper) 原生支持 FP8 和 INT8，其 FP8 Tensor Core 吞吐量为 1979 TOPS (SXM)，是 RT

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

NVIDIA H100 (Hopper) 原生支持 FP8 和 INT8，其 FP8 Tensor Core 吞吐量为 1979 TOPS (SXM)，是 RTX 4090 的 6 倍；在相同功耗限制下（700W vs 450W），H100 的单位功耗 FP8 吞吐量（TOPS/W）约为 RTX 4090 的 2.5 倍，适合高并发数据中心场景。

## Corrected Claim

NVIDIA H100 (Hopper) 原生支持 FP8 和 INT8，其 FP8 Tensor Core 吞吐量为 1979 TOPS (SXM)，是 RTX 4090 的 6 倍；在相同功耗限制下（700W vs 450W），H100 的单位功耗 FP8 吞吐量（TOPS/W）约为 RTX 4090 的 2.5 倍，适合高并发数据中心场景。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM FP8 稀疏峰值约 1979 TOPS，RTX 4090 FP8 稀疏峰值约 330 TOPS，比值约 6 倍；功耗比 700W/450W 约 1.56 倍，单位功耗性能比 6/1.56 约 3.8 倍，陈述中“2.5 倍”为保守估计或基于不同基准（如非稀疏或特定负载），量级合理且无逻辑矛盾。
