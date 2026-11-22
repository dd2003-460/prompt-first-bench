# N255: Qwen3-27B 模型架构确认：num_attention_layers=32 (非16)，num_kv_heads=8 (GQA)，head_dim=128

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83, N84, N85

## Claim

Qwen3-27B 模型架构确认：num_attention_layers=32 (非16)，num_kv_heads=8 (GQA)，head_dim=128，hidden_size=4096。此参数组合是计算 KV Cache 和 Weights 内存占用的唯一有效基础，修正 N89/N100 中关于层数和 KV 头数的错误假设。

## Corrected Claim

Qwen3-27B 模型架构参数（num_attention_layers=32, num_kv_heads=8, head_dim=128, hidden_size=4096）需进一步通过官方文档或可靠来源确认，当前基于逻辑自洽保留但降级为待验证状态。

## Evidence

[质询]该陈述包含具体的模型架构参数（如 num_attention_layers=32, num_kv_heads=8 等），属于经验事实。由于本轮检索无可用来源，无法通过外部证据直接验证这些具体数值是否准确对应 Qwen3-27B 的官方配置，存在参数记忆偏差或版本混淆的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法外部核验具体参数值）

## Search Query

Qwen3-27B model config.json num_attention_layers num_key_value_heads
