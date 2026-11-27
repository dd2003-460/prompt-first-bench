# N244: Mac Studio M2 Ultra (192GB) 的 GPU 算力规格：统一内存架构下 GPU 共享内存带宽，GPU 峰值算力约为 74 TFLOPS (

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

Mac Studio M2 Ultra (192GB) 的 GPU 算力规格：统一内存架构下 GPU 共享内存带宽，GPU 峰值算力约为 74 TFLOPS (FP32) 或 148 TFLOPS (BF16/FP16)，相比 NVIDIA RTX 4090 (82.6 TFLOPS FP32 / 165.2 TFLOPS TF32) 在峰值算力上具备优势，但受限于内存带宽 (800 GB/s vs 1008 GB/s) 导致 Decode 阶段性能瓶颈。

## Corrected Claim

Mac Studio M2 Ultra (192GB) 的 GPU 算力规格：统一内存架构下 GPU 共享内存带宽，GPU 峰值算力约为 74 TFLOPS (FP32) 或 148 TFLOPS (BF16/FP16)，相比 NVIDIA RTX 4090 (82.6 TFLOPS FP32 / 165.2 TFLOPS TF32) 在峰值算力上具备优势，但受限于内存带宽 (800 GB/s vs 1008 GB/s) 导致 Decode 阶段性能瓶颈。

## Evidence

父节点级核验未通过：非正交, 不完备（子节点严重偏离父节点主题。父节点讨论的是 Mac Studio M2 Ultra 的 GPU 算力与内存带宽瓶颈，而所有 4 个子节点均围绕 NVIDIA H100 SXM 80GB 运行 Qwen3-27B 的显存占用、Batch Size 及成本计算展开，完全未涉及 Mac Studio 或 M2 Ultra 的相关参数（如 192GB 统一内存、800GB/s 带宽下的具体表现）。此外，子节点内部存在逻辑矛盾：子节点 1 称模型加载需 54GB，子节点 3 称 Batch Size=2 时总占用 79.16GB，这意味着单 Batch 仅占 25.08GB，与子节点 1 的 54GB 基础权重+开销严重冲突，数据不自洽。）
