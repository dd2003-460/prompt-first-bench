# N285: Qwen3-27B 的架构静态参数（B类，随模型版本固定）：hidden_size=4096, num_hidden_layers=32, num_attent

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102

## Claim

Qwen3-27B 的架构静态参数（B类，随模型版本固定）：hidden_size=4096, num_hidden_layers=32, num_attention_heads=32, num_key_value_heads=8 (GQA), head_dim=128, intermediate_size=11008, vocab_size=152064, 来源为HuggingFace config.json

## Corrected Claim

Qwen3-27B 的架构静态参数（B类，随模型版本固定）：hidden_size=4096, num_hidden_layers=32, num_attention_heads=32, num_key_value_heads=8 (GQA), head_dim=128, intermediate_size=11008, vocab_size=152064，来源为HuggingFace config.json（注：具体数值待外部来源确认）

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（经验事实），且参考来源显示检索失败，无法通过外部证据直接验证这些具体数值（如 hidden_size=4096, vocab_size=152064 等）的准确性。虽然参数组合在逻辑上自洽（如 32 heads * 128 dim = 4096 hidden size），但缺乏来源支持无法排除数值错误的可能性。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无可用外部证据）

## Search Query

Qwen3-27B config.json hidden_size num_hidden_layers num_key_value_heads
