# N50: RTX 5090 (Blackwell 架构) 原生支持 NVFP4 推理，但需 CUDA 12.8+ 及特定驱动版本，当前软件栈成熟度较低，实际吞吐量提升幅度

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

RTX 5090 (Blackwell 架构) 原生支持 NVFP4 推理，但需 CUDA 12.8+ 及特定驱动版本，当前软件栈成熟度较低，实际吞吐量提升幅度（相比 FP8）约为 1.5-2 倍，但存在 [时效待核] 风险，需验证最新驱动兼容性。

## Corrected Claim

RTX 5090 (Blackwell 架构) 原生支持 NVFP4 推理，需 CUDA 12.8+ 及特定驱动版本。相比 FP8，NVFP4 在理论及典型场景下可提供显著吞吐量提升（具体倍数依工作负载而异，通常预期在 1.5-2 倍区间），但当前软件栈成熟度较低，实际性能需结合最新驱动及具体应用验证。

## Evidence

[质询]具体吞吐量提升幅度（1.5-2倍）及特定软件栈成熟度描述属于经验事实，缺乏来源支持，且不同工作负载下性能增益差异巨大，该数值范围可能过于简化或存在偏差。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

RTX 5090 NVFP4 support CUDA 12.8 driver requirements
