# N372: BF16 精度下 Qwen3-27B 在 RTX 4090 (24GB) 上因显存不足 (需 65.6GB) 导致的不可行性，具体量化为：显存缺口 = 65.6

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

BF16 精度下 Qwen3-27B 在 RTX 4090 (24GB) 上因显存不足 (需 65.6GB) 导致的不可行性，具体量化为：显存缺口 = 65.6GB - 24GB = 41.6GB，必须通过 offload 或降精度解决。

## Corrected Claim

BF16 精度下 Qwen3-27B 在 RTX 4090 (24GB) 上因显存不足 (需 65.6GB) 导致的不可行性，具体量化为：显存缺口 = 65.6GB - 24GB = 41.6GB，必须通过 offload 或降精度解决。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数模型在BF16下权重占用约54GB，加上KV Cache及激活值，总显存需求65.6GB符合工程估算量级；24GB显存确实无法容纳，缺口计算41.6GB数学正确。
