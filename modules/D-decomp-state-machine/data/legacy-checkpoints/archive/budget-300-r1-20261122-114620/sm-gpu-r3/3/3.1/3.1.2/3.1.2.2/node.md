# N281: Qwen3-27B 在 MMLU 基准上的 BF16 基准准确率具体数值：根据 Qwen3 官方技术报告，Qwen3-27B 在 MMLU 上的准确率为 70.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N87

## Claim

Qwen3-27B 在 MMLU 基准上的 BF16 基准准确率具体数值：根据 Qwen3 官方技术报告，Qwen3-27B 在 MMLU 上的准确率为 70.0% (需精确核对)。该数值是计算 BF16 与 FP32 差异的基准。若 BF16 Acc=70.0%，则 0.5% 的相对差异阈值为 0.35 个百分点，即 BF16 与 FP32 的准确率差值必须 <0.35% 才能视为统计上不显著。

## Corrected Claim

Qwen3-27B 在 MMLU 基准上的 BF16 基准准确率约为 70%（具体数值需以官方技术报告为准）。若基准准确率为 X%，则 0.5% 的相对差异阈值为 0.005*X 个百分点。

## Evidence

[质询]具体数值 70.0% 属于经验事实，且检索无可用来源支持，无法确认该精确数值是否准确（Qwen3-27B 在 MMLU 上的实际得分可能略有不同，例如 69.x% 或 71.x%），存在数值偏差风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证 70.0% 这一具体数值）

## Search Query

Qwen3-27B official technical report MMLU accuracy
