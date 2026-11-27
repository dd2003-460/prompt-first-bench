# N180: 在现有候选硬件中，仅 A100 80GB (80 GB) 和 H100 80GB (80 GB) 满足 67.7 GB 的 BF16 单卡显存需求；RTX A6

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

在现有候选硬件中，仅 A100 80GB (80 GB) 和 H100 80GB (80 GB) 满足 67.7 GB 的 BF16 单卡显存需求；RTX A6000 (48 GB) 和 L40S (48 GB) 均因显存不足而无法运行 BF16 版本的 Qwen3-27B，必须使用量化方案。

## Corrected Claim

在现有候选硬件中，仅 A100 80GB (80 GB) 和 H100 80GB (80 GB) 满足 67.7 GB 的 BF16 单卡显存需求；RTX A6000 (48 GB) 和 L40S (48 GB) 均因显存不足而无法运行 BF16 版本的 Qwen3-27B，必须使用量化方案。

## Evidence

先验知识/题面给定，逻辑校验通过：A100/H100 80GB显存大于67.7GB需求，RTX A6000/L40S 48GB显存小于67.7GB需求，数值比较逻辑自洽且符合硬件规格常识。
