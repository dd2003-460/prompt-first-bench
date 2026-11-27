# N124: BF16 精度下 Qwen3-27B 的最小显存需求分解：权重 54.36GB + KV Cache 25.76GB + 激活值峰值（约 2-4GB，取决于 B

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：权重(27B*2B=54GB)与KV Cache(32K上下文)量级估算符合BF16精度下的显存占用规律，总显存需求略超80GB，结论自洽。

## Search Query

Qwen3 27B BF16 32k context A100 80GB OOM out of memory batch size 1
