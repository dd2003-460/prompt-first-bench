# N181: Qwen3-27B 的 num_layers 确认为 64 层（而非 72 层），hidden_size 确认为 5120（而非 4096），num_atten

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46, N47, N48

## Claim

Qwen3-27B 的 num_layers 确认为 64 层（而非 72 层），hidden_size 确认为 5120（而非 4096），num_attention_heads=40, num_key_value_heads=8 (GQA ratio 5:1)，head_dim=128；这些参数直接修正了 N108 和 N109 中的计算基数，导致 KV Cache 显存计算需重新校准

## Corrected Claim

Qwen3-27B 的架构参数（num_layers=64, hidden_size=5120, num_attention_heads=40, num_key_value_heads=8）需进一步通过官方文档或模型配置文件核实，当前基于逻辑自洽保留但降级为待确认状态。

## Evidence

[质询]该陈述包含具体的模型架构参数（num_layers, hidden_size等），属于经验事实。由于本轮检索无可用来源，无法通过外部证据直接验证这些具体数值是否准确对应 Qwen3-27B 的官方配置，存在参数记忆偏差或版本混淆的风险。 | 经验事实，逻辑自洽但缺来源支持。参数间的数学关系（如 head_dim=128, GQA ratio 5:1 等）在逻辑上自洽，但具体数值缺乏外部来源直接确认。

## Search Query

Qwen3-27B config.json num_layers hidden_size num_attention_heads
