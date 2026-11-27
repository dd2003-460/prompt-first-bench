# N204: W4 精度下 Qwen3-27B 的 Quality Factor (QF) 量化值，基于 GSM8K 和 MMLU 基准测试的准确率下降幅度，预期 QF_W4

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

W4 精度下 Qwen3-27B 的 Quality Factor (QF) 量化值，基于 GSM8K 和 MMLU 基准测试的准确率下降幅度，预期 QF_W4 在 0.92-0.95 区间，需引用具体量化算法（如 AWQ, GPTQ, SmoothQuant）的评测报告

## Corrected Claim

W4 精度下 Qwen3-27B 的 Quality Factor (QF) 量化值受具体量化算法（如 AWQ, GPTQ, SmoothQuant）影响显著，需引用特定算法在 GSM8K 和 MMLU 基准测试上的实测准确率下降幅度来确定 QF_W4 的具体数值，而非预设固定区间。

## Evidence

[质询]该陈述包含具体的经验性数值区间（0.92-0.95）和特定模型/精度组合的性能预期，属于硬件/模型性能经验事实，无法从第一性原理推导，且缺乏具体量化算法（AWQ/GPTQ等）的明确指定，不同算法下QF波动可能超出该区间。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值区间及算法依赖关系）

## Search Query

Qwen3-27B 4-bit quantization quality degradation GSM8K MMLU accuracy drop
