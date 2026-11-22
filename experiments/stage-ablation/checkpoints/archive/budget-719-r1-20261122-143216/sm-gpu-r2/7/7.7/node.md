# N135: 显存带宽对 Decode 吞吐量的线性影响系数在 Batch Size=1 时接近 1.0，但在 Batch Size>1 时因计算密度增加而下降，需针对 Qw

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32, N33, N34

## Claim

显存带宽对 Decode 吞吐量的线性影响系数在 Batch Size=1 时接近 1.0，但在 Batch Size>1 时因计算密度增加而下降，需针对 Qwen3-27B 在 32K 上下文下的具体 Batch Size 配置进行实测校正。

## Corrected Claim

显存带宽对 Decode 吞吐量的影响在 Batch Size=1 时通常接近线性（系数接近 1.0），但在 Batch Size>1 时因计算密度增加，带宽瓶颈效应减弱，具体影响系数需针对 Qwen3-27B 在 32K 上下文下的硬件环境与 Batch Size 配置进行实测校正。

## Evidence

[质询]该陈述包含具体的经验性结论（系数接近1.0、随Batch Size下降），属于经验事实而非第一性原理可严格推导的数学/物理定律；且缺乏针对Qwen3-27B在32K上下文下的具体实测数据支持，无法排除特定硬件或软件栈优化带来的非线性偏差。 | 经验事实，逻辑自洽（Decode阶段通常受显存带宽限制，Batch Size增加会提高计算密度从而降低带宽瓶颈的线性影响系数），但缺来源支持。

## Search Query

LLM decode throughput vs memory bandwidth batch size linear coefficient
