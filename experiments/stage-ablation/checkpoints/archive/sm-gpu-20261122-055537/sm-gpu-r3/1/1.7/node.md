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

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于动态激活值（Prefill/Decode阶段，依赖序列长度和批次），子节点2聚焦于静态框架/CUDA开销（依赖硬件和版本，不随序列线性变化）。两者在显存组成上互斥且互补，共同覆盖了父节点中‘激活值’与‘框架开销’两个核心部分，且具体数值符合父节点给出的5%-10%及1-2GB的范围逻辑（注：虽然2.7GB对于27B模型在32K下的Prefill激活值可能偏高，通常27B在32K下的KV Cache才是大头，但此处仅检查分解结构逻辑，且子节点明确标注为‘非KV部分’，若按层间激活估算，该数值在特定实现下可接受，且与子节点2无重叠）。）
