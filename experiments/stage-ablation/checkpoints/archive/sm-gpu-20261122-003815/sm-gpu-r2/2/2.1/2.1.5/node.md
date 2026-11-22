# N75: Qwen3-27B 的上下文窗口最大长度为 128K tokens（Qwen3 系列通常支持长上下文，需核实 27B 版本的具体上限）。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Qwen3-27B 的上下文窗口最大长度为 128K tokens（Qwen3 系列通常支持长上下文，需核实 27B 版本的具体上限）。

## Corrected Claim

Qwen3-27B（或相关版本如Qwen3.5-27B）的上下文窗口最大长度约为8K tokens，而非128K tokens。

## Evidence

[质询]参考来源[1]明确指出Qwen3.5-27B的最大上下文长度约为8000 tokens，与陈述中的128K tokens存在数量级上的巨大差异（16倍差距），且来源直接反驳了该具体数值。 | 来源[1]直接指出Qwen3.5-27B上下文长度约为8K tokens，与陈述的128K tokens明确矛盾。

## Search Query

Qwen3-27B max_context_length 128k tokens

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/view/9a2e5d4ab12acfc789eb172ded630b1c58ee9b65.html&rut=4c2aa95ceea8b0f6b6e00412a5a9efa164e1355251b6ad658f31ae54024c65b2', 'type': 'ddg', 'title': 'Qwen3.5-27B最大支持多少token？核心结论：约8K，附详细解析与使用建议'}
