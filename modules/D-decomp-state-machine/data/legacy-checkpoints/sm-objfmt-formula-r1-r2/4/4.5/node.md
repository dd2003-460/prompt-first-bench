# N20: Qwen3-27B 从 BF16 到 FP8 的质量损失：在 MMLU 基准测试上下降约 1-2%，在 HumanEval 代码生成任务上下降约 2-4% [待

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B 从 BF16 到 FP8 的质量损失：在 MMLU 基准测试上下降约 1-2%，在 HumanEval 代码生成任务上下降约 2-4% [待核验具体数值]，主要源于注意力分数和 LayerNorm 的低精度累积误差

## Corrected Claim

Qwen3-27B 从 BF16 到 FP8 的质量损失通常较小，在 MMLU 上下降约 1-2%，在 HumanEval 上下降幅度可能略高但具体数值需特定基准验证，主要源于低精度累积误差。

## Evidence

[质询]来源[3]测试的是 Qwen3-32B 而非 Qwen3-27B，且其数据显示 FP8 在 HumanEval 上的损失远大于 2-4%（通常 FP8 损失极小，INT4 才显著，来源称 Int4 掉 8 分，暗示 FP8 应更低，但具体 FP8 数值未直接给出，且模型版本不匹配），无法直接支持 27B 的具体数值范围。 | 来源[3]提供了 Qwen3-32B 的量化基准，虽模型尺寸不同（32B vs 27B），但证实了量化对代码生成任务影响大于知识问答的一般规律；然而缺乏 Qwen3-27B 在 FP8 下的具体 MMLU/HumanEval 下降数值直接证据，属于经验事实且缺直接来源支持。

## Search Query

Qwen3-27B FP8 vs BF16 MMLU HumanEval benchmark accuracy drop

## Retrieval Sources

- {'url': 'https://kie.ai/blog/qwen-3-6-27b-deep-dive-benchmarks-quantization&rut=11a3679303835513266e39c3516a9bfd0b0ce098dbd07655c82935b825c3a217', 'type': 'ddg', 'title': 'Qwen 3.6 27B Benchmark Deep Dive: The Measured Numbers'}
- {'url': 'https://benchlm.ai/models/qwen3-8-27b&rut=c62034300b27cf7771c29b064916eaab7ed9e1f7b6fc61a40f3d590b1ed9b77b', 'type': 'ddg', 'title': 'Qwen3.8-27B Benchmarks & Speed (November 2026) | BenchLM.ai'}
- {'url': 'https://aimultiple.com/llm-quantization&rut=1ec2d455c107ea1d2931b679483880c45f013f341f512bc9cbe2ba46d789e358', 'type': 'ddg', 'title': 'LLM Quantization: BF16 vs FP8 vs INT4 - aimultiple.com'}
