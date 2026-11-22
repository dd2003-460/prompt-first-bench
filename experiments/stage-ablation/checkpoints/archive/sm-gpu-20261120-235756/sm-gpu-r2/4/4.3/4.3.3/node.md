# N89: 单卡最大并发 Batch Size 计算公式：Batch_Size = (GPU_Total_VRAM - Weight_VRAM - Activation_O

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

单卡最大并发 Batch Size 计算公式：Batch_Size = (GPU_Total_VRAM - Weight_VRAM - Activation_Overhead) / KV_Per_Request，其中 Activation_Overhead 需根据框架（如 vLLM PagedAttention）估算为 1-2GB。

## Corrected Claim

单卡最大并发 Batch Size 计算公式：Batch_Size = (GPU_Total_VRAM - Weight_VRAM - Activation_Overhead) / KV_Per_Request，其中 Activation_Overhead 需根据框架（如 vLLM PagedAttention）估算为 1-2GB。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM paged attention memory overhead estimation
