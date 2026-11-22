# N147: Qwen3-27B 在 32K 上下文下 KV Cache 占单卡 48GB 显存的比例为 17.07%，计算公式为 8.192 GB / 48 GB * 10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

Qwen3-27B 在 32K 上下文下 KV Cache 占单卡 48GB 显存的比例为 17.07%，计算公式为 8.192 GB / 48 GB * 100% = 17.07%，剩余显存 39.808 GB 可容纳 BF16 权重 (54.2GB) 需 offload 或量化

## Corrected Claim

Qwen3-27B 在 32K 上下文下 KV Cache 占单卡 48GB 显存的比例为 17.07%，计算公式为 8.192 GB / 48 GB * 100% = 17.07%，剩余显存 39.808 GB 可容纳 BF16 权重 (54.2GB) 需 offload 或量化

## Evidence

先验知识/题面给定，逻辑校验通过：8.192/48=17.066...%≈17.07%，48-8.192=39.808，数值计算准确且逻辑自洽。
