# N38: Qwen3-27B 的 KV Cache 头数（num_key_value_heads）为 8 头（采用 Grouped Query Attention, GQ

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7, N8, N9

## Claim

Qwen3-27B 的 KV Cache 头数（num_key_value_heads）为 8 头（采用 Grouped Query Attention, GQA 策略），每头维度（head_dim）为 128 维，总隐藏层维度（hidden_size）为 4096 维。

## Corrected Claim

Qwen3-27B 采用 Grouped Query Attention (GQA) 策略，其 KV Cache 头数（num_key_value_heads）为 8，每头维度（head_dim）为 128，总隐藏层维度（hidden_size）为 4096。

## Evidence

父节点级核验未通过：不完备（父节点明确列出了三个关键维度参数：num_key_value_heads (8), head_dim (128), 和 hidden_size (4096)。子节点仅涵盖了 num_key_value_heads 及其衍生概念（GQA组数），完全遗漏了 head_dim 和 hidden_size 这两个关键参数，导致信息覆盖不全。）

## Search Query

Qwen3-27B GQA num_key_value_heads head_dim hidden_size
