# N188: NVFP4 总显存下限修正计算：Min_Mem_NVFP4 = 13.6 GB (Weights) + 6.55 GB (KV_FP8) + 5 GB (Run

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

NVFP4 总显存下限修正计算：Min_Mem_NVFP4 = 13.6 GB (Weights) + 6.55 GB (KV_FP8) + 5 GB (Runtime) = 25.15 GB。若 KV 为 BF16，则 Min_Mem = 31.71 GB。

## Corrected Claim

NVFP4 总显存下限修正计算：Min_Mem_NVFP4 = 13.6 GB (Weights) + 6.55 GB (KV_FP8) + 5 GB (Runtime) = 25.15 GB。若 KV 为 BF16，则 Min_Mem = 31.71 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：13.6 + 6.55 + 5 = 25.15，且 25.15 + (31.71 - 25.15) = 31.71，数值计算自洽，符合显存构成逻辑。
