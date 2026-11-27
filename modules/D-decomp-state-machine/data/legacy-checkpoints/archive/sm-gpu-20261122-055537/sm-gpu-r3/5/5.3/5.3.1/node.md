# N85: NVIDIA L4 运行 Qwen3-27B (FP8) 在 32K 上下文下的理论最大吞吐量上限为 48.75 tokens/s，计算公式为：T_max = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N26

## Claim

NVIDIA L4 运行 Qwen3-27B (FP8) 在 32K 上下文下的理论最大吞吐量上限为 48.75 tokens/s，计算公式为：T_max = Bandwidth (300 GB/s) / Model_Size_FP8 (27 GB) = 11.11 * 4.4 (KV Cache 占比修正系数，基于 32K 序列长度下 KV Cache 占用约 5-6GB 导致的带宽竞争衰减)。

## Corrected Claim

NVIDIA L4 运行 Qwen3-27B (FP8) 在 32K 上下文下的理论最大吞吐量上限约为 11.11 tokens/s（基于纯权重带宽限制 300GB/s / 27GB），实际吞吐量受 KV Cache 内存占用和计算开销影响会显著低于此值，具体数值需通过基准测试确定，原陈述中的 48.75 tokens/s 及 4.4 修正系数缺乏可靠依据。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于带宽参数修正与纯权重理论上限的重新计算（纠正父节点公式错误），子节点2聚焦于显存容量约束与KV Cache具体占用导致的可行性否定（指出父节点场景不可行）。两者分别处理了‘计算逻辑/参数’和‘物理约束/可行性’两个不同维度，无重复且无矛盾，共同覆盖了父节点中涉及的带宽、模型大小、KV Cache及最终结论的所有关键方面。）
