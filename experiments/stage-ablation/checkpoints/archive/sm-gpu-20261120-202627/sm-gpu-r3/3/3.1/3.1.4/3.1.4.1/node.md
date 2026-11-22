# N251: Qwen3-27B 在 RTX 3080 (12GB) 上运行 INT4 精度时，模型权重显存占用约为 13.5GB，超过 12GB 显存容量，导致单卡部署不可

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

Qwen3-27B 在 RTX 3080 (12GB) 上运行 INT4 精度时，模型权重显存占用约为 13.5GB，超过 12GB 显存容量，导致单卡部署不可行，必须采用双卡聚合显存或 Offload 至系统内存。

## Corrected Claim

Qwen3-27B 在 RTX 3080 (12GB) 上运行 INT4 精度时，模型权重显存占用约为 13.5GB，超过 12GB 显存容量，导致单卡部署不可行，必须采用双卡聚合显存或 Offload 至系统内存。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在INT4下权重约13.5GB，加上KV Cache及激活值，必然超过12GB显存，单卡部署不可行。
