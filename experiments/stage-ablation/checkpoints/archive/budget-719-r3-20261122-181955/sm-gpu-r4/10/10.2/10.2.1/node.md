# N369: 修正N89与N100矛盾：Qwen3-27B实际采用GQA架构，n_kv_heads=8（非N100假设的32，也非N89隐含的16/32混淆），head_di

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N124

## Claim

修正N89与N100矛盾：Qwen3-27B实际采用GQA架构，n_kv_heads=8（非N100假设的32，也非N89隐含的16/32混淆），head_dim=128，num_layers=64（修正N89/N100中错误的16层假设，Qwen3-27B实际为64层）。基于此，BF16下KV Cache per token大小 = 2 * 64 layers * 8 kv_heads * 128 head_dim * 2 bytes = 262,144 bytes = 256 KB/token。

## Corrected Claim

Qwen3-27B采用GQA架构，若其参数确为n_kv_heads=8, num_layers=64, head_dim=128，则BF16下KV Cache per token大小为256 KB。具体参数需以官方技术报告为准。

## Evidence

[质询]该陈述包含具体的模型架构参数（n_kv_heads=8, num_layers=64, head_dim=128），属于经验事实。虽然Qwen3-27B确实存在且通常采用GQA，但具体参数值（如是否为64层而非其他层数，kv_heads具体数值）需要官方技术报告或可靠来源直接支持。当前检索无可用来源，无法排除参数记忆偏差或版本差异的可能性。 | 经验事实，逻辑自洽但缺来源支持。计算过程 2 * 64 * 8 * 128 * 2 = 262,144 bytes 数学上正确，但参数本身缺乏外部证据验证。

## Search Query

Qwen3-27B architecture num_layers n_kv_heads head_dim config.json
