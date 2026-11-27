# N97: 最大并发Batch Size (B_max) 的显存约束公式：B_max = (Total_VRAM - Model_Weights - Overhead) /

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

最大并发Batch Size (B_max) 的显存约束公式：B_max = (Total_VRAM - Model_Weights - Overhead) / (KV_Cache_per_token * Context_Length)，其中KV_Cache_per_token需根据模型GQA配置计算，此公式决定了在固定32K上下文下硬件能支持的理论最大并发数。

## Corrected Claim

最大并发Batch Size (B_max) 的显存约束公式：B_max = (Total_VRAM - Model_Weights - Overhead) / (KV_Cache_per_token * Context_Length)，其中KV_Cache_per_token需根据模型GQA配置计算，此公式决定了在固定32K上下文下硬件能支持的理论最大并发数。

## Evidence

先验知识/题面给定，逻辑校验通过
