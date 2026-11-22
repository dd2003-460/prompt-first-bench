# N441: Qwen3-27B 的架构参数确认：隐藏层维度 d_model 为 4096，注意力头数 n_heads 为 32，KV 头数 n_kv_heads 为 8 (

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N184

## Claim

Qwen3-27B 的架构参数确认：隐藏层维度 d_model 为 4096，注意力头数 n_heads 为 32，KV 头数 n_kv_heads 为 8 (GQA)，层数 n_layers 为 64。这些参数是计算每 Token KV 大小的基础。

## Corrected Claim

Qwen3-27B 的架构参数确认：隐藏层维度 d_model 为 4096，注意力头数 n_heads 为 32，KV 头数 n_kv_heads 为 8 (GQA)，层数 n_layers 为 64。这些参数是计算每 Token KV 大小的基础。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B config.json num_hidden_layers num_key_value_heads head_dim
