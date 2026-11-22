# N101: INT4/W4量化下，Qwen3-27B的权重显存占用计算需包含量化组尺度（Scale/Zero-point）开销：若采用Group Size 128，每128

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

INT4/W4量化下，Qwen3-27B的权重显存占用计算需包含量化组尺度（Scale/Zero-point）开销：若采用Group Size 128，每128个权重需额外1个FP16 scale (2 bytes) 和1个FP16 zero-point (2 bytes)，即每权重额外增加 (4 bytes / 128) = 0.03125 bytes/weight，总权重显存 ≈ 13.5GB + (27B * 0.03125) ≈ 14.34GB。

## Corrected Claim

INT4/W4量化下，Qwen3-27B的权重显存占用计算需包含量化组尺度（Scale/Zero-point）开销：若采用Group Size 128，每128个权重需额外1个FP16 scale (2 bytes) 和1个FP16 zero-point (2 bytes)，即每权重额外增加 (4 bytes / 128) = 0.03125 bytes/weight，总权重显存 ≈ 13.5GB + (27B * 0.03125) ≈ 14.34GB。

## Evidence

先验知识/题面给定，逻辑校验通过：INT4权重基础占用13.5GB，Group Size 128下每权重额外开销0.03125 bytes，27B参数额外开销约0.84GB，总显存约14.34GB，计算逻辑自洽且数值量级合理。

## Search Query

GPTQ AWQ group size 128 overhead calculation bytes per weight
