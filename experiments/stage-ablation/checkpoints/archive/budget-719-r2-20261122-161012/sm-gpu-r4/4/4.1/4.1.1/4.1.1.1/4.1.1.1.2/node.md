# N474: Qwen3-27B 的 head_dim (Head Dimension) 确认为 128，来源为 HuggingFace Qwen/Qwen3-27B 模型仓

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N196

## Claim

Qwen3-27B 的 head_dim (Head Dimension) 确认为 128，来源为 HuggingFace Qwen/Qwen3-27B 模型仓库的 config.json 文件字段 'head_dim': 128 或通过 'hidden_size' (4096) / 'num_attention_heads' (32) 计算得出，该参数是 KV Cache 单头大小的基础。

## Corrected Claim

Qwen3-27B 的 head_dim 通常为 128，但具体数值需依据 HuggingFace 仓库 config.json 中 'head_dim' 字段或 'hidden_size' 与 'num_attention_heads' 的实际配置确认，不同版本或架构变体可能存在差异。

## Evidence

[质询]数值量级与架构常识存在潜在冲突：Qwen3-27B 作为 27B 参数模型，其 hidden_size 通常为 4096 或 5120。若 hidden_size 为 4096 且 head_dim 为 128，则 num_attention_heads 应为 32。然而，许多现代大模型（包括 Qwen 系列）常采用 GQA (Grouped Query Attention) 或 MLA (Multi-head Latent Attention)，此时 'num_attention_heads' 可能指 KV heads 或逻辑头数，而物理 head_dim 可能不同（如 Qwen2/3 系列部分模型 head_dim 为 128，但需确认具体配置）。更关键的攻击点是：若 hidden_size 实际为 5120（27B 常见配置），则 5120/32=160，与 128 不符；或者若采用 GQA，head_dim 计算逻辑不同。由于缺乏来源，无法确认 hidden_size 确为 4096 且 num_heads 确为 32 且无 GQA 导致的维度变化。 | 经验事实，逻辑自洽但缺来源支持。虽然 4096/32=128 数学上成立，但 Qwen3-27B 的具体 hidden_size 和 attention 架构（是否 GQA/MLA）属于经验参数，无来源验证其具体数值组合。

## Search Query

Qwen3-27B config.json head_dim hidden_size site:huggingface.co
