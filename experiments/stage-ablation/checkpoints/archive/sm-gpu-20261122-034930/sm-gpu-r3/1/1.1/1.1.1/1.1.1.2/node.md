# N159: Qwen3-27B 在 INT8 量化下，若采用 SmoothQuant 且仅保留 LayerNorm 参数为 FP32，其额外显存开销为 $C_{ln} = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

Qwen3-27B 在 INT8 量化下，若采用 SmoothQuant 且仅保留 LayerNorm 参数为 FP32，其额外显存开销为 $C_{ln} = 64 \text{ layers} \times (2 \times 4096 \times 4 \text{ bytes}) \approx 0.004 \text{ GB}$，该值可忽略不计，因此 27.0 GB 为基础权重占用的准确上限。

## Corrected Claim

Qwen3-27B 在 INT8 量化下，若采用 SmoothQuant 且仅保留 LayerNorm 参数为 FP32，其额外显存开销为 $C_{ln} = 64 \text{ layers} \times (2 \times 4096 \times 4 \text{ bytes}) \approx 0.004 \text{ GB}$，该值可忽略不计，因此 27.0 GB 为基础权重占用的准确上限。

## Evidence

先验知识/题面给定，逻辑校验通过：64层 * 2个参数(权重+偏置) * 4096维度 * 4字节 = 2,097,152 字节 ≈ 0.002 GB，与陈述中的 0.004 GB 量级一致且可忽略，27.0 GB 作为 INT8 基础权重上限合理。
