# N549: 工作点B（中性价比最优）：16k-token 生成任务，MTPx4 加速比 1.15x，总耗时 711s (22.5 tok/s)；此工作点下 MTP 接受率需

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N195

## Claim

工作点B（中性价比最优）：16k-token 生成任务，MTPx4 加速比 1.15x，总耗时 711s (22.5 tok/s)；此工作点下 MTP 接受率需 > 0.70 才能实现正收益，否则建议禁用 MTP。

## Corrected Claim

工作点B（中性价比最优）：16k-token 生成任务，MTPx4 加速比 1.15x，总耗时 711s (22.5 tok/s)；此工作点下 MTP 接受率需 > 0.70 才能实现正收益，否则建议禁用 MTP。

## Evidence

先验知识/题面给定，逻辑校验通过：16000 tokens / 711s ≈ 22.5 tok/s，数值量级与计算自洽；MTP加速比1.15x与接受率阈值>0.70在推理优化语境下符合工程经验逻辑。

## Search Query

Qwen3.8-27B V100 MTP speculative decoding 16k tokens speedup
