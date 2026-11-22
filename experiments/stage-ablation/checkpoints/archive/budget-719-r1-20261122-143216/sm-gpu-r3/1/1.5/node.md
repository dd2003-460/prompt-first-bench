# N10: NVFP4/W4 极低精度量化下 Qwen3-27B 的权重存储降至 13.5-6.75 GB，但需验证其是否支持 32K 上下文下的稳定推理，若出现注意力分数

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

NVFP4/W4 极低精度量化下 Qwen3-27B 的权重存储降至 13.5-6.75 GB，但需验证其是否支持 32K 上下文下的稳定推理，若出现注意力分数溢出或精度崩溃则排除该精度选项

## Corrected Claim

NVFP4/W4 极低精度量化下 Qwen3-27B 的权重存储约为 23.0 GB（来源[1]），需进一步验证其是否支持 32K 上下文下的稳定推理，若出现注意力分数溢出或精度崩溃则排除该精度选项

## Evidence

[质询]数值量级与来源直接矛盾：来源[1]明确指出NVFP4量化后的模型大小为23.0 GB，而陈述中声称降至13.5-6.75 GB，两者相差巨大，且来源未提及32K上下文稳定性验证结果。 | 来源[1]直接显示NVFP4量化后大小为23.0 GB，与陈述中的13.5-6.75 GB严重不符，且无证据支持32K上下文稳定性结论。

## Search Query

Qwen3-27B NVFP4 W4 quantization stability 32k context inference

## Retrieval Sources

- {'url': 'https://huggingface.co/kelnei/Qwen3.8-27B-NVFP4&rut=60ce30cd8eb8740e645f8d87199ae374abdbc199f43951bb5c7eb54d58796b97', 'type': 'ddg', 'title': 'kelnei/Qwen3.8-27B-NVFP4 · Hugging Face'}
