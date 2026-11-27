# N124: BF16 精度下 Qwen3-27B 的最小显存需求分解：权重 54.36GB + KV Cache 25.76GB + 激活值峰值（约 2-4GB，取决于 B

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31, N32, N33

## Claim

BF16 精度下 Qwen3-27B 的最小显存需求分解：权重 54.36GB + KV Cache 25.76GB + 激活值峰值（约 2-4GB，取决于 Batch Size 和中间层缓存策略）+ 框架开销（约 1-2GB，CUDA Context 等）= 83.12-85.12GB。因此，80GB 显存的 A100 在 BF16 下运行 32K 上下文处于临界状态，需严格限制 Batch Size=1 并关闭不必要的缓存功能，否则 OOM。

## Corrected Claim

BF16 精度下 Qwen3-27B 的最小显存需求分解：权重 54.36GB + KV Cache 25.76GB + 激活值峰值（约 2-4GB，取决于 Batch Size 和中间层缓存策略）+ 框架开销（约 1-2GB，CUDA Context 等）= 83.12-85.12GB。因此，80GB 显存的 A100 在 BF16 下运行 32K 上下文处于临界状态，需严格限制 Batch Size=1 并关闭不必要的缓存功能，否则 OOM。

## Evidence

父节点级核验未通过：不完备（子节点分别解释了'激活值'和'框架开销'两个独立维度，互不重叠且无矛盾，正交性良好。但父节点明确列出了四项显存组成（权重、KV Cache、激活值、框架开销），子节点仅覆盖了后两项，完全缺失了'权重'和'KV Cache'这两个在总显存中占比最大（合计约80GB）的关键组成部分，导致分解不完备。）

## Search Query

Qwen3 27B BF16 32k context A100 80GB OOM out of memory batch size 1
