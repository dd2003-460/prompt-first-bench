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

父节点级核验未通过：非正交, 有冗余（子节点2（算子工作区）和子节点3（激活值峰值）存在概念重叠和矛盾。在Transformer推理中，Attention和FFN层的中间激活值通常就是算子（如FlashAttention, GEMM）的工作区内容，两者难以严格物理隔离。此外，父节点声称总开销为2-4GB，但子节点2（1-2GB）与子节点3（1.5-3GB）简单相加即为2.5-5GB，加上子节点1（0.5-1.5GB），总和达到3-6.5GB，超出了父节点定义的2-4GB范围，存在数值矛盾。）
