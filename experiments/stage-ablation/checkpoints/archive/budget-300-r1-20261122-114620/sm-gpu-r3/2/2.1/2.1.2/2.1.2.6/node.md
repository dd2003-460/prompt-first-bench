# N185: ROCm 5.7 对 Qwen3-27B 的支持状态：截至 2024-11，ROCm 5.7 尚未原生支持 FlashAttention-2 的 AMD 优化内

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55, N56, N57

## Claim

ROCm 5.7 对 Qwen3-27B 的支持状态：截至 2024-11，ROCm 5.7 尚未原生支持 FlashAttention-2 的 AMD 优化内核，需回退到 PyTorch SDPA 后端，该后端在 AMD GPU 上的内存访问效率比 CUDA FA2 低约 20-25%，预计 ROCm 6.0 将引入 FA2 支持，届时吞吐有望提升至 18-19 tokens/s，接近 RTX 3090 水平。

## Corrected Claim

截至 2024-11，ROCm 5.7 对 Qwen3-27B 的 FlashAttention-2 支持可能不完善，需回退到 PyTorch SDPA 后端，导致性能低于 CUDA FA2；预计后续版本（如 ROCm 6.0）将改善 FA2 支持以提升吞吐。

## Evidence

[质询]该陈述包含多个具体的经验性数值（如内存效率低20-25%、吞吐18-19 tokens/s）和特定版本的时间线预测（ROCm 6.0引入FA2支持），这些属于具体的工程参数和市场/产品状态，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

ROCm 5.7 FlashAttention-2 support status AMD GPU inference optimization
