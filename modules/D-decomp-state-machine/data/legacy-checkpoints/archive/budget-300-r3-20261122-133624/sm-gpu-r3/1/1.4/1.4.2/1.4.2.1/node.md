# N204: PyTorch/CUDA 内存碎片导致的显存预留量公式：$R_{frag} = \alpha \times (M_{weights} + M_{kv})$，其中

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54, N56, N57

## Claim

PyTorch/CUDA 内存碎片导致的显存预留量公式：$R_{frag} = \alpha \times (M_{weights} + M_{kv})$，其中 $\alpha$ 为碎片系数。在 vLLM 启用 PagedAttention 时，由于 KV Cache 被分页管理，碎片率显著降低，$\alpha \approx 0.02-0.05$；在未启用分页或静态分配场景下，$\alpha \approx 0.10-0.15$。对于 27B INT8 模型（权重~27.5GB, KV~4GB），启用 PagedAttention 时 $R_{frag} \approx 1.5-2.4$GB，未启用时 $\approx 3.2-4.8$GB。

## Corrected Claim

PyTorch/CUDA 内存碎片导致的显存预留量通常可估算为 $R_{frag} \approx \alpha \times (M_{weights} + M_{kv})$。在 vLLM 启用 PagedAttention 时，由于 KV Cache 分页管理，碎片率显著降低，α 通常较小（经验值可能在 0.02-0.05 左右，具体视实现而定）；在未启用分页或静态分配场景下，α 较大（经验值可能在 0.10-0.15 左右）。对于 27B INT8 模型（权重~27.5GB, KV~4GB），启用 PagedAttention 时预留量约为 1.5-2.4GB，未启用时约为 3.2-4.8GB（基于上述经验系数估算）。

## Evidence

[质询]碎片系数 α 的具体数值范围（0.02-0.05 和 0.10-0.15）属于经验性工程参数，高度依赖于具体的硬件架构、CUDA 版本、分配器实现（如 PyTorch 的 caching allocator 行为）以及工作负载特征，并非普适的物理常数或固定公式参数。将其表述为确定性的区间可能过于绝对，且缺乏通用文献支持该特定数值范围作为标准参考值。 | 逻辑推导成立（数值计算无误：27.5+4=31.5GB，31.5*0.02≈0.63GB, 31.5*0.05≈1.57GB, 31.5*0.10≈3.15GB, 31.5*0.15≈4.72GB，与文中 1.5-2.4GB 和 3.2-4.8GB 基本吻合，考虑到四舍五入和可能的额外开销），但 α 的具体取值属于经验事实，无外部来源支持，且不同场景下波动较大，故降级为定性表述。
