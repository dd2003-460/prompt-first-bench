# N241: W4A8 量化的质量损失量化基准：Qwen3-27B W4A8 在 MMLU 基准上的准确率下降通常为 1.5-2.5% (相对 BF16)，在 HumanEv

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

W4A8 量化的质量损失量化基准：Qwen3-27B W4A8 在 MMLU 基准上的准确率下降通常为 1.5-2.5% (相对 BF16)，在 HumanEval 代码生成任务上下降 3-5%。若 '可接受阈值' 定义为 MMLU 下降 < 2% 且 HumanEval 下降 < 5%，则 W4A8 处于边界可行区域；若阈值更严 (MMLU < 1%)，则 W4A8 不可行，需回退至 INT8。

## Corrected Claim

W4A8 量化通常会导致模型性能下降，具体幅度取决于量化算法和校准数据。一般而言，MMLU 下降可能在 1-3% 左右，HumanEval 下降可能在 2-5% 左右。若阈值严格（如 MMLU < 1%），W4A8 可能不满足要求，需考虑 INT8 或更精细的量化策略。

## Evidence

[质询]具体数值范围（MMLU 1.5-2.5%, HumanEval 3-5%）属于特定模型版本和量化实现的经验数据，不同量化算法（如GPTQ, AWQ, SmoothQuant）及校准集差异会导致结果波动，且缺乏来源支持该特定数值区间为通用基准。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3 27B W4A8 quantization MMLU accuracy drop benchmark
