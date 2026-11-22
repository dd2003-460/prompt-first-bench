# N35: Qwen3-27B 的精确参数总量（Total Parameters）需从 HuggingFace 模型卡或 config.json 中提取，以修正 27B 的

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

Qwen3-27B 的精确参数总量（Total Parameters）需从 HuggingFace 模型卡或 config.json 中提取，以修正 27B 的近似值（例如实际可能是 26.8B 或 27.2B），从而精确计算各精度下的权重字节数（Bytes = Params * Bits/8）。

## Corrected Claim

Qwen3-27B 的近似参数总量为 27B（270亿），精确参数总量需查阅 HuggingFace 模型卡或 config.json 中的 total_parameters 字段以获取确切数值（例如 26.8B 或 27.2B），进而精确计算各精度下的权重字节数。

## Evidence

[质询]该陈述是一个操作指令（需从HuggingFace提取精确值），而非一个已验证的事实结论。参考来源仅提供了近似值“270亿参数”，并未提供精确的Total Parameters数值（如26.8B或27.2B），因此无法通过现有来源直接验证“精确参数总量”这一具体数值，且来源标题中的“Qwen 3.6”与陈述中的“Qwen3”存在版本命名上的潜在混淆（尽管通常指代同一系列，但精确数值需以官方config为准）。 | 来源[1]仅提及“270亿参数”这一近似值，未提供config.json中的精确Total Parameters数值，属于经验事实且缺乏直接来源支持精确数值，故降级。

## Search Query

Qwen3-27B huggingface config.json num_parameters total

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2055287697623856945&rut=9eeddf0f14c1c269f39d9ab19c2f4848dd4aa0eac931137b38cbe095a39ec949', 'type': 'ddg', 'title': 'Qwen 3.6 27B深度评测：27B参数单挑397B，本地跑AI编程的时代来了'}
