# N357: Qwen3-27B 的实际注意力配置为 GQA（Grouped Query Attention），具体 n_kv_heads=32（而非 N89 假设的 8 或

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N121

## Claim

Qwen3-27B 的实际注意力配置为 GQA（Grouped Query Attention），具体 n_kv_heads=32（而非 N89 假设的 8 或 N100 假设的 32 全注意力，需以官方 config.json 为准），head_dim=128，总层数 64 层（非 N89/N100 假设的 16 层），这是计算 KV Cache 准确值的必要修正参数。

## Corrected Claim

Qwen3-27B 采用 GQA 架构，具体参数（如 n_kv_heads, head_dim, 总层数）需以官方发布的 config.json 为准，当前检索无法确认具体数值为 n_kv_heads=32, head_dim=128, 64层。

## Evidence

[质询]该陈述包含具体的经验性技术参数（n_kv_heads=32, head_dim=128, 64层），属于模型架构的具体配置细节。虽然Qwen3-27B确实存在且通常采用GQA，但具体的数值（如KV头数是否为32，层数是否为64）属于经验事实，无法仅通过第一性原理推导得出。由于检索失败，无法通过外部来源直接验证这些具体数值是否准确，存在参数记忆偏差或版本差异的风险。 | 经验事实，逻辑自洽但缺来源支持。Qwen3-27B作为大语言模型，采用GQA、64层、head_dim=128符合当前主流大模型架构的常规量级和逻辑，但具体数值需官方config.json确认，当前无可用外部证据直接支持。

## Search Query

Qwen3-27B model config.json n_kv_heads num_hidden_layers attention
