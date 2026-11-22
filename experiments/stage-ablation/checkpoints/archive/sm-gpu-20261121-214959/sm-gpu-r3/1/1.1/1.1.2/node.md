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

父节点级核验未通过：不完备（父节点包含三个独立的关键参数：KV头数(8)、每头维度(128)和总隐藏层维度(4096)。子节点仅覆盖了KV头数及其衍生的GQA组数，完全缺失了关于每头维度(head_dim)和总隐藏层维度(hidden_size)的信息，因此不完备。）

## Search Query

Qwen3-27B GQA num_key_value_heads head_dim hidden_size
