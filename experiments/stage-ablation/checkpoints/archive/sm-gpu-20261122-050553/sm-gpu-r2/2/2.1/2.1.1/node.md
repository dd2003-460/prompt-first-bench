# N54: Qwen3-27B 的实际架构参数需从 config.json 获取：假设 Layer=64 (非 32), Head=16, D_head=128, 则 KV

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

Qwen3-27B 的实际架构参数需从 config.json 获取：假设 Layer=64 (非 32), Head=16, D_head=128, 则 KV Cache 大小 = 2 * Layer * Head * D_head * Context_Length * Bytes_per_Element。对于 BF16, 32K 上下文，KV Cache = 2 * 64 * 16 * 128 * 32768 * 2 bytes = 4.3 GB (若双向注意力则 x2 = 8.6 GB)。此计算需修正 N12 中基于 Layer=32 的 16GB 估计，实际 KV Cache 占用可能显著低于 16GB。

## Corrected Claim

Qwen3-27B的KV Cache大小取决于其具体架构参数（如层数、KV头数、头维度及数据类型）。若假设Layer=64, KV_Head=16, D_head=128, BF16, 32K上下文，则KV Cache约为4.3GB。实际值需查阅官方config.json确认，可能因采用GQA/MQA等技术而显著低于基于全注意力头的估计。

## Evidence

[质询]该陈述基于假设的架构参数（Layer=64, Head=16, D_head=128）进行计算，但Qwen3-27B的实际架构参数（如层数、头数、头维度）属于经验事实，且不同版本或配置可能存在差异。若实际参数与假设不符（例如层数并非64，或使用了GQA/MQA导致KV头数减少），则计算结果将产生显著偏差。此外，'双向注意力'在标准Transformer解码器中通常不适用（除非是特定编码器-解码器架构或特殊设计），此处x2的修正逻辑可能基于错误的前提。 | 经验事实，逻辑自洽但缺来源支持。检索无可用来源，无法验证Qwen3-27B的具体架构参数（Layer/Head/D_head）及是否采用GQA/MQA，因此无法确认4.3GB/8.6GB的数值准确性，仅能确认计算公式在给定假设下的数学正确性。

## Search Query

Qwen3-27B config.json num_hidden_layers num_attention_heads hidden_size KV cache size
