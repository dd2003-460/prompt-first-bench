# N257: FP8 精度下总内存需求修正值：Weights (27GB) + KV_Cache (2.15GB) + Overhead (3GB) = 32.15 GB。该

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：算术求和 27+2.15+3=32.15 正确；32.15GB 确实大于 24GB 且小于 48GB，符合硬件容量排除逻辑。
