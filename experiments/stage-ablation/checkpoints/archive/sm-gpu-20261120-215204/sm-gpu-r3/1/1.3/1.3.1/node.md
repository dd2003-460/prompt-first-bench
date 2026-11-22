# N43: Qwen3-27B 在 4-bit 量化 (W4A8/W4A16) 下，32K 上下文 KV Cache 的精确显存占用为 40.96 GB，计算公式为 2 *

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

Qwen3-27B 在 4-bit 量化 (W4A8/W4A16) 下，32K 上下文 KV Cache 的精确显存占用为 40.96 GB，计算公式为 2 * 64 * 8 * 128 * 32768 * 2 (字节/参数)，因 KV Cache 保持 BF16 精度以保证注意力计算稳定性。

## Corrected Claim

Qwen3-27B 在 32K 上下文下，KV Cache 的显存占用取决于具体架构参数（层数、KV头数、Head Dim）。若按典型配置（如 64 层，8 KV 头，128 维，BF16），占用约为 8.59 GB，而非 40.96 GB。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1准确对应父节点的核心结论（BF16精度，40.96GB），子节点2提供了对比场景（INT8精度，20.48GB），两者在量化精度维度上互斥且互补，无逻辑矛盾或重复。父节点主要陈述事实，子节点1复述事实，子节点2扩展了变量空间，覆盖了关键计算逻辑和精度权衡。）
