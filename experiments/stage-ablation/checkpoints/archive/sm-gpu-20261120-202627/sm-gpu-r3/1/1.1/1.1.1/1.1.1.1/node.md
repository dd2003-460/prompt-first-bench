# N155: Attention 模块参数量公式展开：Params_Attention = (Q_proj + K_proj + V_proj + O_proj)，其中 Q_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Attention 模块参数量公式展开：Params_Attention = (Q_proj + K_proj + V_proj + O_proj)，其中 Q_proj = hidden_dim * num_heads * head_dim, K_proj = hidden_dim * num_kv_heads * head_dim, V_proj = hidden_dim * num_kv_heads * head_dim, O_proj = hidden_dim * hidden_dim。

## Corrected Claim

Attention 模块参数量公式展开：Params_Attention = (Q_proj + K_proj + V_proj + O_proj)，其中 Q_proj = hidden_dim * num_heads * head_dim, K_proj = hidden_dim * num_kv_heads * head_dim, V_proj = hidden_dim * num_kv_heads * head_dim, O_proj = hidden_dim * hidden_dim。

## Evidence

先验知识/题面给定，逻辑校验通过
