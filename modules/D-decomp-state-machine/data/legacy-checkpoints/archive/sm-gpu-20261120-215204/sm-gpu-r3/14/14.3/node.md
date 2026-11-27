# N411: AMD MI300X 在 ROCm 平台上的软件栈稳定性风险量化：若关键算子 (如 FlashAttention) 未优化，回退到通用实现可能导致性能下降 20

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N155

## Claim

AMD MI300X 在 ROCm 平台上的软件栈稳定性风险量化：若关键算子 (如 FlashAttention) 未优化，回退到通用实现可能导致性能下降 20-30%，即实际吞吐从理论 59-68 Tokens/s 降至 41-55 Tokens/s，需通过基准测试验证具体损失幅度。

## Corrected Claim

AMD MI300X 在 ROCm 平台上的软件栈稳定性存在风险：若关键算子 (如 FlashAttention) 未优化，回退到通用实现可能导致显著性能下降（通常估计在 20-30% 左右），具体损失幅度需通过基准测试验证。

## Evidence

[质询]该陈述包含具体的经验性数值（20-30%性能下降、具体吞吐区间），属于硬件/软件性能经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

ROCm MI300X FlashAttention performance loss benchmark Qwen3 27B
