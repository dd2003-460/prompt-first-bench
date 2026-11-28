# N95: 单卡可用显存平衡方程：Available_GPU_Mem = Total_Physical_Mem (16GB) - CUDA_Context (1.75GB 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

单卡可用显存平衡方程：Available_GPU_Mem = Total_Physical_Mem (16GB) - CUDA_Context (1.75GB avg) - vLLM_Overhead (0.3GB) - Weight_Shared_Per_GPU; 在 TP=4 下，Weight_Shared_Per_GPU = 13.69GB / 4 ≈ 3.42GB，故 Available_for_KV ≈ 16 - 1.75 - 0.3 - 3.42 = 10.53 GB。

## Corrected Claim

单卡可用显存平衡方程：Available_GPU_Mem = Total_Physical_Mem (16GB) - CUDA_Context (1.75GB avg) - vLLM_Overhead (0.3GB) - Weight_Shared_Per_GPU; 在 TP=4 下，Weight_Shared_Per_GPU = 13.69GB / 4 ≈ 3.42GB，故 Available_for_KV ≈ 16 - 1.75 - 0.3 - 3.42 = 10.53 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 16 - 1.75 - 0.3 - 3.42 = 10.53 正确，且各组件显存占用量级符合 vLLM 部署常规经验。
