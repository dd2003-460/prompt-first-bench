# N29: 推理吞吐量(tokens/s) = 有效显存带宽(GB/s) / (模型大小(GB) + KV缓存大小(GB))，其中KV缓存大小 = 2 * num_laye

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（子节点本质上是对同一公式在不同硬件参数下的实例化，存在严重的结构性冗余。虽然硬件类型（消费级/数据中心/统一内存）提供了分类视角，但三个子节点重复了相同的计算逻辑和数值假设（如KV Cache均固定为10.7GB，未体现不同硬件下的实际差异），且未覆盖父节点中提到的'batch size'和'精度'对KV缓存大小的影响，导致完备性不足。）
