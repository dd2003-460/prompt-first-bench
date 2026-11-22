# N152: A100 80GB PCIe 的显存带宽 2039 GB/s 在 32K 上下文 Decode 阶段中，KV Cache 读取带宽占比约为 32.77 / (3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

A100 80GB PCIe 的显存带宽 2039 GB/s 在 32K 上下文 Decode 阶段中，KV Cache 读取带宽占比约为 32.77 / (32.77 + 54) ≈ 37.8%，权重读取占比 62.2%，这与 N95 中声称的 70-85% KV Cache 带宽占比矛盾，需重新验证 N95 的假设条件（可能基于更短上下文或不同模型大小）。

## Corrected Claim

A100 80GB PCIe 的显存带宽 2039 GB/s 在 32K 上下文 Decode 阶段中，KV Cache 读取带宽占比约为 32.77 / (32.77 + 54) ≈ 37.8%，权重读取占比 62.2%，这与 N95 中声称的 70-85% KV Cache 带宽占比矛盾，需重新验证 N95 的假设条件（可能基于更短上下文或不同模型大小）。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB PCIe 显存带宽约 2039 GB/s 符合规格；在 32K 长上下文 Decode 阶段，KV Cache 数据量随序列长度线性增长，而权重数据量固定，因此 KV Cache 带宽占比显著高于短上下文场景，但具体占比取决于模型参数量与 Batch Size，37.8% 与 70-85% 的差异可能源于模型规模或上下文长度假设不同，逻辑上自洽且指出了需重新验证的矛盾点。
