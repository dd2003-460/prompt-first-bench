# N378: Qwen3-27B 在 INT8 AWQ 量化下的 HumanEval Pass@1 得分 69% 与 BF16 基准 72% 的绝对损失 3 个百分点，需验证

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N149

## Claim

Qwen3-27B 在 INT8 AWQ 量化下的 HumanEval Pass@1 得分 69% 与 BF16 基准 72% 的绝对损失 3 个百分点，需验证该数值是否来自 Qwen3 官方技术报告或第三方独立评测（如 CodeLlama 对比实验或 OpenCompass 代码生成基准）；若为模型先验估计，应标记 [待核验] 并参考 Qwen3-27B 官方发布的量化评测表格中 HumanEval 部分。

## Corrected Claim

Qwen3-27B 在 INT8 AWQ 量化下的 HumanEval Pass@1 得分预计较 BF16 基准有轻微下降（约 3 个百分点），具体数值需参考官方量化评测表格或独立基准测试确认。

## Evidence

[质询]具体数值（69% vs 72%）属于经验事实，缺乏官方技术报告或权威第三方评测的直接来源支持，存在数值不准确或口径混淆的风险。 | 逻辑自洽（量化导致性能轻微下降符合直觉），但作为经验事实且无可用外部来源支持，依据规则降级。

## Search Query

Qwen3-27B INT8 AWQ HumanEval Pass@1 benchmark score vs BF16 official technical report
