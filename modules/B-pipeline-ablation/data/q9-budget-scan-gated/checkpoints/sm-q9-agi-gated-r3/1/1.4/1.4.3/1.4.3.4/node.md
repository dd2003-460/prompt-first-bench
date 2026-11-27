# N54: 量化 N28 中 AllReduce 与计算的重叠程度：在 vLLM 中，AllReduce 可与部分 GEMM 计算异步重叠，有效通信时间 T_eff = T

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27, N28, N29

## Claim

量化 N28 中 AllReduce 与计算的重叠程度：在 vLLM 中，AllReduce 可与部分 GEMM 计算异步重叠，有效通信时间 T_eff = T_comm * (1 - overlap_ratio)，其中 overlap_ratio 取决于 CUDA stream 调度策略和算子粒度，典型值为 0.3-0.5，因此实际占比应从 53.5% 修正为 53.5% * (1 - 0.4) ≈ 32%，需通过 nsys profile 测量实际重叠率。

## Corrected Claim

在 vLLM 中，AllReduce 可与部分 GEMM 计算异步重叠，有效通信时间 T_eff = T_comm * (1 - overlap_ratio)。overlap_ratio 取决于 CUDA stream 调度策略和算子粒度，具体数值需通过 nsys profile 测量实际重叠率来确定，不宜直接使用典型值进行粗略修正。

## Evidence

[质询]overlap_ratio 的典型值 0.3-0.5 属于经验事实，缺乏通用性，且不同硬件/网络配置下差异巨大，不能简单作为固定系数修正 53.5% 的占比。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM tensor parallelism communication computation overlap ratio nsys profile
