# N12: 在 BF16 精度、Batch_Size=1、Seq_Len=32K 条件下，Qwen3-27B 的 KV Cache 占用约为 2 * 64 * 32 * 1

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

在 BF16 精度、Batch_Size=1、Seq_Len=32K 条件下，Qwen3-27B 的 KV Cache 占用约为 2 * 64 * 32 * 128 * 32768 * 2 bytes ≈ 34.4 GB [待核验：需确认是否采用 GQA 以减少 KV 头数]。

## Corrected Claim

在 BF16 精度、Batch_Size=1、Seq_Len=32K 条件下，若 Qwen3-27B 采用 MHA 架构（KV 头数=64），KV Cache 占用约为 34.4 GB；若采用 GQA 架构（如 KV 头数=8），占用将降至约 4.3 GB。需确认具体模型的注意力架构以获取准确数值。

## Evidence

[质询]该陈述假设 Qwen3-27B 采用 MHA（Multi-Head Attention）且 KV 头数等于 Query 头数（64），但 Qwen3 系列模型（包括 27B 版本）通常采用 GQA（Grouped Query Attention）或 MQA 架构以优化推理效率，其 KV 头数通常远小于 Query 头数（例如 8 或 16 而非 64）。若采用 GQA，实际 KV Cache 占用将显著低于 34.4 GB（可能仅为 1/4 或 1/8），因此基于 MHA 假设的计算结果可能严重高估内存占用。 | 参考来源 [1] 仅讨论精度定义，与 KV Cache 计算无关，无可用外部证据；逻辑上公式结构正确（2 * n_layers * n_kv_heads * head_dim * seq_len * bytes_per_elem），但关键参数 n_kv_heads=64 缺乏来源支持且与 Qwen3 常见架构（GQA）可能存在冲突，属于经验事实且缺来源直接支持，故降级。

## Search Query

Qwen3-27B KV cache size 32k context bf16

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1912129762048074069&rut=cd99ca270274da39f65192a9a274afca703b72cd151eab750eeb2a9f8f7a6731', 'type': 'ddg', 'title': '大模型精度：FP32、TF32、FP16、BF16、FP8、FP4、NF4、INT8'}
