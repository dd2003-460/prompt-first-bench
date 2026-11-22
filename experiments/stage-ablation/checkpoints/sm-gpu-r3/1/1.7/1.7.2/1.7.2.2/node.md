# N184: 在 32K (32,768 tokens) 上下文窗口下，Qwen3-27B 的 KV Cache 总大小计算：BF16 模式下为 32,768 * 256 K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

在 32K (32,768 tokens) 上下文窗口下，Qwen3-27B 的 KV Cache 总大小计算：BF16 模式下为 32,768 * 256 KB = 8,388,608 KB ≈ 8 GB；FP8 模式下为 32,768 * 128 KB = 4,194,304 KB ≈ 4 GB。相比 BF16，KV Cache 节省 4 GB (50%)。

## Corrected Claim

在 32K (32,768 tokens) 上下文窗口下，Qwen3-27B 的 KV Cache 总大小计算：BF16 模式下为 32,768 * 256 KB = 8,388,608 KB ≈ 8 GB；FP8 模式下为 32,768 * 128 KB = 4,194,304 KB ≈ 4 GB。相比 BF16，KV Cache 节省 4 GB (50%)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（如层数、头数、头维度）决定了每 token KV Cache 大小在 BF16 下约为 256KB，FP8 减半为 128KB，计算过程 32768 * 256KB = 8GB 及 32768 * 128KB = 4GB 数学正确，节省 50% 符合精度减半的线性关系。
