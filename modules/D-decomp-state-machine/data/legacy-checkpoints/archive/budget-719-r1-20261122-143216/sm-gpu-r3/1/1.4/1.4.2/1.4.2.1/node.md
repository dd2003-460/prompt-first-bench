# N174: Qwen3-27B 在 INT8 (W8A8) 精度下的 MMLU-Pro 基准测试得分，需对比 BF16 基线分数（约 70-75分区间，具体需查证）计算绝对

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

Qwen3-27B 在 INT8 (W8A8) 精度下的 MMLU-Pro 基准测试得分，需对比 BF16 基线分数（约 70-75分区间，具体需查证）计算绝对下降值，以验证是否低于 2% 的相对误差阈值。

## Corrected Claim

Qwen3-27B 在 INT8 (W8A8) 精度下的 MMLU-Pro 基准测试得分需与 BF16 基线分数对比，以评估量化带来的性能下降幅度，具体数值需查阅官方技术报告或权威基准测试数据。

## Evidence

[质询]该陈述包含具体的经验性数值（BF16基线分数约70-75分）和特定的量化误差阈值（2%相对误差），这些属于经验事实，无法从第一性原理推导，且缺乏来源支持以确认具体数值和阈值设定的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B INT8 W8A8 MMLU-Pro benchmark accuracy score
