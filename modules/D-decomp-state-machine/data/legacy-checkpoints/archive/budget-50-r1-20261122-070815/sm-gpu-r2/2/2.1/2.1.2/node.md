# N56: Qwen3-27B 在 BF16 精度下的 GSM8K 数学推理基准测试分数（具体数值需检索，作为逻辑/数学能力基准线）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

Qwen3-27B 在 BF16 精度下的 GSM8K 数学推理基准测试分数（具体数值需检索，作为逻辑/数学能力基准线）

## Corrected Claim

Qwen3-27B（或相关版本如Qwen3.8-27B）在 BF16 精度下进行了 GSM8K 数学推理基准测试，具体分数需查阅完整报告或官方技术文档确认。

## Evidence

[质询]参考来源[1]提及的是 'Qwen3.8-27B' 而非 'Qwen3-27B'，且摘要中仅说明进行了 GSM8K 评估（'2 GSM8K evaluations'），并未提供具体的分数数值，存在模型版本名称不匹配及具体数值缺失的问题。 | 来源[1]主题相关但模型名称存在细微差异（Qwen3.8 vs Qwen3），且未直接提供具体分数数值，仅证实进行了相关基准测试，属于间接支持且无法排除版本差异导致的数值偏差，故降级。

## Search Query

Qwen3-27B BF16 GSM8K benchmark score

## Retrieval Sources

- {'url': 'https://github.com/sgl-project/sglang/issues/41938&rut=c0396d5ee9a026bf42e54912d6a050477e1c4b533bb4a9c2c9bf0d48c9178029', 'type': 'ddg', 'title': 'Benchmark: Qwen3.8-27B FP8/BF16 on H200 with float32 SSM state ... - GitHub'}
