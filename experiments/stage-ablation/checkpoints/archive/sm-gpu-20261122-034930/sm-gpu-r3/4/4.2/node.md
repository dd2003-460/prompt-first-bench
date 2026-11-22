# N29: 推理吞吐量(tokens/s) = 有效显存带宽(GB/s) / (模型大小(GB) + KV缓存大小(GB))，其中KV缓存大小 = 2 * num_laye

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4

## Claim

推理吞吐量(tokens/s) = 有效显存带宽(GB/s) / (模型大小(GB) + KV缓存大小(GB))，其中KV缓存大小 = 2 * num_layers * num_kv_heads * head_dim * seq_len * batch_size * dtype_size，对于Qwen3-27B（假设64层，8 KV heads，128 head_dim），32K上下文下KV缓存约为1.5-3GB（取决于batch size和精度）[待核验：Qwen3-27B具体架构参数]

## Corrected Claim

推理吞吐量(tokens/s) ≈ 有效显存带宽(GB/s) / (模型大小(GB) + KV缓存大小(GB))，其中KV缓存大小 = 2 * num_layers * num_kv_heads * head_dim * seq_len * batch_size * dtype_size。对于Qwen3-27B，在32K上下文下，KV缓存大小需根据具体架构参数（层数、KV头数等）和batch size、精度进行计算，通常范围可能在1.5-3GB或更高，具体数值待架构参数确认。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别代表了三种不同硬件架构（消费级独显、数据中心HBM、统一内存SoC）的工作点，彼此在硬件特性上正交且互不重复。虽然计算逻辑相同，但它们是为了验证公式在不同带宽/容量权衡下的适用性，而非简单的参数重复。覆盖了三类主流部署场景，具备完备性。）
