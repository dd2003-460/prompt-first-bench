# N281: FP8 量化中 Block Size 对精度损失的影响系数：对比 per-channel 与 per-block (block_size=128) 量化策略在 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99

## Claim

FP8 量化中 Block Size 对精度损失的影响系数：对比 per-channel 与 per-block (block_size=128) 量化策略在 MMLU-Pro 上的分数差异，公式为 ΔScore_block = Score_per_channel - Score_per_block，需确定 Qwen3-27B 官方推荐或社区最佳实践的 Block Size 及其对应的分数下限。

## Corrected Claim

FP8量化中，Block Size的选择（如per-channel vs per-block）会显著影响精度损失，通常较小的Block Size（如128）能保留更多局部动态范围从而降低精度损失，但具体在Qwen3-27B上MMLU-Pro的分数差异及官方推荐值需查阅特定量化库（如llm-compressor或AutoGPTQ）的官方文档或基准测试报告，无法仅凭通用逻辑确定具体数值。

## Evidence

[质询]该陈述试图量化一个具体的经验性能指标（MMLU-Pro分数差异及具体Block Size推荐值），但缺乏任何来源支持，且不同模型、不同量化实现（如GPTQ, AWQ, SmoothQuant）下该数值差异极大，无法从第一性原理推导，属于典型的经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体数值无法从第一性原理推出）

## Search Query

FP8 quantization block size impact on LLM accuracy MMLU benchmark per-channel vs per-block
