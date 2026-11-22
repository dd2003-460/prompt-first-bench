# N306: AMD Radeon PRO W7900 在 INT8 量化下运行 Qwen3-27B 的算子覆盖度：ROCm 的 ONNX Runtime 或 PyTorch

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N103, N104, N105

## Claim

AMD Radeon PRO W7900 在 INT8 量化下运行 Qwen3-27B 的算子覆盖度：ROCm 的 ONNX Runtime 或 PyTorch 后端对 GEMM、LayerNorm、RMSNorm 等核心算子的 INT8 加速支持完整，但 FlashAttention-2 在 INT8 下的性能未优化，可能导致 Attention 层耗时增加 20-30%。

## Corrected Claim

AMD Radeon PRO W7900 在 INT8 量化下运行 Qwen3-27B 时，ROCm 后端对核心算子（如 GEMM、RMSNorm）通常具备加速支持，但 FlashAttention-2 在 INT8 下的优化程度可能不足，导致 Attention 层性能相较于 FP16 或优化后的 INT8 实现存在一定开销，具体性能损耗需实测确定。

## Evidence

[质询]该陈述包含具体的性能量化数据（'耗时增加 20-30%'）和特定硬件/软件栈的兼容性断言（'ROCm 对...支持完整'），属于经验事实。在缺乏任何参考来源支持的情况下，无法验证该具体数值量级及'支持完整'这一绝对化表述的准确性，且不同模型架构（如 Qwen3 是否使用 RMSNorm 而非 LayerNorm）可能导致算子覆盖度描述不精确。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

ROCm INT8 quantization operator coverage Qwen3 FlashAttention-2 performance
