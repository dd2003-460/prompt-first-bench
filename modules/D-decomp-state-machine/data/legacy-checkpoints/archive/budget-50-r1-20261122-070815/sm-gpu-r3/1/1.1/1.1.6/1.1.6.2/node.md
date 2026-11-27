# N170: Qwen3-27B 在 INT4 精度下，KV Cache 计算中假设 num_key_value_heads=4 (GQA)，需验证 config.json 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

Qwen3-27B 在 INT4 精度下，KV Cache 计算中假设 num_key_value_heads=4 (GQA)，需验证 config.json 中 num_key_value_heads 的实际值，若为 MHA (32 heads) 则显存占用将扩大 8 倍至 2.16 GB，直接影响单卡可行性判断。

## Corrected Claim

Qwen3-27B 在 INT4 精度下，KV Cache 计算中假设 num_key_value_heads=4 (GQA)。需验证 config.json 中 num_key_value_heads 的实际值；若为 MHA (32 heads)，KV Cache 显存占用将扩大 8 倍，可能影响单卡可行性判断。

## Evidence

[质询]该陈述包含具体的硬件/模型配置参数（num_key_value_heads=4, 显存占用2.16GB），属于经验事实。由于检索失败，无法验证Qwen3-27B的实际config.json中num_key_value_heads是否为4，也无法确认2.16GB这一具体数值是否准确（取决于序列长度、batch size等未明确变量）。 | 经验事实，逻辑自洽但缺来源支持。GQA机制下KV Cache显存占用与num_key_value_heads成正比，若从4头变为32头（MHA），显存占用确实会扩大8倍，逻辑推导成立，但具体数值2.16GB及实际配置值无法通过现有来源验证。

## Search Query

Qwen3-27B config.json num_key_value_heads GQA configuration
