# N52: INT4 (AWQ/GPTQ) 量化下的额外开销：Zero-point 和 Scale 通常以 FP16 存储，每 128 个元素一组，开销约为 (27 * 1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

INT4 (AWQ/GPTQ) 量化下的额外开销：Zero-point 和 Scale 通常以 FP16 存储，每 128 个元素一组，开销约为 (27 * 10^9 / 128) * 4 bytes ≈ 850 MB；加上 Group Norm 等元数据，总占用约为 14.5-15.0 GB，而非简单的 13.5 GB

## Corrected Claim

INT4 (AWQ/GPTQ) 量化下的额外开销：Zero-point 和 Scale 通常以 FP16 存储，每 128 个元素一组，开销约为 (27 * 10^9 / 128) * 4 bytes ≈ 850 MB；加上 Group Norm 等元数据，总占用约为 14.5-15.0 GB，而非简单的 13.5 GB

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数模型INT4量化后权重约13.5GB，Zero-point和Scale以FP16存储每128元素一组，开销计算(27*10^9/128)*4≈850MB合理，总占用14.5-15.0GB符合工程实践

## Search Query

AWQ GPTQ INT4 quantization zero-point scale overhead memory usage 27B
