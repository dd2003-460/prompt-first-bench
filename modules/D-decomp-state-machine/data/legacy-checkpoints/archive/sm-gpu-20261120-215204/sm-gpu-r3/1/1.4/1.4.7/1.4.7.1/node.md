# N187: H100 SXM5 在 FP8 精度下运行 Qwen3-27B 的生成速度理论上限为 3350 GB/s / 27 GB ≈ 124 Tokens/s，考虑 H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

H100 SXM5 在 FP8 精度下运行 Qwen3-27B 的生成速度理论上限为 3350 GB/s / 27 GB ≈ 124 Tokens/s，考虑 Hopper 架构在 LLM 推理中较高的内存带宽利用率 (80-90%)，实际预期速度为 99-112 Tokens/s，显著高于 A100 的 59 Tokens/s。

## Corrected Claim

H100 SXM5 在 FP8 精度下运行 Qwen3-27B 的生成速度理论上限为 3350 GB/s / 27 GB ≈ 124 Tokens/s，考虑 Hopper 架构在 LLM 推理中较高的内存带宽利用率 (80-90%)，实际预期速度为 99-112 Tokens/s，显著高于 A100 的 59 Tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 带宽 3350 GB/s 与 Qwen3-27B 模型大小 27 GB 均为公认工程参数，算术推导 3350/27≈124 正确，带宽利用率 80-90% 符合 Hopper 架构 LLM 推理经验值，结论逻辑自洽且量级合理。
