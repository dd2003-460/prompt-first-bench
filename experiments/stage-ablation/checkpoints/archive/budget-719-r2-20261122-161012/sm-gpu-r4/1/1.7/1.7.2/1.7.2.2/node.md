# N184: 在 32K (32,768 tokens) 上下文窗口下，Qwen3-27B 的 KV Cache 总大小计算：BF16 模式下为 32,768 * 256 K

- **status**: pending
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

父节点级核验未通过：有冗余（子节点2和子节点3在逻辑结构上高度重复，它们仅因数据精度（BF16 vs FP8）导致的字节数不同而分开，本质上是同一公式在不同参数下的实例化，属于冗余分解。）
