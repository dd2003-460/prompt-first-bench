# N63: Qwen3-27B 在 BF16 精度下，32K 上下文 KV Cache 的具体占用量计算公式：KV_Bytes = 2 * N_layers * N_kv_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16, N17, N18

## Claim

Qwen3-27B 在 BF16 精度下，32K 上下文 KV Cache 的具体占用量计算公式：KV_Bytes = 2 * N_layers * N_kv_heads * D_head * seq_len * bytes_per_param，需代入 Qwen3-27B 具体架构参数（N_layers, N_kv_heads, D_head）得出精确 GB 数，以验证 N12 中 16GB 估计的准确性。

## Corrected Claim

Qwen3-27B 在 BF16 精度下，32K 上下文 KV Cache 的占用量可通过公式 KV_Bytes = 2 * N_layers * N_kv_heads * D_head * seq_len * 2 计算，具体数值需依据官方发布的模型架构参数确定，以验证 N12 中 16GB 估计的准确性。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（Qwen3-27B的层数、KV头数、头维度），属于经验事实。由于检索失败，无法验证这些具体参数是否准确，也无法确认最终计算出的GB数是否与N12的16GB估计一致。 | 经验事实，逻辑自洽但缺来源支持。公式本身在逻辑上是正确的（KV Cache大小确实由层数、KV头数、头维度、序列长度和数据类型决定），但具体数值依赖于未经验证的模型架构参数。

## Search Query

Qwen3-27B architecture config N_layers N_kv_heads D_head huggingface
