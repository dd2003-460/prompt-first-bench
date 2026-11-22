# N288: Qwen3-27B 在 BF16 精度下，GSM8K 数据集的最终答案准确率（Acc_BF16_GSM8K）约为 85%-90%（参考 Qwen2.5-32B 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N121

## Claim

Qwen3-27B 在 BF16 精度下，GSM8K 数据集的最终答案准确率（Acc_BF16_GSM8K）约为 85%-90%（参考 Qwen2.5-32B 或同级模型表现，具体需 [待核验]）。此数值作为逻辑推理能力的基线。

## Corrected Claim

Qwen3-27B 在 BF16 精度下于 GSM8K 数据集上进行了基准测试（参考来源[1]），具体最终答案准确率需查阅完整基准报告，通常同级模型表现可能在 85%-90% 区间，但当前来源未提供确切数值。

## Evidence

[质询]来源[1]提及的是 'Qwen3.8-27B'（疑似笔误或非标准版本号，通常应为 Qwen3-27B 或 Qwen2.5-32B 等），且摘要仅说明进行了 GSM8K 评估，未提供具体的准确率数值（85%-90%），无法直接支持该具体数值区间。 | 来源[1]主题相关（Qwen系列模型在H200上的GSM8K基准测试），但仅确认了测试存在，未提供具体准确率数值，属于间接支持；经验事实（具体模型精度下的基准分数）缺乏直接来源支持，故降级。

## Search Query

Qwen3 27B GSM8K accuracy BF16 baseline

## Retrieval Sources

- {'url': 'https://github.com/sgl-project/sglang/issues/41938&rut=eb2c1cdc34a0ccb4fd980a81a38388e220eb87ec074611613b62dc1989622dd7', 'type': 'ddg', 'title': 'Benchmark: Qwen3.8-27B FP8/BF16 on H200 with float32 SSM state ... - GitHub'}
