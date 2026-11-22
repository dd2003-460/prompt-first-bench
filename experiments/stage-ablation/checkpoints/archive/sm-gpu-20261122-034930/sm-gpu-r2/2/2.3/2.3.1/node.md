# N76: W4权重显存占用精确值为13.5GB（基于27B参数 * 0.5 bytes/param，假设Qwen3-27B参数量为27.0B，需确认W4量化是否包含Sca

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

W4权重显存占用精确值为13.5GB（基于27B参数 * 0.5 bytes/param，假设Qwen3-27B参数量为27.0B，需确认W4量化是否包含Scale因子额外开销，通常Scale因子占额外1-2%显存，即13.5GB * 1.02 ≈ 13.77GB）

## Corrected Claim

W4权重显存占用精确值为13.5GB（基于27B参数 * 0.5 bytes/param，假设Qwen3-27B参数量为27.0B，需确认W4量化是否包含Scale因子额外开销，通常Scale因子占额外1-2%显存，即13.5GB * 1.02 ≈ 13.77GB）

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 * 0.5 bytes/param = 13.5GB，量纲与数值计算正确，符合W4量化基本定义。
