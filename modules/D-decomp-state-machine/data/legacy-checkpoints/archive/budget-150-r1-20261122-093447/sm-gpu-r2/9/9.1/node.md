# N120: 显存容量决策树阈值验证：Qwen3-27B 在 32K ctx 下，W4 精度总需求 ~20.7GB (N13)，刚好低于 24GB 单卡上限，但需预留 1-2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

显存容量决策树阈值验证：Qwen3-27B 在 32K ctx 下，W4 精度总需求 ~20.7GB (N13)，刚好低于 24GB 单卡上限，但需预留 1-2GB 运行时开销，实际可用显存需 ≥ 22GB；RTX 4090 (24GB) 可行但无余量，RTX 3090 (24GB) 可行但无余量，若 batch_size>1 或 ctx>32K 则必须双卡

## Corrected Claim

显存容量决策树阈值验证：Qwen3-27B 在 32K ctx 下，W4 精度总需求 ~20.7GB (N13)，刚好低于 24GB 单卡上限，但需预留 1-2GB 运行时开销，实际可用显存需 ≥ 22GB；RTX 4090 (24GB) 可行但无余量，RTX 3090 (24GB) 可行但无余量，若 batch_size>1 或 ctx>32K 则必须双卡

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数W4量化约13.5GB，32K上下文KV Cache及激活值估算约7-8GB，总和约20.7GB，符合24GB显存限制下的推理逻辑。
