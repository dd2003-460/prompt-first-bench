# N224: RTX 5090 在 NVFP4 精度下的可行性分析：权重占用 13.5GB (27B*0.5B) + KV Cache 2.6GB (INT8 KV) + 激

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

RTX 5090 在 NVFP4 精度下的可行性分析：权重占用 13.5GB (27B*0.5B) + KV Cache 2.6GB (INT8 KV) + 激活 1.3GB + Overhead 3GB = 20.4GB < 32GB，可行且余量 36%；此配置允许在单卡上运行更高精度权重或更长上下文（如 64K），相比 W4 方案在质量上更具优势（NVFP4 通常优于 W4 的均匀量化）。

## Corrected Claim

RTX 5090 在 NVFP4 精度下的可行性分析：权重占用 13.5GB (27B*0.5B) + KV Cache 2.6GB (INT8 KV) + 激活 1.3GB + Overhead 3GB = 20.4GB < 32GB，可行且余量 36%；此配置允许在单卡上运行更高精度权重或更长上下文（如 64K），相比 W4 方案在质量上更具优势（NVFP4 通常优于 W4 的均匀量化）。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在NVFP4(4bit)下权重约13.5GB，加上KV Cache、激活及Overhead总计20.4GB，小于32GB显存，且NVFP4精度通常优于W4均匀量化，符合技术常识。

## Search Query

RTX 5090 NVFP4 inference Qwen3 27B memory footprint
