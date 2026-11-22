# N80: Qwen3-27B 在 BF16 精度下的 GSM8K 数学推理得分：约为 85-90%（需确认具体版本，Qwen3 系列在数学任务上表现显著提升）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

Qwen3-27B 在 BF16 精度下的 GSM8K 数学推理得分：约为 85-90%（需确认具体版本，Qwen3 系列在数学任务上表现显著提升）

## Corrected Claim

Qwen3-27B 在 BF16 精度下进行了 GSM8K 数学推理评估，具体得分需查阅完整基准报告确认（参考来源显示存在该评估，但未列出具体数值）。

## Evidence

[质询]参考来源[1]仅提及进行了GSM8K评估，但未提供具体的得分数值（85-90%），且模型名称为'Qwen3.8-27B'，与陈述中的'Qwen3-27B'存在版本标识差异，无法直接确认数值准确性。 | 来源[1]确认存在BF16精度下的GSM8K评估，但未提供具体分数，属于间接支持；作为经验事实（具体基准测试得分），缺乏直接数值支持，故降级。

## Search Query

Qwen3-27B GSM8K math reasoning score BF16

## Retrieval Sources

- {'url': 'https://github.com/sgl-project/sglang/issues/41938&rut=eb2c1cdc34a0ccb4fd980a81a38388e220eb87ec074611613b62dc1989622dd7', 'type': 'ddg', 'title': 'Benchmark: Qwen3.8-27B FP8/BF16 on H200 with float32 SSM state ... - GitHub'}
