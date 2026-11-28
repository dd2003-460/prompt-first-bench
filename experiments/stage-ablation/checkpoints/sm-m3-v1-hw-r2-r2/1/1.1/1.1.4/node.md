# N37: 单请求最大上下文长度 (max_model_len=262144) 对应的 KV Cache 总显存需求为 262,144 tokens * 8 MB/toke

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

单请求最大上下文长度 (max_model_len=262144) 对应的 KV Cache 总显存需求为 262,144 tokens * 8 MB/token = 2048 GB，远超 48.5 GB 可用空间，证明在 V100 集群上无法原生支持 262k 上下文的完整 KV 存储，必须使用 PagedAttention 分页或截断

## Corrected Claim

单请求最大上下文长度 (max_model_len=262144) 对应的 KV Cache 总显存需求取决于具体模型架构。以 Llama-2-70B 为例，每 token 约 32KB，262k tokens 约需 8GB 显存，这在 48.5GB 空间内是可行的；但对于更大模型或更高精度，可能需要 PagedAttention 优化内存碎片，而非因为总量远超 48.5GB。原陈述中 8MB/token 的参数错误。

## Evidence

[质询]数值量级严重错误：8 MB/token 的 KV Cache 开销对于任何主流大语言模型（如 Llama 系列）都极不合理。通常 7B-70B 模型的 KV Cache 每 token 开销在 KB 到几十 MB 之间（取决于层数、头数和精度），绝不可能达到 8 MB/token。若按此计算，262k tokens 需要 2TB 显存，这违背了当前硬件和模型架构的基本常识。 | 逻辑校验失败：KV Cache 大小计算公式为 2 * num_layers * num_kv_heads * head_dim * dtype_size * seq_len。即使假设一个极大的模型（如 100+ 层，高维头），单 token 开销也远小于 8MB。例如 Llama-2-70B (80层, 8 KV heads, 128 dim, FP16) 每 token 约 32KB。8MB/token 意味着模型规模需达到数千亿参数级别且结构极端异常，这与 'V100 集群' 和常规 'max_model_len' 语境不符。此外，262,144 * 8MB = 2048GB 的算术正确，但前提参数错误导致结论无效。
