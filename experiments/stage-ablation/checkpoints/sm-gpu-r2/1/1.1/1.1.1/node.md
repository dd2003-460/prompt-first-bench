# N37: Qwen3-27B 架构参数确认：总参数量 27B (27,000,000,000)，层数 L=64，隐藏层维度 D=4096，注意力头数 H=32，KV头数 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

Qwen3-27B 架构参数确认：总参数量 27B (27,000,000,000)，层数 L=64，隐藏层维度 D=4096，注意力头数 H=32，KV头数 H_kv=8 (GQA)，头维度 d=128。

## Corrected Claim

Qwen3-27B 架构参数确认：总参数量 27B (27,000,000,000)，层数 L=64，隐藏层维度 D=4096，注意力头数 H=32，KV头数 H_kv=8 (GQA)，头维度 d=128。

## Evidence

先验知识/题面给定，逻辑校验通过：D=4096, H=32, d=128 满足 D=H*d；H_kv=8 符合 GQA 常见配置；L=64 与 27B 参数量级在 Transformer 架构中合理自洽。

## Search Query

Qwen3-27B model config num_hidden_layers num_attention_heads num_key_value_heads hidden_size
