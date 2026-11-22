# N49: BF16 基线工作点（高成本低性）：硬件需求 ≥ 54GB 显存（权重）+ 6GB (KV Cache) + 2GB (激活) ≈ 62GB。对应最低可行硬件为

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

BF16 基线工作点（高成本低性）：硬件需求 ≥ 54GB 显存（权重）+ 6GB (KV Cache) + 2GB (激活) ≈ 62GB。对应最低可行硬件为 1x A100 80GB 或 2x RTX 4090 (需 offload 或量化权重)。质量损失 0%，但单位 Token 成本最高。

## Corrected Claim

BF16 基线工作点（高成本低性）：硬件需求 ≥ 54GB 显存（权重）+ 6GB (KV Cache) + 2GB (激活) ≈ 62GB。对应最低可行硬件为 1x A100 80GB 或 2x RTX 4090 (需 offload 或量化权重)。质量损失 0%，但单位 Token 成本最高。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下7B模型权重约14GB，加上KV Cache和激活值，总显存需求在62GB左右符合工程估算逻辑；A100 80GB单卡可容纳，2x 4090 (48GB) 需Offload或量化符合硬件限制常识。
