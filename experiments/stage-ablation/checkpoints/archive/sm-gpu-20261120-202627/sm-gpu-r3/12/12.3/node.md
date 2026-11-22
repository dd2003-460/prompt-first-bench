# N460: 候选硬件显存容量筛选清单：A100 80GB (Pass), H100 80GB (Pass), MI300X 192GB (Pass), RTX 4090 2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N150

## Claim

候选硬件显存容量筛选清单：A100 80GB (Pass), H100 80GB (Pass), MI300X 192GB (Pass), RTX 4090 24GB (Fail for BF16 single, Pass for FP8 dual), L40S 48GB (Pass for FP8 single, Fail for BF16 single), RTX 4080 16GB (Fail), L4 24GB (Fail for BF16, Borderline for FP8 dual)。

## Corrected Claim

候选硬件显存容量筛选清单：A100 80GB (Pass), H100 80GB (Pass), MI300X 192GB (Pass), RTX 4090 24GB (Fail for BF16 single, Pass for FP8 dual), L40S 48GB (Pass for FP8 single, Fail for BF16 single), RTX 4080 16GB (Fail), L4 24GB (Fail for BF16, Borderline for FP8 dual)。

## Evidence

先验知识/题面给定，逻辑校验通过：各硬件显存容量数值符合公开规格，基于BF16/FP8精度对显存占用差异的筛选逻辑自洽（如4090 24GB在BF16下通常不足，FP8下可能通过；L40S 48GB在BF16下可能不足，FP8下通过），无内部矛盾。

## Search Query

GPU VRAM capacity list A100 H100 RTX 4090 L40S
