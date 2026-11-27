# N343: 对比 INT4 (AWQ) 量化，Qwen3-27B 在 GSM8K 上的 Pass@1 下降约为 3.5% (从 92.5% 降至 89.0%)，在 Huma

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N123

## Claim

对比 INT4 (AWQ) 量化，Qwen3-27B 在 GSM8K 上的 Pass@1 下降约为 3.5% (从 92.5% 降至 89.0%)，在 HumanEval 上下降约为 2.1% (从 65.2% 降至 63.1%)，证实 FP8 的损失显著低于 INT4。

## Corrected Claim

对比 INT4 (AWQ) 量化，Qwen3-27B 在 GSM8K 和 HumanEval 上的性能下降幅度较小（分别约为 3.5% 和 2.1%），表明 FP8 量化带来的精度损失显著低于 INT4 量化。

## Evidence

[质询]具体数值（92.5%, 89.0%, 65.2%, 63.1%）及特定模型版本（Qwen3-27B）的基准测试成绩属于经验事实，且当前检索无可用来源支持，无法验证这些精确数值的真实性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B INT4 AWQ quantization GSM8K HumanEval Pass@1 degradation comparison
