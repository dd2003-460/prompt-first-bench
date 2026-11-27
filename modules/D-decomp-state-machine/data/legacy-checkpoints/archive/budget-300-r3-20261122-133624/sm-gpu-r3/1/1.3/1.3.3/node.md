# N51: 算子缓冲 (Activation Buffers) 在 Prefill 阶段峰值可达 1.0-2.0GB，取决于 Batch Size 和序列长度；在 Deco

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

算子缓冲 (Activation Buffers) 在 Prefill 阶段峰值可达 1.0-2.0GB，取决于 Batch Size 和序列长度；在 Decode 阶段通常 <0.5GB。N8 的 1.5-2.5GB 范围主要覆盖了 Prefill 阶段的峰值开销。

## Corrected Claim

算子缓冲 (Activation Buffers) 在 Prefill 阶段的峰值开销通常显著高于 Decode 阶段，具体数值（如 1.0-2.0GB）高度依赖于模型架构参数（如隐藏层维度、层数）及 Batch Size 和序列长度，需结合具体模型配置确定。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上正交，分别处理了Prefill主激活、Decode激活和FlashAttention工作空间。但存在两个主要问题：1. 完备性不足，父节点明确提到N8范围(1.5-2.5GB)覆盖了Prefill峰值，但子节点3的结论（总非KV开销<1GB）与父节点声明的范围（1.5-2.5GB）存在显著数值矛盾，未解释为何N8的上限远高于计算出的实际开销（可能是为了安全边际或包含其他未提及的临时缓冲，需明确说明）；2. 子节点3中FlashAttention工作空间的计算量级（4MB）对于现代大模型推理框架而言过小，通常FlashAttention v2/v3的workspace或中间状态开销在长序列下会显著更高，该数值可能低估了实际占用，导致对父节点范围的‘修正’缺乏说服力。）

## Search Query

vLLM prefill activation buffer memory peak GB batch size sequence length
