# N705: Qwen3-27B 的 n_kv_heads 确切值为 8，来源为 Hugging Face Qwen/Qwen3-27B config.json 文件 (ke

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N251, N252, N253

## Claim

Qwen3-27B 的 n_kv_heads 确切值为 8，来源为 Hugging Face Qwen/Qwen3-27B config.json 文件 (key: 'num_key_value_heads': 8)，该值与 N369/N370 中使用的参数一致，排除了 N100 中 n_kv_heads=32 的错误假设。

## Corrected Claim

Qwen3-27B 的 n_kv_heads 值据称在 Hugging Face config.json 中为 8，该值与 N369/N370 一致，但需进一步核实以排除 N100 中 n_kv_heads=32 的假设。

## Evidence

[质询]该陈述包含具体的经验性参数值（n_kv_heads=8），属于模型架构配置细节，无法通过第一性原理推导，且当前检索无可用来源支持，存在数值记忆错误或版本混淆的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法外部核验具体数值）

## Search Query

Qwen3-27B config.json num_key_value_heads 8
