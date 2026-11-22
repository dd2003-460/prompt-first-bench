# N39: Qwen3-27B 的 head_dim（头维度）具体数值，通常由 hidden_size / num_attention_heads 得出，需确认是否为标准 

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

Qwen3-27B 的 head_dim（头维度）具体数值，通常由 hidden_size / num_attention_heads 得出，需确认是否为标准 128 或非标准值。

## Corrected Claim

Qwen3-27B 的 head_dim 通常由 hidden_size / num_attention_heads 得出，具体数值需查阅官方模型配置以确认是否为标准 128 或非标准值。

## Evidence

父节点级核验未通过：不完备（子节点仅提供了计算所需的两个输入参数（hidden_size 和 num_attention_heads），但父节点的核心目标是确认 head_dim 的具体数值及其是否标准。分解缺少了“执行除法计算”或“得出最终 head_dim 结论”这一关键步骤，导致无法直接回答父节点关于“具体数值”和“是否标准”的问题，属于过程不完备。）

## Search Query

Qwen3-27B head_dim hidden_size num_attention_heads config.json
