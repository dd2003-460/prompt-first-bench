# N73: BF16 单卡方案的 Decode 吞吐量理论上限 = 显存带宽 (GB/s) / 模型权重大小 (GB) = 1008 GB/s (RTX 4090) / 5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17, N18, N19

## Claim

BF16 单卡方案的 Decode 吞吐量理论上限 = 显存带宽 (GB/s) / 模型权重大小 (GB) = 1008 GB/s (RTX 4090) / 54 GB ≈ 18.7 tokens/s；实际受限于 CUDA 内核启动开销、KV Cache 读取及框架调度，实测吞吐量通常为理论值的 60-80%，即约 11-15 tokens/s。

## Corrected Claim

BF16 单卡方案的 Decode 吞吐量理论上限 = 显存带宽 (GB/s) / 模型权重大小 (GB) = 1008 GB/s (RTX 4090) / 54 GB ≈ 18.7 tokens/s；实际受限于 CUDA 内核启动开销、KV Cache 读取及框架调度，实测吞吐量通常为理论值的 60-80%，即约 11-15 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：1008/54≈18.7 计算正确，60-80% 效率区间符合 LLM 推理工程常识
