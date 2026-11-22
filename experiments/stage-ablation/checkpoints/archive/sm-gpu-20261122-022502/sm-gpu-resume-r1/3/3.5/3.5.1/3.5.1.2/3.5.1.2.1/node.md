# N749: TensorRT-LLM 中针对 RTX 4090 (Ada) 优化的 INT4/AWQ 解码内核具体实现名称（如 `gemm_int4` 或 `awq_gem

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N231

## Claim

TensorRT-LLM 中针对 RTX 4090 (Ada) 优化的 INT4/AWQ 解码内核具体实现名称（如 `gemm_int4` 或 `awq_gemm`）及其在 CUDA 12.4+ 下的峰值算力利用率 (MFU) 百分比，对比 vLLM 对应内核的 MFU 差值

## Corrected Claim

TensorRT-LLM 针对 RTX 4090 (Ada) 架构提供了优化的 INT4/AWQ 解码内核（具体实现名称需查阅官方文档或源码，如 `gemm_int4` 系列），其 MFU 通常高于 vLLM 对应内核，但具体 MFU 百分比及差值需依据实际基准测试数据确定，无法仅凭逻辑推导得出精确数值。

## Evidence

[质询]该陈述包含具体的硬件性能指标（MFU百分比）和内核实现名称，属于经验事实。由于缺乏任何参考来源支持，且不同内核实现（如AWQ vs GPTQ）及具体配置下的MFU数值波动较大，无法从第一性原理推导出具体的百分比数值，存在数值量级和具体实现名称不确定的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

TensorRT-LLM AWQ INT4 kernel implementation Ada Lovelace MFU efficiency
