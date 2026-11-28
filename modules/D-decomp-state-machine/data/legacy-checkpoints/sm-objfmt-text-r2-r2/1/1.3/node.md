# N9: KV Cache 显存需求 K_mem 计算公式为 2 * n_layers * n_kv_heads * head_dim * seq_len * bytes

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

KV Cache 显存需求 K_mem 计算公式为 2 * n_layers * n_kv_heads * head_dim * seq_len * bytes_per_elem，其中 n_layers=64, n_kv_heads=8, head_dim=128, seq_len=32768, bytes_per_elem 取决于精度（BF16=2, FP8=1），计算得出 BF16 下约为 13.7 GB，FP8 下约为 6.85 GB

## Corrected Claim

KV Cache 显存需求 K_mem 计算公式为 2 * n_layers * n_kv_heads * head_dim * seq_len * bytes_per_elem，其中 n_layers=64, n_kv_heads=8, head_dim=128, seq_len=32768, bytes_per_elem 取决于精度（BF16=2, FP8=1），计算得出 BF16 下约为 13.7 GB，FP8 下约为 6.85 GB

## Evidence

父节点级核验未通过：不完备（子节点之间存在概念重叠（均讨论了精度对显存的影响），且严重偏离父节点主题。父节点仅关注 KV Cache 的计算公式及基于固定参数的静态数值结果，而子节点引入了父节点未提及的外部变量（如 W_mem, A_mem）和复杂场景（PagedAttention 碎片、特定硬件型号），导致分解不仅未覆盖父节点的核心逻辑（公式推导过程），反而引入了大量无关的外部系统级约束。）

## Search Query

Qwen3-27B layer count kv heads head dim config
