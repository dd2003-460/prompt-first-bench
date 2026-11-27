# N149: 对比基准量化：RTX 4090 (1008 GB/s) 与 M2 Ultra (800 GB/s) 在运行 Qwen3-27B FP8 (权重 27GB) 时的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

对比基准量化：RTX 4090 (1008 GB/s) 与 M2 Ultra (800 GB/s) 在运行 Qwen3-27B FP8 (权重 27GB) 时的理论 Decode 吞吐比为 1008/800 = 1.26:1；但若计入 N47 中的软件栈效率差异 (50-70%)，M2 Ultra 的实际相对吞吐可能降至 RTX 4090 的 63-88%。

## Corrected Claim

对比基准量化：RTX 4090 (1008 GB/s) 与 M2 Ultra (800 GB/s) 在运行 Qwen3-27B FP8 (权重 27GB) 时的理论 Decode 吞吐比为 1008/800 = 1.26:1；但若计入 N47 中的软件栈效率差异 (50-70%)，M2 Ultra 的实际相对吞吐可能降至 RTX 4090 的 63-88%。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽比 1008/800=1.26 计算正确；软件效率区间 50-70% 与 63-88% 的推导逻辑自洽（1/1.26≈0.79，结合效率波动范围合理）。
