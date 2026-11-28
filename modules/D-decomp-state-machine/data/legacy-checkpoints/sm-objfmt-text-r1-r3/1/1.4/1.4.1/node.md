# N32: Qwen3-27B 的架构参数：n_layers=64, hidden_size=4096, num_attention_heads=32, num_key_v

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

Qwen3-27B 的架构参数：n_layers=64, hidden_size=4096, num_attention_heads=32, num_key_value_heads=8 (GQA), head_dim=128, intermediate_size=11008。

## Corrected Claim

Qwen3-27B 的架构参数：n_layers=64, hidden_size=4096, num_attention_heads=32, num_key_value_heads=8 (GQA), head_dim=128, intermediate_size=11008。

## Evidence

父节点级核验未通过：不完备（子节点分别关注KV Cache增长、GQA对显存的优化以及FFN权重占比，三者主题不重叠且无矛盾，满足正交性。但父节点中明确列出的 `head_dim=128` 未在任何一个子节点中被解释或关联到具体影响（如注意力计算量或头内维度特性），导致关键参数覆盖不全，不满足完备性。各子节点针对不同参数组合及其工程意义，不存在冗余。）
