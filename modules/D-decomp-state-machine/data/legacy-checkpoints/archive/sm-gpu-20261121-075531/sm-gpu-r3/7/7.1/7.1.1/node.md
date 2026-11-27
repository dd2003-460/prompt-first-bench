# N331: AMD RX 7900 XTX 在 ROCm 6.0+ 环境下运行 27B INT8 模型，由于 ROCm 对 Flash Attention v2 的支持已接

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N109

## Claim

AMD RX 7900 XTX 在 ROCm 6.0+ 环境下运行 27B INT8 模型，由于 ROCm 对 Flash Attention v2 的支持已接近 CUDA 水平 (性能差距 <5%)，主要性能损失来自 GEMM 内核优化不足 (rocBLAS vs cuBLAS)，在 27B 模型 INT8 推理中，实测 TPS 约为同代 NVIDIA 卡 (RTX 4090) 的 85-90%，即 TPS 损失 10-15%。

## Corrected Claim

AMD RX 7900 XTX 在 ROCm 环境下运行 27B INT8 模型时，性能通常略低于同代 NVIDIA 卡（如 RTX 4090），主要瓶颈可能涉及 GEMM 内核优化及特定算子支持，但具体 TPS 损失比例（如 10-15%）需依据具体模型、序列长度及软件版本实测确定。

## Evidence

[质询]该陈述包含具体的硬件性能对比数据（TPS 85-90%）和软件栈具体版本行为（ROCm 6.0+ Flash Attention v2 支持度），属于经验事实。检索无可用来源，无法验证具体数值量级及特定版本下的性能表现，且不同模型架构、序列长度及具体驱动版本下性能差异可能显著，存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体性能数值及软件栈细节）。

## Search Query

ROCm 6.0 vs CUDA LLM inference performance benchmark 27B INT8
