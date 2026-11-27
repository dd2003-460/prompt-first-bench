# N185: Qwen3-27B 在 INT8 量化（如 SmoothQuant 或 GPTQ-Int8）下，MMLU 基准的准确率下降幅度具体数值需检索 Qwen 官方技术

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

Qwen3-27B 在 INT8 量化（如 SmoothQuant 或 GPTQ-Int8）下，MMLU 基准的准确率下降幅度具体数值需检索 Qwen 官方技术报告或第三方评测（如 LMSYS Chatbot Arena 日志），预期区间为 0.5%-1.5%，低于 N60 声称的 1.0%-2.0% 下限，需确认是否因评测集版本不同导致偏差。

## Corrected Claim

Qwen3-27B 在 INT8 量化下的 MMLU 准确率下降幅度需查阅官方报告或第三方评测确认，通常预期在 0.5%-2.0% 区间内，具体数值取决于量化方法（SmoothQuant/GPTQ）及评测集版本。

## Evidence

[质询]该陈述包含具体的经验性数值区间（0.5%-1.5%）和特定模型/量化方法的性能对比，属于硬件/模型规格类的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

Qwen3-27B INT8 quantization MMLU accuracy drop benchmark
