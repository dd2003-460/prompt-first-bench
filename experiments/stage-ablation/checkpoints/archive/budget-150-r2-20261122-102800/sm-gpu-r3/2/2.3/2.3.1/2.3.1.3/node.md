# N224: 工作点3（低显存/高延迟/W4）：总显存需求 17.04 GB，单卡 RTX 4090 (24GB) 可行，单卡 A100-40GB 可行，单卡 H100-80

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

工作点3（低显存/高延迟/W4）：总显存需求 17.04 GB，单卡 RTX 4090 (24GB) 可行，单卡 A100-40GB 可行，单卡 H100-80GB 可行，显存约束最宽松，但质量损失最大（GSM8K 下降 10-15%）。

## Corrected Claim

工作点3（低显存/高延迟/W4）：总显存需求 17.04 GB，单卡 RTX 4090 (24GB) 可行，单卡 A100-40GB 可行，单卡 H100-80GB 可行，显存约束最宽松，但质量损失最大（GSM8K 下降 10-15%）。

## Evidence

先验知识/题面给定，逻辑校验通过：17.04GB显存需求低于RTX 4090(24GB)、A100-40GB及H100-80GB的显存上限，硬件可行性判断正确；W4量化通常伴随较大的精度损失，GSM8K下降10-15%符合经验规律。
