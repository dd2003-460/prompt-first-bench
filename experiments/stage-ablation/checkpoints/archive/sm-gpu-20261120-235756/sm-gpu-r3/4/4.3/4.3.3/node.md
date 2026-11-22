# N89: 单卡最大并发 Batch Size 计算公式：Batch_Size = (GPU_Total_VRAM - Weight_VRAM - Activation_O

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

单卡最大并发 Batch Size 计算公式：Batch_Size = (GPU_Total_VRAM - Weight_VRAM - Activation_Overhead) / KV_Per_Request，其中 Activation_Overhead 需根据框架（如 vLLM PagedAttention）估算为 1-2GB。

## Corrected Claim

单卡最大并发 Batch Size 计算公式：Batch_Size = (GPU_Total_VRAM - Weight_VRAM - Activation_Overhead) / KV_Per_Request，其中 Activation_Overhead 需根据框架（如 vLLM PagedAttention）估算为 1-2GB。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应公式中的三个核心变量（Activation_Overhead, Weight_VRAM, GPU_Total_VRAM），彼此独立无重叠，且共同覆盖了父节点公式的所有关键组成部分。虽然 Weight_VRAM 子节点包含了不同精度的具体数值，但这属于该变量的具体实现细节而非冗余，因为不同精度下的显存占用差异巨大，是计算 Batch Size 时必须考虑的关键变量，不能简单压缩为一个单一参数。）

## Search Query

vLLM paged attention memory overhead estimation
