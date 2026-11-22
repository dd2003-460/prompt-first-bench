# N71: Qwen3-27B 的 Transformer 层数 (num_layers) 为 64 层（依据 Qwen2.5-32B 同量级架构推断，需核实 Qwen3 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Qwen3-27B 的 Transformer 层数 (num_layers) 为 64 层（依据 Qwen2.5-32B 同量级架构推断，需核实 Qwen3 是否沿用或调整）。

## Corrected Claim

Qwen3-27B 采用 Decoder-Only Transformer 架构，其层数推测为 64 层（基于 Qwen2.5-32B 同量级架构类比），具体数值需查阅官方模型配置文件核实。

## Evidence

[质询]该陈述明确标注为‘依据 Qwen2.5-32B 同量级架构推断’，属于未经证实的推测。Qwen3-27B 的具体层数（num_layers）是具体的硬件/模型架构参数，属于经验事实，不能仅凭逻辑自洽或类比推断判定为 verified，且参考来源未提供具体数值支持。 | 经验事实，逻辑自洽但缺来源支持。来源[1]仅确认 Qwen3 采用 Decoder-Only Transformer 架构且结构与 Qwen2 大体相同，但未提供 Qwen3-27B 的具体层数（64层）这一数值证据。

## Search Query

Qwen3-27B model config num_layers hidden_size num_attention_heads

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1901014191235633835&rut=52a0df11cd97085ff2660bd7faf0fff72b20b46e3c91b77dd3ac31d2fc50d7f4', 'type': 'ddg', 'title': '连夜读完了Qwen3的2000行代码，我画出了Qwen3的结构图 - 知乎'}
