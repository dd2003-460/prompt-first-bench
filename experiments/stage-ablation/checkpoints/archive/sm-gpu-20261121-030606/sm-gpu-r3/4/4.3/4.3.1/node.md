# N129: 修正N21的总显存公式：Total_Mem = W_precision + KV_Cache + Activation_Peak + Framework_Ove

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

修正N21的总显存公式：Total_Mem = W_precision + KV_Cache + Activation_Peak + Framework_Overhead。N21中BF16下65GB = 54GB (权重) + 5.2GB (KV) + 2.5GB (激活) + 3.3GB (其他/碎片/Overhead)。需明确Framework_Overhead的构成（CUDA Context, cuDNN buffers等）。

## Corrected Claim

修正N21的总显存公式：Total_Mem = W_precision + KV_Cache + Activation_Peak + Framework_Overhead。N21中BF16下65GB = 54GB (权重) + 5.2GB (KV) + 2.5GB (激活) + 3.3GB (其他/碎片/Overhead)。需明确Framework_Overhead的构成（CUDA Context, cuDNN buffers等）。

## Evidence

父节点级核验未通过：不完备（子节点分别处理了 Framework_Overhead 和 Activation_Peak 两个不同项，内容正交且无冗余。但父节点明确列出了四个组成部分（权重、KV、激活、开销），并特别要求修正公式及明确开销构成。子节点仅覆盖了后两项，缺失了对 W_precision（权重显存）和 KV_Cache 的验证或修正，未完全覆盖父节点中‘总显存公式’的所有关键方面（尽管前两项可能在其他节点处理，但就本父节点的‘修正公式’任务而言，分解显得不完整，因为它没有确认前两项是否正确或是否也需要类似修正，导致公式闭环缺失）。）

## Search Query

GPU memory overhead CUDA context inference
