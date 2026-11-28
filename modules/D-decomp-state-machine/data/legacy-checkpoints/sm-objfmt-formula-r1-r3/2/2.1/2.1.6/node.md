# N59: Qwen3-27B 的 Transformer 架构具体参数：num_layers = 64, hidden_dim = 4096, num_attention

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10, N11, N12

## Claim

Qwen3-27B 的 Transformer 架构具体参数：num_layers = 64, hidden_dim = 4096, num_attention_heads = 32, head_dim = 128, num_key_value_heads = 8 (GQA 配置)

## Corrected Claim

Qwen3-27B 采用 Transformer 架构，具体参数包括 num_layers、hidden_dim 等，需查阅官方技术报告确认精确数值。

## Evidence

[质询]具体架构参数（如层数、隐藏维度、注意力头数）属于经验事实，无法从第一性原理推导，且当前无可用来源验证其准确性，存在参数记忆错误或版本混淆的风险。 | 经验事实，逻辑自洽（head_dim=hidden_dim/num_heads=128，GQA配置合理）但缺来源支持

## Search Query

Qwen3-27B architecture config num_layers hidden_dim num_key_value_heads
