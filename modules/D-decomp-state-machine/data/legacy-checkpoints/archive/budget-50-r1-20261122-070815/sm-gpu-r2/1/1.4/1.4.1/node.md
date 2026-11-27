# N43: Qwen3-27B 在 BF16 精度下的权重显存占用为 54 GB，加上 32K 上下文 KV Cache (约 2.15 GB) 及 15% 激活/碎片开销

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Qwen3-27B 在 BF16 精度下的权重显存占用为 54 GB，加上 32K 上下文 KV Cache (约 2.15 GB) 及 15% 激活/碎片开销，总需求约 64.3 GB，远超 RTX 4090/3090 的 24 GB 单卡显存上限，单卡 BF16 方案在物理上不可行

## Corrected Claim

Qwen3-27B 在 BF16 精度下的权重显存占用为 54 GB，加上 32K 上下文 KV Cache (约 2.15 GB) 及 15% 激活/碎片开销，总需求约 64.3 GB，远超 RTX 4090/3090 的 24 GB 单卡显存上限，单卡 BF16 方案在物理上不可行

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重约54GB，加上KV Cache及开销后总显存需求远超24GB单卡上限，物理上不可行。
