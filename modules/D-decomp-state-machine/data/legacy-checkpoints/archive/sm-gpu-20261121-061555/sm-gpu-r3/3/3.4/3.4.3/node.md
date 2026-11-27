# N89: INT8精度下Qwen3-27B在A100 (40GB HBM2e)上的有效显存带宽利用率修正因子为0.75-0.80，受INT8张量核心支持及反量化路径影响，

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20, N21, N24

## Claim

INT8精度下Qwen3-27B在A100 (40GB HBM2e)上的有效显存带宽利用率修正因子为0.75-0.80，受INT8张量核心支持及反量化路径影响，实际吞吐量基准需乘以该因子。

## Corrected Claim

INT8精度下Qwen3-27B在A100上的有效显存带宽利用率通常低于理论峰值，受INT8张量核心支持及反量化路径影响，实际吞吐量需根据具体量化方案和软件栈进行修正，典型修正因子可能在0.7-0.85之间，具体数值需实测确定。

## Evidence

[质询]该修正因子（0.75-0.80）是一个具体的经验数值，缺乏通用的物理定律或第一性原理支持，且不同量化实现（如SmoothQuant, GPTQ, AWQ）及硬件微架构下的实际带宽利用率差异巨大，该特定数值范围可能仅适用于特定基准测试或特定软件栈，不具备普适性。 | source=knowledge，逻辑上INT8量化确实会因反量化开销和Tensor Core支持差异导致有效带宽利用率低于理论峰值，0.75-0.80在工程经验上属于合理量级，但作为精确数值缺乏通用理论推导支持，且无外部来源验证其普适性。

## Search Query

A100 INT8 LLM inference bandwidth utilization efficiency factor
