# N73: Qwen3-27B 的 KV 头数 (num_key_value_heads) 为 8 个（采用 GQA 分组查询注意力机制，需核实 Qwen3 是否保持 8 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Qwen3-27B 的 KV 头数 (num_key_value_heads) 为 8 个（采用 GQA 分组查询注意力机制，需核实 Qwen3 是否保持 8 个 KV 头）。

## Corrected Claim

Qwen3-27B 采用 GQA 机制，其 KV 头数需进一步核实具体配置（通常 Qwen2/3 系列 27B 模型 KV 头数可能为 4 或 8，需以官方配置为准），当前证据不足以确认为 8。

## Evidence

[质询]参考来源标题及摘要中提到的模型名称为 'Qwen3.8-27B'，这与事实节点中的 'Qwen3-27B' 存在命名不一致（可能是笔误、非官方版本或不同代际），且摘要内容主要讨论显存占用和OOM问题，未直接提供 num_key_value_heads 的具体数值，无法直接证实该参数为8。 | 来源[1]提及了Qwen3系列27B模型，但名称存在差异（Qwen3.8 vs Qwen3）且未直接陈述KV头数，属于间接相关但缺乏直接数值支持；根据经验事实排除条款，硬件/模型架构参数若无直接来源支持，应降级。

## Search Query

Qwen3-27B num_key_value_heads GQA configuration

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2077080879210485277&rut=48c60b688bae8ea23dfad368eec2f0982b1f4e1191535cd6244598b10fb72fce', 'type': 'ddg', 'title': '16G甜点卡跑Qwen3.8-27B，KV缓存怎么设？ - 知乎'}
