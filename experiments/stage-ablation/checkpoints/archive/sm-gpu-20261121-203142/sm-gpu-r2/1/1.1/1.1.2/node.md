# N36: Qwen3-27B的KV Cache参数确认：hidden_size=4096, num_attention_heads=32, num_key_value_h

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3-27B的KV Cache参数确认：hidden_size=4096, num_attention_heads=32, num_key_value_heads=8, num_hidden_layers=64（需从HuggingFace配置文件中验证，若不同则修正N10中的层数假设）

## Corrected Claim

Qwen3-27B（或 Qwen3.8-27B）的 KV Cache 参数确认：num_hidden_layers=64，采用混合注意力机制（16层全注意力+48层线性注意力）。hidden_size、num_attention_heads 和 num_key_value_heads 需进一步从 HuggingFace 配置文件直接验证以确认具体数值。

## Evidence

[质询]来源标题及内容明确指向 'Qwen3.8-27B'，而待核验事实为 'Qwen3-27B'。虽然两者可能指代同一模型系列的不同版本或笔误，但来源并未直接确认 'Qwen3-27B' 的具体配置参数（如 hidden_size=4096, num_attention_heads=32 等），仅提供了层数（64层）和注意力机制结构（16层全注意力+48层线性注意力）的间接信息。此外，来源未直接列出 hidden_size 和 head 数量，需依赖外部常识或进一步验证，存在版本混淆或参数不匹配的风险。 | 来源[1]间接支持了 num_hidden_layers=64 这一参数，并描述了混合注意力机制，但未直接提供 hidden_size、num_attention_heads 和 num_key_value_heads 的具体数值，且模型名称存在 'Qwen3.8' 与 'Qwen3' 的细微差异，无法完全排除版本差异导致的参数不同。

## Search Query

Qwen3-27B hidden_size num_attention_heads num_key_value_heads num_hidden_layers

## Retrieval Sources

- {'url': 'https://github.com/wuhy80/wuhy-notes/blob/main/%E5%A4%A7%E6%A8%A1%E5%9E%8B/04-%E9%83%A8%E7%BD%B2%E4%B8%8E%E5%B7%A5%E5%85%B7%E9%93%BE/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/Qwen3.8-27B%20%E6%98%BE%E5%AD%98%E4%B8%8E%20KV%20Cache%20%E9%A2%84%E7%AE%97.md&rut=a94eec89f1a98dac6ec35d4ca8663ef3619808cf53158f3466fe82f509863d12', 'type': 'ddg', 'title': 'Qwen3.8-27B 显存与 KV Cache 预算.md - GitHub'}
