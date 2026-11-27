# N53: INT4/W4 精度下的 Group Quantization (如 GPTQ 或 AWQ) 通常以 Group Size=128 为单位存储 Scale 和 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

INT4/W4 精度下的 Group Quantization (如 GPTQ 或 AWQ) 通常以 Group Size=128 为单位存储 Scale 和 Zero Point (各 1 个 FP16 或 FP32 值)，额外显存开销计算公式为：Overhead_GB = (27B / 128) * (2 * 2 bytes) / 1e9 ≈ 0.84 GB (若使用 FP16 Scale/Zero)，总权重显存约为 13.5 + 0.84 = 14.34 GB。

## Corrected Claim

INT4/W4 精度下的 Group Quantization (如 GPTQ 或 AWQ) 通常以 Group Size=128 为单位存储 Scale 和 Zero Point (各 1 个 FP16 或 FP32 值)，额外显存开销计算公式为：Overhead_GB = (27B / 128) * (2 * 2 bytes) / 1e9 ≈ 0.84 GB (若使用 FP16 Scale/Zero)，总权重显存约为 13.5 + 0.84 = 14.34 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数/128组 * 2个FP16值(4字节) = 0.84GB，计算无误且符合GPTQ/AWQ标准实现逻辑。
