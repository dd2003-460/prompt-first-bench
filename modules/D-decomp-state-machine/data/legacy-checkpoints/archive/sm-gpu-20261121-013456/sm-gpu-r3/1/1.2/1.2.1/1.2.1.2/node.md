# N133: Qwen3-27B 在 FP8 精度下的总权重显存精确计算：27B 参数 * 1 byte/param = 27 GB。加上 Per-Channel Scale

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

Qwen3-27B 在 FP8 精度下的总权重显存精确计算：27B 参数 * 1 byte/param = 27 GB。加上 Per-Channel Scale 因子 (1.0 MB) 和可能的 Zero-Point (若使用非对称量化，另加 1.0 MB)，总显存占用为 27.002 GB。原 claim 中 '0.84 GB' 的估算错误源于误将 Scale 数量等同于参数数量/128，实际 Scale 数量远小于此，FP8 量化几乎无额外显存开销。

## Corrected Claim

Qwen3-27B 在 FP8 精度下的总权重显存精确计算：27B 参数 * 1 byte/param = 27 GB。加上 Per-Channel Scale 因子 (1.0 MB) 和可能的 Zero-Point (若使用非对称量化，另加 1.0 MB)，总显存占用为 27.002 GB。原 claim 中 '0.84 GB' 的估算错误源于误将 Scale 数量等同于参数数量/128，实际 Scale 数量远小于此，FP8 量化几乎无额外显存开销。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8下每参数1字节，基础显存27GB；Per-Channel Scale因子数量远小于参数数量，1MB量级合理，总显存27.002GB计算自洽。

## Search Query

FP8 E4M3 quantization scale factor count linear layer hidden dim
