# N348: 候选硬件全集的筛选阈值定义：显存容量下限为 24GB（以容纳 W4 权重 + 32K FP8 KV Cache + 开销），带宽下限为 900 GB/s（以确保

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

候选硬件全集的筛选阈值定义：显存容量下限为 24GB（以容纳 W4 权重 + 32K FP8 KV Cache + 开销），带宽下限为 900 GB/s（以确保 W4 量化下 Decode 吞吐 > 25 tokens/s），价格上限设定为 $15,000（排除 H100 等超高端卡，聚焦消费级与专业级中端市场），该阈值集用于剔除 MI300X（生态风险高）和 H100（性价比劣势）等选项。

## Corrected Claim

候选硬件全集的筛选阈值定义：显存容量下限为 24GB（以容纳 W4 权重 + 32K FP8 KV Cache + 开销），带宽下限为 900 GB/s（以确保 W4 量化下 Decode 吞吐 > 25 tokens/s），价格上限设定为 $15,000（排除 H100 等超高端卡，聚焦消费级与专业级中端市场），该阈值集用于剔除 MI300X（生态风险高）和 H100（性价比劣势）等选项。

## Evidence

检索失败: no sources from any channel (all 5 failed)
