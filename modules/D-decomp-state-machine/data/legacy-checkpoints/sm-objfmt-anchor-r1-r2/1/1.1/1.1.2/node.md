# N34: BF16 精度下 32K 上下文 KV Cache 精确计算公式：Mem_KV = 2 * num_layers * num_kv_heads * head_d

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

BF16 精度下 32K 上下文 KV Cache 精确计算公式：Mem_KV = 2 * num_layers * num_kv_heads * head_dim * seq_len * 2 bytes。代入 N30 参数得：2 * 32 * 4 * 128 * 32768 * 2 ≈ 2.1 GB (注意：此处需重新核算 head_dim，若 head_dim=128, kv_heads=4, layers=32, 则单层单序列 KV 为 4*128*32*2*2=65536 bytes/layer? 不，KV cache 是 per layer per head per token。正确公式：Layers * 2(K,V) * Heads_KV * Head_Dim * Seq_Len * Bytes。若 Qwen3-27B 类似 Llama3-70B 结构，需确切 head 数。假设 kv_heads=4, head_dim=128, layers=32: 32 * 2 * 4 * 128 * 32768 * 2 = 2,147,483,648 bytes ≈ 2 GB。这与 N5 声称的 8-12GB 有巨大出入，需核验 Qwen3-27B 的实际层数和 head 数，或者 N5 的估算包含了 Batch Size > 1 的情况。

## Corrected Claim

BF16 精度下 KV Cache 计算公式为 Mem_KV = 2 * num_layers * num_kv_heads * head_dim * seq_len * 2 bytes。若采用假设参数 (layers=32, kv_heads=4, head_dim=128, seq_len=32768)，计算结果约为 2 GB。但该结果依赖于未经验证的架构假设，需核实 Qwen3-27B 实际层数及 KV 头数以确定真实内存占用。

## Evidence

[质询]该陈述基于假设的架构参数（layers=32, kv_heads=4, head_dim=128）进行计算，这些参数并非 Qwen3-27B 的确切已知规格（Qwen3-27B 实际层数通常为 64 层左右，且 KV heads 数量可能不同），因此得出的 2GB 结论极可能因参数错误而严重低估实际内存需求，导致与 N5 的 8-12GB 对比失效。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，且核心参数为假设值，无法验证其对应真实模型规格。

## Search Query

Qwen3-27B architecture details number of layers attention heads dimensions
