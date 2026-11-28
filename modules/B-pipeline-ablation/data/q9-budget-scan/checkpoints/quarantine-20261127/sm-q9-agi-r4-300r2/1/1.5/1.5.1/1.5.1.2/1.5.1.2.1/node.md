# N281: INT8 量化下 Qwen3-27B 在长链逻辑推理任务（如 GSM8K-CoT 或 ARC-Challenge）的准确率下降幅度 ΔAcc_int8 = Ac

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N112

## Claim

INT8 量化下 Qwen3-27B 在长链逻辑推理任务（如 GSM8K-CoT 或 ARC-Challenge）的准确率下降幅度 ΔAcc_int8 = Acc_fp16 - Acc_int8，通常估计在 2%-5% 之间，具体取决于量化校准集的代表性；需通过本地 V100 实测 50 条典型科研推理样本验证该区间。

## Corrected Claim

INT8 量化下 Qwen3-27B 在长链逻辑推理任务的准确率通常会有一定程度的下降，具体幅度取决于量化算法、校准集质量及任务难度，建议通过本地实测确定具体区间。

## Evidence

[质询]该陈述包含具体的经验数值区间（2%-5%）和特定硬件/数据集组合（V100, 50条样本），属于经验事实而非第一性原理可推导内容；且‘通常估计’缺乏广泛公认的基准数据支持，不同量化方法（如GPTQ, AWQ, SmoothQuant）及校准策略下差异可能更大，2%-5%并非绝对通用的标准区间。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但涉及具体经验参数且无外部来源佐证，依据经验事实排除条款精神及保守原则降级）

## Search Query

INT8 quantization accuracy drop LLM logical reasoning benchmark
