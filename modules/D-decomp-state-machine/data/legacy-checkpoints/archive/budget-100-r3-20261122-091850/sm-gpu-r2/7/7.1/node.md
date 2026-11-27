# N108: 模型结构参数验证：检索 Qwen3-27B 官方配置 (config.json) 或 HuggingFace 模型卡，确认 num_layers, hidden

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

模型结构参数验证：检索 Qwen3-27B 官方配置 (config.json) 或 HuggingFace 模型卡，确认 num_layers, hidden_dim, num_attention_heads, num_key_value_heads, head_dim 的具体整数值，以替代 N31 中的假设值 (64, 4096, 8, 128)，确保 KV Cache 计算基于真实架构而非近似。

## Corrected Claim

需通过有效渠道（如 HuggingFace 或官方文档）检索 Qwen3-27B 的 config.json 以获取真实的 num_layers, hidden_dim, num_attention_heads, num_key_value_heads, head_dim 数值，当前无法基于假设值进行精确验证。

## Evidence

[质询]该陈述旨在获取具体的经验事实（模型架构参数），但当前检索通道全部失败，缺乏外部来源支持，无法确认具体数值是否准确。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无可用外部证据）

## Search Query

Qwen3-27B config.json num_layers hidden_dim num_key_value_heads
