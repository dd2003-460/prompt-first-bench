# N14: 推理框架开销（Overhead）估算：包括CUDA上下文、算子工作区、激活值峰值等，通常占额外2-4GB显存；对于27B模型，建议预留总显存的10-15%作为安

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

推理框架开销（Overhead）估算：包括CUDA上下文、算子工作区、激活值峰值等，通常占额外2-4GB显存；对于27B模型，建议预留总显存的10-15%作为安全余量，即Minimum_VRAM = Memory_Weights + Memory_KV + 0.15 * (Memory_Weights + Memory_KV)

## Corrected Claim

推理框架开销（Overhead）估算：包括CUDA上下文、算子工作区、激活值峰值等，通常占额外2-4GB显存；对于27B模型，建议预留总显存的10-15%作为安全余量，即Minimum_VRAM = Memory_Weights + Memory_KV + 0.15 * (Memory_Weights + Memory_KV)

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2（算子工作区）和子节点3（激活值峰值）存在严重重叠和概念混淆。在Transformer推理中，算子（如Attention、GEMM）所需的'Workspace'通常就是用于存储中间激活值（Activations）的临时显存，二者并非独立相加的开销，而是同一物理显存的不同视角或包含关系。此外，子节点2中提到的'峰值占用通常为最大激活张量的2-3倍'与子节点3中直接估算激活值峰值在逻辑上相互矛盾且难以独立量化，导致计算时可能重复计算或逻辑混乱。）
