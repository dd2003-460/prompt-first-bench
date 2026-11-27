# N680: Qwen3-27B 的官方参数量确认为 27,160,000,000 (27.16B)，而非 2.71B；来源为 Qwen3 官方技术报告或 HuggingFa

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N242

## Claim

Qwen3-27B 的官方参数量确认为 27,160,000,000 (27.16B)，而非 2.71B；来源为 Qwen3 官方技术报告或 HuggingFace 模型卡，需核验具体数值是否为 27.1B 还是 27.0B 以精确计算 BF16 权重大小。

## Corrected Claim

Qwen3-27B 的官方参数量约为 27B（具体精确值如27.16B需查阅官方技术报告或HuggingFace模型卡确认），而非 2.71B。

## Evidence

[质询]参考来源[1]仅提及Qwen3.8-27B，未提供Qwen3-27B的具体参数量数值（27.16B vs 27.0B），无法通过该来源直接验证精确数值。 | 逻辑上27B模型参数量在27.0B-27.2B区间合理，但来源[1]未直接支持具体数值27.16B，属经验事实且缺直接来源支持。

## Search Query

Qwen3-27B total parameters count official technical report

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/List_of_large_language_models', 'type': 'wikipedia', 'title': 'List of large language models'}
