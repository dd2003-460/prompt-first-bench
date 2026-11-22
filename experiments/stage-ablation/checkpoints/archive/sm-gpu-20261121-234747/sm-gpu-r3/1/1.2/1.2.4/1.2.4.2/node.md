# N183: AMD MI300X 在运行 Qwen3-27B INT8 时的软件栈成熟度评估：ROCm 5.7+ 对 PyTorch/vLLM 的支持程度，特别是 Flas

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

AMD MI300X 在运行 Qwen3-27B INT8 时的软件栈成熟度评估：ROCm 5.7+ 对 PyTorch/vLLM 的支持程度，特别是 FlashAttention-2/3 在 MI300X 上的优化状态及与 CUDA 版本的性能差距（通常报告为 10-20% 效率损失），量化其对 TCO 中运维人力成本的影响。

## Corrected Claim

AMD MI300X 在运行 Qwen3-27B INT8 时的软件栈成熟度评估：ROCm 对 PyTorch/vLLM 的支持程度及 FlashAttention 优化状态需进一步验证，通常报告存在一定效率损失，具体数值及 TCO 影响需结合实际基准测试数据。

## Evidence

[质询]该陈述包含具体的经验性数值（10-20%效率损失）和特定软件版本支持状态（ROCm 5.7+），属于硬件/软件生态的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

AMD MI300X ROCm vLLM Qwen3-27B performance gap vs CUDA 2025
