# N174: W4A16量化后Qwen3-27B的总权重存储基线为：27.18e9 * 0.5 bytes = 13.59 GB (权重) + 0.425 GB (Scale

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51, N52, N53

## Claim

W4A16量化后Qwen3-27B的总权重存储基线为：27.18e9 * 0.5 bytes = 13.59 GB (权重) + 0.425 GB (Scale) = 14.015 GB，该数值不包含KV Cache及激活值。

## Corrected Claim

W4A16量化后Qwen3-27B的总权重存储基线为：27.18e9 * 0.5 bytes = 13.59 GB (权重) + 0.425 GB (Scale) = 14.015 GB，该数值不包含KV Cache及激活值。

## Evidence

先验知识/题面给定，逻辑校验通过：W4A16量化下权重存储为参数量*0.5字节，Scale开销估算合理，总数值计算自洽。

## Search Query

W4A16 quantized model size calculation 27B parameters
