# N300: Qwen3-27B 的 KV Cache 显存占用精确计算：需确认 num_kv_heads (GQA 配置，通常为 8 或 16 而非 32) 和 head_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

Qwen3-27B 的 KV Cache 显存占用精确计算：需确认 num_kv_heads (GQA 配置，通常为 8 或 16 而非 32) 和 head_dim (128)，公式为 2 * num_layers * num_kv_heads * head_dim * seq_len * bytes_per_element，以修正 N82 中可能高估的 7.0GB 数值。

## Corrected Claim

Qwen3-27B 的 KV Cache 显存占用需根据实际模型配置（num_kv_heads, head_dim, num_layers）通过公式 2 * num_layers * num_kv_heads * head_dim * seq_len * bytes_per_element 计算，以修正可能存在的估算偏差。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（num_kv_heads, head_dim, num_layers），属于经验事实。虽然公式逻辑正确，但缺乏来源确认 Qwen3-27B 的具体配置（如层数、KV头数），无法验证其是否确实能修正 N82 的 7.0GB 数值，且 'Qwen3-27B' 本身是否为真实存在的特定版本或仅为假设场景需进一步确认。 | 经验事实，逻辑自洽但缺来源支持。KV Cache 计算公式在逻辑上正确，但具体参数（num_kv_heads=8/16, head_dim=128）及最终数值修正结果缺乏外部来源直接验证。

## Search Query

Qwen3-27B architecture num_kv_heads head_dim GQA configuration
