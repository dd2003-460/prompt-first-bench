# N163: 2x RTX 4090 (PCIe 4.0) 运行 FP8 Qwen3-27B 的推理吞吐效率折损因子为 0.6-0.8，源于每层 All-Reduce 通信延

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

2x RTX 4090 (PCIe 4.0) 运行 FP8 Qwen3-27B 的推理吞吐效率折损因子为 0.6-0.8，源于每层 All-Reduce 通信延迟 (PCIe 带宽 ~32 GB/s) 与计算时间的重叠不足，导致有效 tokens/s 低于单卡理想值的 80%。

## Corrected Claim

2x RTX 4090 (PCIe 4.0) 运行 FP8 Qwen3-27B 的推理吞吐效率通常低于单卡理想值，折损因子受并行策略、序列长度及通信/计算重叠程度影响，典型范围可能在0.6-0.8之间，但非固定常数。

## Evidence

[质询]数值量级与具体折损因子（0.6-0.8）缺乏通用性，高度依赖具体模型架构（如是否使用张量并行/流水线并行）、序列长度及硬件拓扑，将其作为固定经验参数表述过于绝对；且PCIe 4.0 x16双向带宽通常为64GB/s，单向32GB/s，若通信与计算重叠不足，实际瓶颈可能更复杂，简单归因于'重叠不足'可能忽略其他开销（如内存带宽瓶颈）。 | 先验知识/题面给定，逻辑校验通过：多卡推理因通信开销导致效率低于单卡理想值符合基本直觉，但具体折损因子0.6-0.8为经验估计值，无来源直接支持，且受多种变量影响，故降级为定性表述。

## Search Query

PCIe 4.0 tensor parallelism overhead LLM inference efficiency loss
