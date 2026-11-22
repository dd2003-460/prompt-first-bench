# N146: Qwen3-27B 在 32K 上下文下 KV Cache 占单卡 24GB 显存的比例为 34.13%，计算公式为 8.192 GB / 24 GB * 10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

Qwen3-27B 在 32K 上下文下 KV Cache 占单卡 24GB 显存的比例为 34.13%，计算公式为 8.192 GB / 24 GB * 100% = 34.13%，剩余显存 15.808 GB 需容纳权重和激活值

## Corrected Claim

Qwen3-27B 在 32K 上下文下 KV Cache 占单卡 24GB 显存的比例为 34.13%，计算公式为 8.192 GB / 24 GB * 100% = 34.13%，剩余显存 15.808 GB 需容纳权重和激活值

## Evidence

先验知识/题面给定，逻辑校验通过：8.192/24=0.341333...≈34.13%，24-8.192=15.808，数值计算准确且量纲一致。
