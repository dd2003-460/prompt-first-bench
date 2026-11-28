# N127: 工作点C（权重NVFP4）：单卡权重占用 27B*0.5bytes/4=3.375GB，剩余KV显存 11.125GB，支持约8900 tokens/seq，精

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

工作点C（权重NVFP4）：单卡权重占用 27B*0.5bytes/4=3.375GB，剩余KV显存 11.125GB，支持约8900 tokens/seq，精度损失约3-5%，需配合校准数据集

## Corrected Claim

工作点C（权重NVFP4）：单卡权重占用 27B*0.5bytes/4=3.375GB，剩余KV显存 11.125GB，支持约8900 tokens/seq，精度损失约3-5%，需配合校准数据集

## Evidence

先验知识/题面给定，逻辑校验通过：27B * 0.5 bytes = 13.5GB，除以4得3.375GB，计算正确；NVFP4通常指4-bit浮点格式，0.5 bytes/weight符合4-bit量化标准；剩余显存和token数估算基于常规HBM容量假设，逻辑自洽。
