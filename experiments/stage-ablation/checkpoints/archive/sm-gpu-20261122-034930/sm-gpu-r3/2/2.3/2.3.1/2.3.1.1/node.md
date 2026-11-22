# N226: W4量化（如AWQ/GPTQ）的Scale因子开销精确值：对于Qwen3-27B，Scale因子通常以FP16存储，每个量化组（如group_size=128）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

W4量化（如AWQ/GPTQ）的Scale因子开销精确值：对于Qwen3-27B，Scale因子通常以FP16存储，每个量化组（如group_size=128）需要一个Scale值，总Scale参数量约为27B/128≈210M参数，占用显存约0.42GB（FP16），因此W4权重实际占用约为13.5GB + 0.42GB ≈ 13.92GB。

## Corrected Claim

W4量化（如AWQ/GPTQ）的Scale因子开销精确值：对于Qwen3-27B，Scale因子通常以FP16存储，每个量化组（如group_size=128）需要一个Scale值，总Scale参数量约为27B/128≈210M参数，占用显存约0.42GB（FP16），因此W4权重实际占用约为13.5GB + 0.42GB ≈ 13.92GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B/128≈210M，210M*2bytes≈0.42GB，13.5+0.42=13.92GB，计算无误且符合W4量化常识。

## Search Query

AWQ GPTQ W4 quantization scale factor overhead GB
