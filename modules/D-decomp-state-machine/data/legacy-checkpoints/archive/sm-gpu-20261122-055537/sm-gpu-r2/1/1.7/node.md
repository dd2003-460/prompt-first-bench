# N13: 激活值与框架开销估算：推理时激活值峰值通常占权重大小的5%-10%（取决于batch size和seq length），加上CUDA Context和框架（如v

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

激活值与框架开销估算：推理时激活值峰值通常占权重大小的5%-10%（取决于batch size和seq length），加上CUDA Context和框架（如vLLM/llama.cpp）基础开销约1-2GB，作为总显存需求的缓冲项。

## Corrected Claim

激活值与框架开销估算：推理时激活值峰值通常占权重大小的5%-10%（取决于batch size和seq length），加上CUDA Context和框架（如vLLM/llama.cpp）基础开销约1-2GB，作为总显存需求的缓冲项。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1专注于动态激活值（Prefill/Decode），子节点2专注于静态框架/上下文开销，两者在概念上严格正交（动态 vs 静态），且共同覆盖了父节点中提到的‘激活值峰值’和‘框架基础开销’两个核心维度。虽然子节点1引入了特定模型（Qwen3-27B）的具体数值，而父节点是通用比例，但这属于从通用规则到具体实例的合理细化，不构成冗余或矛盾。）
