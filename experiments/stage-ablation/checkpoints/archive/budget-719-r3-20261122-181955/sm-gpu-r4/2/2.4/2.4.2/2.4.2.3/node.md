# N257: FP8 精度下总内存需求修正值：Weights (27GB) + KV_Cache (2.15GB) + Overhead (3GB) = 32.15 GB。该

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83, N84, N85

## Claim

FP8 精度下总内存需求修正值：Weights (27GB) + KV_Cache (2.15GB) + Overhead (3GB) = 32.15 GB。该数值确认适配 A6000 (48GB) 和 L40S (48GB)，但超出 RTX 4090 (24GB) 和 RTX 3090 (24GB) 的容量上限，排除这些消费级显卡在 FP8 下运行 32K 上下文的可行性。

## Corrected Claim

FP8 精度下总内存需求修正值：Weights (27GB) + KV_Cache (2.15GB) + Overhead (3GB) = 32.15 GB。该数值确认适配 A6000 (48GB) 和 L40S (48GB)，但超出 RTX 4090 (24GB) 和 RTX 3090 (24GB) 的容量上限，排除这些消费级显卡在 FP8 下运行 32K 上下文的可行性。

## Evidence

父节点级核验未通过：非正交（子节点之间存在数值矛盾：子节点2计算KV Cache为4.0GB，子节点4汇总总内存为33.5GB（基于4.0GB KV），但父节点明确陈述总内存为32.15GB（基于2.15GB KV）。子节点4的结论与父节点核心事实（总内存值）直接冲突，导致分解不一致。）
