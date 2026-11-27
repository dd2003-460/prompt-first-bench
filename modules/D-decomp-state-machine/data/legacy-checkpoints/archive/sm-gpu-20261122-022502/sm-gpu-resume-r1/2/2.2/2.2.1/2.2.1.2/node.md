# N177: H100 SXM5 运行 BF16 Qwen3-27B 在 32K 上下文、batch_size=1 下的激活值峰值显存占用约为 hidden_size * s

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

H100 SXM5 运行 BF16 Qwen3-27B 在 32K 上下文、batch_size=1 下的激活值峰值显存占用约为 hidden_size * seq_len * 2 * 2 / 1e9 = 4096 * 32768 * 4 / 1e9 ≈ 0.54GB，加上 CUDA Context 和框架缓冲 (~1.5GB)，总非权重/KV 开销约 2GB，故 13.42GB 余量充足，无 OOM 风险。

## Corrected Claim

H100 SXM5 运行 BF16 Qwen3-27B 在 32K 上下文、batch_size=1 下的激活值峰值显存占用需考虑 Attention 和 FFN 中间层，估算约为 4-5GB，加上 CUDA Context 和框架缓冲 (~1.5GB)，总非权重/KV 开销约 5.5-6.5GB，13.42GB 余量仍充足，但需确认具体推理框架的激活值优化策略。

## Evidence

父节点级核验未通过：不完备（子节点分别针对激活值、固定开销和余量/量化进行了正交分析，无重复或矛盾。但存在完备性缺失：父节点结论的核心前提是'13.42GB 余量'，这隐含了权重和 KV Cache 的具体占用量，但三个子节点均未验证或讨论权重大小（BF16 Qwen3-27B）及 KV Cache 在 32K 上下文下的具体显存占用，导致无法独立复核'余量充足'这一结论的算术正确性。此外，子节点1中提到的'FlashAttention'和'PagedAttention'主要影响 KV Cache 的存储方式和碎片，对'激活值'峰值（通常指中间层特征图）的影响描述略显混淆，需明确区分激活内存与 KV 内存。）
