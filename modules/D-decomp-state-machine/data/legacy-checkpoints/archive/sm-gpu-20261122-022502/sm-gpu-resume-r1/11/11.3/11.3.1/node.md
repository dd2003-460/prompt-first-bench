# N341: Qwen3-27B 在 HumanEval (代码生成) 基准测试上的 BF16 基线 Pass@1 为 65.2% (来源: Qwen3 Technical 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N123

## Claim

Qwen3-27B 在 HumanEval (代码生成) 基准测试上的 BF16 基线 Pass@1 为 65.2% (来源: Qwen3 Technical Report Table 1)，FP8 量化后的 Pass@1 为 64.9%，绝对下降值为 0.3% (约 0.15 个测试用例)。

## Corrected Claim

Qwen3-27B 在 HumanEval 基准测试上，FP8 量化后的 Pass@1 相比 BF16 基线有轻微下降（具体数值需查阅 Qwen3 Technical Report 确认）。

## Evidence

[质询]具体数值（65.2% 和 64.9%）属于经验事实，且检索无可用来源，无法验证其精确性；此外，0.3% 的绝对下降对应约 0.15 个测试用例的计算基于 HumanEval 共 164 个测试用例（164 * 0.003 ≈ 0.49，若按 100 个算则是 0.3，此处存在量级或基数混淆的潜在风险，但主要问题是缺乏来源支持具体数值）。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证具体数值）

## Search Query

Qwen3-27B HumanEval Pass@1 score BF16 FP8 quantization
