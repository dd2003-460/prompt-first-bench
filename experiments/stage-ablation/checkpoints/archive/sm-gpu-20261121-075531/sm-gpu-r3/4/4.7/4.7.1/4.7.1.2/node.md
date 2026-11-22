# N305: Qwen3-27B 在 32K 上下文、Batch Size=1 下 KV Cache 的总显存占用 (KV_Cache_Total_Bytes)：计算公式为 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N100

## Claim

Qwen3-27B 在 32K 上下文、Batch Size=1 下 KV Cache 的总显存占用 (KV_Cache_Total_Bytes)：计算公式为 2 (K+V) * num_layers * num_kv_heads * head_dim * seq_len * bytes_per_elem。需代入 Qwen3-27B 具体层数和头数计算精确值（预计约 1.5-2.5 GB）。

## Corrected Claim

Qwen3-27B 在 32K 上下文、Batch Size=1 下 KV Cache 的总显存占用计算公式为 2 * num_layers * num_kv_heads * head_dim * seq_len * bytes_per_elem。具体数值需依据 Qwen3-27B 的实际架构参数（层数、KV 头数、头维度）计算，预计量级在 GB 级别。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（层数、头数、维度）及由此推导的显存占用数值，属于经验事实。由于缺乏参考来源支持，无法验证 Qwen3-27B 的具体架构参数（如是否采用 GQA、具体的 num_kv_heads 和 head_dim）是否准确，进而无法确认 1.5-2.5 GB 这一数值范围的精确性。 | 经验事实，逻辑自洽但缺来源支持。公式结构正确，量级估算（27B 模型在 32K 上下文下 KV Cache 占用 GB 级别）符合一般大语言模型显存占用规律，但具体数值依赖未提供的架构细节。

## Search Query

Qwen3-27B KV cache size 32k context calculation layers heads
