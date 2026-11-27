# N59: Qwen3-27B 在 FP8 精度下的 GSM8K 数学推理基准测试分数及相对于 BF16 的下降幅度（数学任务对量化更敏感，需单独量化）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Qwen3-27B 在 FP8 精度下的 GSM8K 数学推理基准测试分数及相对于 BF16 的下降幅度（数学任务对量化更敏感，需单独量化）

## Corrected Claim

Qwen3.8-27B（或 Qwen3-27B，需确认具体版本）在 FP8 精度下进行了 GSM8K 数学推理基准测试，并与 BF16 进行了对比，但具体分数及下降幅度需查阅完整报告。

## Evidence

[质询]来源标题提及的是 'Qwen3.8-27B'，而事实节点声称的是 'Qwen3-27B'，存在模型版本/名称不匹配的风险；此外，来源摘要仅说明进行了 GSM8K 评估，未提供具体的分数数值及相对于 BF16 的下降幅度，无法直接验证具体数值。 | 来源 [1] 间接支持存在 Qwen3 系列 27B 模型在 FP8 和 BF16 下的 GSM8K 基准测试，但模型名称存在细微差异（Qwen3.8 vs Qwen3），且未提供具体分数和下降幅度，属于间接支持且存在不确定性。

## Search Query

Qwen3-27B FP8 GSM8K benchmark score

## Retrieval Sources

- {'url': 'https://github.com/sgl-project/sglang/issues/41938&rut=c0396d5ee9a026bf42e54912d6a050477e1c4b533bb4a9c2c9bf0d48c9178029', 'type': 'ddg', 'title': 'Benchmark: Qwen3.8-27B FP8/BF16 on H200 with float32 SSM state ... - GitHub'}
