# N179: 考虑到 15% 的运行时碎片/激活峰值开销，Qwen3-27B BF16 单卡推理的最小显存需求为 67.7 GB (58.9 * 1.15)，这要求 GPU 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

考虑到 15% 的运行时碎片/激活峰值开销，Qwen3-27B BF16 单卡推理的最小显存需求为 67.7 GB (58.9 * 1.15)，这要求 GPU 显存至少为 68 GB 才能稳定运行。

## Corrected Claim

考虑到 15% 的运行时碎片/激活峰值开销，Qwen3-27B BF16 单卡推理的最小显存需求为 67.7 GB (58.9 * 1.15)，这要求 GPU 显存至少为 68 GB 才能稳定运行。

## Evidence

先验知识/题面给定，逻辑校验通过：58.9 * 1.15 = 67.735，四舍五入为 67.7 GB，且 67.7 GB 确实要求至少 68 GB 显存，计算与逻辑自洽。
