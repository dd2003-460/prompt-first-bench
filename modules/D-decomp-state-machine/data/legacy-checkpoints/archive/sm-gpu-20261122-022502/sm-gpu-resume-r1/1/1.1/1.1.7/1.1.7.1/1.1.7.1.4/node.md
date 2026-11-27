# N486: Qwen3-27B BF16 在 GSM8K 上的基线准确率为 88.4%，需确认是否使用 Few-shot 提示（5-shot vs 8-shot），不同提示

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N149, N150, N151

## Claim

Qwen3-27B BF16 在 GSM8K 上的基线准确率为 88.4%，需确认是否使用 Few-shot 提示（5-shot vs 8-shot），不同提示格式对量化模型的影响系数不同，需检索具体提示模板

## Corrected Claim

Qwen3-27B BF16 在 GSM8K 上的基线准确率约为 88.4%（需进一步确认具体提示格式，如 5-shot 或 8-shot，不同格式对量化模型影响不同）。

## Evidence

[质询]参考来源[1]提及的是 'Qwen3.8-27B' 而非 'Qwen3-27B'，且主要关注 H200 上的速度基准和 FP8/BF16 对比，未明确提供 GSM8K 88.4% 这一具体基线数值，也未说明具体的 Few-shot 提示格式（5-shot vs 8-shot），存在版本混淆和细节缺失的风险。 | 来源[1]主题相关（Qwen3系列27B模型在GSM8K上的评估），但仅间接支持存在BF16评估，未直接证实88.4%的具体数值及提示模板细节，属于经验事实且缺乏直接来源支持。

## Search Query

Qwen3-27B GSM8K baseline accuracy BF16 few-shot prompt configuration

## Retrieval Sources

- {'url': 'https://github.com/sgl-project/sglang/issues/41938&rut=c0396d5ee9a026bf42e54912d6a050477e1c4b533bb4a9c2c9bf0d48c9178029', 'type': 'ddg', 'title': 'Benchmark: Qwen3.8-27B FP8/BF16 on H200 with float32 SSM state ... - GitHub'}
