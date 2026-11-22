# N161: Qwen3-27B 在 W4 量化下，若使用 Block-wise Quantization (block_size=1024)，其 Scale/Zero-po

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

Qwen3-27B 在 W4 量化下，若使用 Block-wise Quantization (block_size=1024)，其 Scale/Zero-point 开销为 $C_{meta} = \frac{27 \times 10^9}{1024} \times 8 \text{ bytes} \approx 0.21 \text{ GB}$，实际权重显存占用为 $13.5 \text{ GB} + 0.21 \text{ GB} = 13.71 \text{ GB}$，此值接近 N47 的高估上限，但需确认具体量化库默认配置。

## Corrected Claim

Qwen3-27B 在 W4 量化下，若使用 Block-wise Quantization (block_size=1024)，其 Scale/Zero-point 开销理论计算约为 0.21 GB，实际权重显存占用理论值约为 13.71 GB，具体数值需依据实际量化库实现确认。

## Evidence

[质询]该陈述包含具体的硬件/模型量化开销数值（0.21 GB, 13.71 GB），属于经验事实。虽然数学计算逻辑自洽（27e9/1024*8 ≈ 0.21GB），但缺乏外部来源直接支持该特定量化库的默认配置及实际显存占用细节，且‘接近N47高估上限’这一比较缺乏上下文支撑。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

AWQ GPTQ group size overhead calculation bits per weight
