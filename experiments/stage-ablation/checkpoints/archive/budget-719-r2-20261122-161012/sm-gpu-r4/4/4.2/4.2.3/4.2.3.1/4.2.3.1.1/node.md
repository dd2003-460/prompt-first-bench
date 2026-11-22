# N509: 工作点1（高性低成-理论上限）：RTX 4090 在 FP8 权重+BF16 KV 配置下，理论 Decode 吞吐为 1008 GB/s / 28.07 GB

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N210

## Claim

工作点1（高性低成-理论上限）：RTX 4090 在 FP8 权重+BF16 KV 配置下，理论 Decode 吞吐为 1008 GB/s / 28.07 GB ≈ 35.9 tokens/s，考虑 70% 内存控制器效率后实际约为 25.1 tokens/s，满足 >20 tokens/s 的交互体验阈值。

## Corrected Claim

工作点1（高性低成-理论上限）：RTX 4090 在 FP8 权重+BF16 KV 配置下，理论 Decode 吞吐为 1008 GB/s / 28.07 GB ≈ 35.9 tokens/s，考虑 70% 内存控制器效率后实际约为 25.1 tokens/s，满足 >20 tokens/s 的交互体验阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽 1008 GB/s 与 LLaMA-2 70B 模型在 FP8 权重+BF16 KV 下约 28.07 GB 的显存占用量级符合工程常识，计算过程 1008/28.07≈35.9 及 35.9*0.7≈25.1 逻辑自洽，且 25.1 > 20 满足阈值条件。
