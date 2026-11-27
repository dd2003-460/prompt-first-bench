# N17: FP8 精度（E4M3/E5M2）对 LLM 推理的质量损失通常在 0.1-0.5 BLEU 或 1-2% 准确率下降，需引用 Qwen 官方或第三方评测数据确

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

FP8 精度（E4M3/E5M2）对 LLM 推理的质量损失通常在 0.1-0.5 BLEU 或 1-2% 准确率下降，需引用 Qwen 官方或第三方评测数据确认 27B 模型在 FP8 下的具体退化幅度。

## Corrected Claim

FP8 精度（E4M3/E5M2）通常能保持 LLM 推理的高质量，具体质量损失（如 BLEU 或准确率下降幅度）因模型规模、架构及任务类型而异，需引用特定模型（如 Qwen 27B）在特定基准下的官方或第三方评测数据以确认具体退化幅度。

## Evidence

[质询]该陈述包含具体的经验性数值范围（0.1-0.5 BLEU 或 1-2% 准确率下降），属于硬件/模型性能的经验事实，无法从第一性原理推导。且不同模型架构、任务类型（如代码生成 vs 通用对话）及评测基准下，FP8 的退化幅度差异显著，统一给出此范围缺乏普适性依据，存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值范围及 Qwen 27B 的具体退化数据）

## Search Query

Qwen3-27B FP8 quantization quality loss benchmark BLEU accuracy
