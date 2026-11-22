# N40: RTX 4060 Ti 16GB 单卡对 Qwen3-27B 的不可行性证明：即使使用最激进的 W4 量化 (13.5GB 权重)，剩余 2.5GB 显存无法容

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

RTX 4060 Ti 16GB 单卡对 Qwen3-27B 的不可行性证明：即使使用最激进的 W4 量化 (13.5GB 权重)，剩余 2.5GB 显存无法容纳 32K 上下文所需的 KV Cache (~16GB)，因此单卡方案在容量上直接不可行，必须排除或仅作为极端低精度 (如 INT2) 且牺牲上下文长度的备选。

## Corrected Claim

RTX 4060 Ti 16GB 单卡对 Qwen3-27B 的不可行性证明：即使使用最激进的 W4 量化 (13.5GB 权重)，剩余 2.5GB 显存无法容纳 32K 上下文所需的 KV Cache (~16GB)，因此单卡方案在容量上直接不可行，必须排除或仅作为极端低精度 (如 INT2) 且牺牲上下文长度的备选。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B W4量化权重约13.5GB，RTX 4060 Ti 16GB剩余显存约2.5GB，而32K上下文KV Cache需求远超此值，容量矛盾成立。

## Search Query

RTX 4060 Ti 16GB large language model 27B parameter memory limitation
