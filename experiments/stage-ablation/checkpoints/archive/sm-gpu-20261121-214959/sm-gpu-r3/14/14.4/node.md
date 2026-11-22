# N358: Intel Gaudi 2/3 排除的具体量化依据：截至 2024 年 Q3，PyTorch 对 Gaudi 2 的官方支持版本滞后于 CUDA 12.1 约 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N128, N129

## Claim

Intel Gaudi 2/3 排除的具体量化依据：截至 2024 年 Q3，PyTorch 对 Gaudi 2 的官方支持版本滞后于 CUDA 12.1 约 6-9 个月；vLLM 对 Gaudi 的支持仍处于实验阶段 (Experimental)，缺乏生产级 PagedAttention 优化，导致长上下文 (32K) 下的 KV Cache 管理效率比 CUDA 方案低 20-40% [待核验]。

## Corrected Claim

截至 2024 年 Q3，PyTorch 对 Gaudi 2 的生态支持成熟度低于 CUDA 12.1；vLLM 对 Gaudi 的支持仍处于实验阶段，缺乏生产级 PagedAttention 优化，导致长上下文 (32K) 下的 KV Cache 管理效率显著低于 CUDA 方案。

## Evidence

[质询]具体数值（6-9个月滞后、20-40%效率差距）缺乏公开基准测试或官方文档的直接支持，属于难以从第一性原理推导的经验性工程指标，且'官方支持版本滞后'的口径（是PyTorch版本还是Gaudi软件栈版本）存在模糊性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体量化数据）

## Search Query

Intel Gaudi 2 PyTorch vLLM support status 2024
